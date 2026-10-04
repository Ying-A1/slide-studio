#!/usr/bin/env python3
"""
slide-studio — optional AI background generator.

Generates ONE image from an OpenAI-compatible `images/generations` endpoint and saves it.
No API key is bundled; configuration comes from the environment:

    IMAGE_API_BASE   e.g. https://your-endpoint/v1        (required)
    IMAGE_API_KEY    e.g. sk-...                           (required)
    IMAGE_MODEL      e.g. gpt-image-2                       (optional; default gpt-image-2)
    IMAGE_API_INSECURE=1   disable TLS verification         (last resort only)

Usage:
    python gen_image.py "SCENE ... + STYLE PARAGRAPH" out/cover.png [WIDTHxHEIGHT] [quality]

Example:
    export IMAGE_API_BASE="https://your-endpoint/v1"
    export IMAGE_API_KEY="sk-..."
    python gen_image.py "a vast floating celestial city above a sea of clouds, \
negative space on the left, no text, no logos" out/cover.png 1536x1024 high
"""
import base64
import json
import os
import ssl
import sys
import urllib.request


def die(msg: str, code: int = 1):
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(code)


def main():
    if len(sys.argv) < 3:
        die("usage: gen_image.py \"<prompt>\" <out.png> [WxH] [quality]")

    prompt = sys.argv[1]
    out = sys.argv[2]
    size = sys.argv[3] if len(sys.argv) > 3 else "1536x1024"
    quality = sys.argv[4] if len(sys.argv) > 4 else "high"

    base = os.environ.get("IMAGE_API_BASE", "").rstrip("/")
    key = os.environ.get("IMAGE_API_KEY", "")
    model = os.environ.get("IMAGE_MODEL", "gpt-image-2")
    if not base or not key:
        die("set IMAGE_API_BASE and IMAGE_API_KEY in your environment first (see README).")

    url = f"{base}/images/generations"
    body = json.dumps({
        "model": model, "prompt": prompt, "size": size, "quality": quality, "n": 1,
    }).encode()

    # TLS context: prefer certifi if present, allow opt-out via env.
    if os.environ.get("IMAGE_API_INSECURE") == "1":
        ctx = ssl._create_unverified_context()
    else:
        try:
            import certifi
            ctx = ssl.create_default_context(cafile=certifi.where())
        except Exception:
            ctx = ssl.create_default_context()

    req = urllib.request.Request(
        url, data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    try:
        resp = urllib.request.urlopen(req, timeout=240, context=ctx)
        data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        die(f"HTTP {e.code}: {e.read()[:400].decode('utf-8', 'ignore')}")
    except ssl.SSLCertVerificationError:
        die("TLS verify failed. `pip install certifi`, or set IMAGE_API_INSECURE=1 to bypass (dev only).")
    except Exception as e:  # noqa: BLE001
        die(f"request failed: {e}")

    item = (data.get("data") or [{}])[0]
    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)

    if item.get("b64_json"):
        raw = base64.b64decode(item["b64_json"])
        with open(out, "wb") as f:
            f.write(raw)
    elif item.get("url"):
        with urllib.request.urlopen(item["url"], timeout=120, context=ctx) as r, open(out, "wb") as f:
            f.write(r.read())
    else:
        die(f"no image in response: {str(data)[:300]}")

    print(f"saved {out}  ({size}, model={model})")


if __name__ == "__main__":
    main()
