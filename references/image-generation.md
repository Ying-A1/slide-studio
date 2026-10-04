# Optional AI background images

**Principle: opt-in only.** The skill must never generate images unless the user has explicitly chosen
to configure an image API. A deck is fully first-class with pure-CSS backgrounds (gradients, solid,
subtle texture). Only offer AI images, and only generate them, after the user says yes and provides an
endpoint. **Never hardcode or commit an API key.**

## What the agent should do

1. Ask: *"Do you want AI-generated backgrounds? They need your own image API (OpenAI-compatible). You can
   also skip this — the deck looks great without them."*
2. If **no** → use CSS backgrounds (the template's `.bg` works with a `background:` gradient too). Done.
3. If **yes** → ask for: **Base URL** (e.g. `https://.../v1`), **API key**, **model** (default `gpt-image-2`).
   Then generate the **cover first**, show it, and only continue once the look is approved (rule 6).

## Config (two interchangeable ways)

Both read the *same* three values. Keys live only in the environment or the user's browser — never in the repo.

**Script / CLI:**

```bash
export IMAGE_API_BASE="https://your-endpoint/v1"
export IMAGE_API_KEY="sk-..."
export IMAGE_MODEL="gpt-image-2"      # optional, this is the default
python scripts/gen_image.py "SCENE ... STYLE PARAGRAPH" out/cover.png [WIDTHxHEIGHT] [quality]
```

**In the generated deck:** press `G` (or the ⚙ button) → paste Base URL + key + model → stored in
`localStorage` only → write a scene → "generate for this slide". If the browser call is blocked by CORS
(common with corporate proxies), fall back to the script with the same values.

## Prompt recipe (always)

`<SCENE, specific, with the composition moves> + <SHARED STYLE PARAGRAPH>`

- Scene names the empty side, pushes the subject opposite, keeps key elements in the middle two-thirds.
- Style paragraph fixes lighting/materials/palette/mood and repeats: *no text, no numbers, no logos, no
  lettering, no watermark.*
- Keep ONE style paragraph for the whole deck and append it to every prompt verbatim.

Example style paragraph (swap to taste):

> Painterly semi-realistic fantasy key-art, luminous atmospheric lighting, epic cinematic vista, volumetric
> god-rays, rich yet slightly muted cinematic color grade, highly detailed. Key elements within the middle
> two-thirds. No text, no words, no letters, no numbers, no logos, no watermark, no UI.

## Model notes (OpenAI-compatible `images/generations`)

- `gpt-image-2` returns `data[0].b64_json` (a PNG). Decode and save, or inline as a `data:` URI.
- Useful sizes: `1536x1024` (≈3:2, good for 16:9 crop), `1024x1024`, `1024x1536`. `quality`: `high` for finals.
- A deck background only needs ~1.5 MP; the fixed stage upscales fine under a scrim.

## Putting the image on a slide

The template's background layer:

```html
<section class="slide cover dark">
  <div class="bg" style="background-image:url('bg/cover.png')"></div>
  <div class="frame"> ... text ... </div>
</section>
```

- `.bg` sits at `z-index:0`; the `.frame` (text) sits above it. A left-to-transparent scrim keeps text legible.
- Add `dark` to the `<section>` so headings/body flip to light.
- Images live in a `bg/` folder **next to the deck**; keep them together when moving/exporting the file.
- `.bg` also accepts a CSS gradient instead of an image — the no-API path uses this.
