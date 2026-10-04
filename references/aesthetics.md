# Aesthetics & theming

The template ships one refined default theme and is built to be re-skinned from `:root` only.
Pick a committed aesthetic for the deck's topic — don't default to the same look every time.

## Default: Mono Editorial (black / white / grey)

Premium, minimal, high-contrast. Great for essays, talks, philosophy, research, brand manifestos.

```css
:root{
  --paper:#f4f3f0;  --panel:#fbfbfa;  --ink:#161618;
  --muted:#74747a;  --light:#a6a6a3;
  --line:rgba(22,22,24,.16);  --hl:rgba(22,22,24,.10);
  --f-head:'Noto Sans SC','Space Grotesk',sans-serif;   /* headings: sans */
  --f-body:'LXGW WenKai Screen','Noto Serif SC',serif;  /* body/quotes: 楷体, warm, not Song */
  --f-num:'Space Grotesk','Noto Sans SC',sans-serif;    /* numbers / labels */
}
```

Signatures: full-bleed `--ink` quote pages, giant hollow section numbers (`-webkit-text-stroke`),
hairline rules, a subtle grey highlight band for `mark`, generous whitespace, dark atmospheric
section dividers when images are on.

## Swapping themes

Change only `:root` to get a different system. Keep the structure. A few directions:

- **Warm editorial** — `--paper:#f6f1e7; --ink:#211d17; --accent:#c0552f` (rust). Fraunces/serif display.
- **Cool institutional** — `--paper:#f3f5f8; --ink:#10131a; --accent:#1e2bfa` (cobalt). Clean sans.
- **Nocturnal** — dark `--paper:#13141a; --ink:#f3f2ee` with a single luminous accent. Flip text defaults.

## Font pairing guidance

- Headings: a face with character. CN: 思源黑体/Noto Sans SC (700–900), or 得意黑/Smiley Sans if available.
  EN: Space Grotesk, Fraunces, Bricolage, Archivo. Avoid Inter/Roboto/Arial.
- Body / quotes: readable and warm. CN: **霞鹜文楷 (LXGW WenKai)** — a 楷体, loads from jsDelivr:
  `https://cdn.jsdelivr.net/npm/lxgw-wenkai-screen-webfont@1.7.0/style.css`. Avoid thin Song/宋体.
- Numbers / eyebrows: a tabular-ish sans (Space Grotesk) reads crisp on page numbers and section numerals.

## Color discipline

- One accent, used sparingly. Headlines stay near-black (or near-white on dark); the accent does the emphasis.
- On image slides, desaturate/scrim so the image never fights the text. A muted cinematic grade
  (`filter:saturate(.74) contrast(1.06) brightness(.9)`) keeps color *and* legibility.
- Backgrounds should create atmosphere (gradients, texture, image) rather than defaulting to flat fills.
