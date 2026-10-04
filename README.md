# slide-studio

> Build beautiful, **editable** slide decks by talking to an AI — then reorder, restyle, change type, and (optionally) drop in AI-generated backgrounds, all in the browser.

**English** · [中文说明](README.zh-CN.md)

`slide-studio` is a [Claude Code / Agent **Skill**](https://docs.claude.com/en/docs/claude-code/skills).
It generates a single self-contained `.html` deck (fixed 16:9, zero dependencies) that ships with a real
in-browser editor. It is a **superset of** Anthropic/Zara Zhang's [`frontend-slides`](https://github.com/zarazhangrui/frontend-slides)
skill — everything that does, plus the editing layer plain HTML decks never had — with slide-design rules
distilled from the YouTube guide *"How to Vibe Code AI Slides"* by **Isa does AI**.

## Features

Everything `frontend-slides` has:

- 🧱 **Zero dependencies** — one HTML file, inline CSS/JS, no build step.
- 🎨 **"Show, don't tell" style discovery** — pick from generated visual previews; curated
  [presets](references/STYLE_PRESETS.md) + a **34-template** [bold pack](bold-template-pack/).
- 📥 **PowerPoint → web** — convert `.pptx`, preserving text, images, order, and notes.
- 🖨️ **Export** — PDF (`scripts/export-pdf.sh`) or a live **Vercel** URL (`scripts/deploy.sh`).
- 🖼️ **Fixed 16:9**, animation-rich, accessible, anti-"AI-slop".

Plus what slide-studio adds:

- ✍️ **Edit text in place** — click any text, type.
- 🔤 **Change font size, hierarchy level, and line spacing** — a floating format bar, no code.
- ↕️ **Reorder / add / delete / duplicate slides** — a drag-and-drop organizer. *(The thing plain decks lack.)*
- 🤖 **Optional AI backgrounds** — generate cinematic art with your **own** image API. Fully opt-in; CSS
  gradients look great if you never configure one. No key ships with this repo.
- 🎬 **Motion** — staggered entrances + a slow Ken-Burns on image slides.
- ⬇️ **Export a clean standalone `.html`** with your new order/edits/type baked in.

## Install

```bash
cp -R slide-studio ~/.claude/skills/slide-studio
```

Then ask: *"Use slide-studio to make a deck about …"*.

## The design rules (why decks look good)

Enforced by the skill, documented in [`references/design-rules.md`](references/design-rules.md):

1. **Lock a design system first** — one base color, one text color, one accent; a display + a body font.
2. **Never bake text into images** — words/numbers/charts are a layer on top; images carry no logos/lettering.
3. **One shared "style paragraph"** appended to every image prompt → one coherent art direction.
4. **Compose around the words** — name the empty side, push the subject opposite, keep key elements in the
   middle two-thirds (edges crop on phones/PDF).
5. **Bright, legible, semantic** — readable backgrounds, charts in their own panels, colors that mean something.
6. **Test the first image before batching.**

## Optional: AI background images (opt-in)

The skill **never** generates images unless *you* configure an image API. Two ways:

- **In the browser** — press **`G`** in a deck, paste your OpenAI-compatible **Base URL + key + model**,
  write a scene, generate. Stored only in your browser's `localStorage`.
- **Via script**:

```bash
export IMAGE_API_BASE="https://your-endpoint/v1"
export IMAGE_API_KEY="sk-..."        # your key — never committed
export IMAGE_MODEL="gpt-image-2"
python scripts/gen_image.py "a vast floating city above a sea of clouds, space on the left, no text" out/cover.png
```

See [`references/image-generation.md`](references/image-generation.md).

## Keyboard shortcuts (in a generated deck)

| Key | Action |
|---|---|
| `←` `→` / `Space` / scroll | Navigate |
| `E` | Edit mode (then the format bar sets size / level / line-height) |
| `O` | Organizer — reorder (drag or ↑↓), add, duplicate, delete, **Export HTML** |
| `G` | Image / API settings (opt-in) |
| `?s=5` | Open on slide 5 |

## Credits & License

- Superset of **frontend-slides** (MIT © 2025 Zara Zhang); some files are vendored — see [NOTICE.md](NOTICE.md).
- Design rules distilled from **"How to Vibe Code AI Slides (Beginner Friendly)"** by *Isa does AI* (independent
  re-implementation; not affiliated).

[MIT](LICENSE) © 2026 Ying-A1
