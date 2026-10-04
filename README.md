# slide-studio

Turn an AI-generated slide deck into something you can keep working on — edit text, change size · level · line-spacing, drag to reorder, add/delete slides, drop in art, export — all in the browser. **Generating it is the start, not the end.**

**English** ·  [中文](README.zh-CN.md)

---

## Why a "Studio"

Most "AI makes your slides" tools hand you a **dead file**: move one slide, change a font size, cut a line — and you're back re-prompting from scratch.

slide-studio fixes that. It still outputs a single, fixed-16:9, zero-dependency `.html` — but that file **carries its own editor in the browser**: double-click to retype, drag to reorder, no code. That's why it's a *studio*, not a generator — after the first pass the deck is still *live*, and you keep shaping it until it's right.

It's a superset of [Zara Zhang's frontend-slides](https://github.com/zarazhangrui/frontend-slides): everything that does, plus the editing layer.

## What it does

### 1. Generate (inherited from frontend-slides)

- From scratch, or turn notes / a doc / a transcript into a deck.
- Convert PowerPoint (`.pptx`) to web — text, images, order, and notes preserved.
- Pick a style by *seeing*, not describing: a few title-slide previews to choose from, backed by curated presets and a 34-template bold pack.
- Fixed 16:9, animated, deliberately not "AI-slop".

### 2. Edit — the part slide-studio adds

Open the generated `.html`; hover the top-left for buttons, or use the keys:

- **`E`** — click any text and retype, like editing a web page.
- Select text and a format bar appears: **font size, level (display / title / body / caption), line-height, bold, align**.
- **`O`** — the organizer: drag to reorder (or ↑ ↓), `＋` insert, `⧉` duplicate, `🗑` delete, click a title to jump.
- Hit **Export HTML** to bake the new order and every edit into a clean single file.

### 3. Art & export

- **`G`** — optional: paste your own image API (Base URL / key / model, stored only in your browser) to generate cinematic backgrounds for a slide. Skip it and CSS gradients look great. **No key ships with this repo.**
- Export a **PDF** (`scripts/export-pdf.sh`) or deploy a live **Vercel** URL (`scripts/deploy.sh`) that works on phones.

## How to use

```bash
# 1. install into your skills dir
cp -R slide-studio ~/.claude/skills/slide-studio
```

```text
# 2. generate — just ask:
Use slide-studio to make a deck about "…"

# 3. refine in the browser (open the generated .html)
E edit · O reorder · G art · arrows/space to flip · ?s=5 to open on slide 5

# 4. finish
"Export HTML" from the organizer; or run the PDF / Vercel scripts
```

## Keyboard

| Key | Action |
|---|---|
| `←` `→` / Space / scroll | Navigate |
| `E` | Edit text (then the format bar sets size / level / line-height) |
| `O` | Organizer: reorder · add · duplicate · delete · Export HTML |
| `G` | Image / API settings (optional) |
| `?s=5` | Open on slide 5 |

## Why the decks look good

The skill enforces a small set of rules (see [`references/design-rules.md`](references/design-rules.md)): lock a design system first; text always sits *over* images, never baked in; one shared "style paragraph" keeps every image coherent; compose around the empty space; test the first image before batching. Distilled from *Isa does AI*'s guide *"How to Vibe Code AI Slides"*.

## Credits & License

Superset of **frontend-slides** (MIT © 2025 Zara Zhang); its template pack and export scripts are vendored here — see [NOTICE.md](NOTICE.md). Design rules distilled from *Isa does AI* (independent re-implementation).

[MIT](LICENSE) © 2026 Ying-A1
