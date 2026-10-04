# Runtime features (what the template already gives you)

`assets/deck-template.html` is a self-contained deck engine. When you generate a deck, you copy this
file's `<style>` + `<script>` wholesale and only replace the slide markup. Do **not** reinvent these.

## Slide types (classes)

Every slide is `<section class="slide ..."><div class="frame"> … </div></section>`.

| Class on `.slide` | Use |
|---|---|
| `cover` | title slide (big `.display`) |
| `divider` | section break: giant hollow `.dnum` + `.dtitle` + `.dtag` |
| `closing` | final statement (`.big`) |
| *(none)* + `.p.ink` | full-bleed dark quote page |
| *(none)* | content: eyebrow row + `.title` + `.points` |
| `dark` | flip text to light (use when the slide has a dark `.bg`) |

Content building blocks inside `.p`: `.kicker` (eyebrow), `.tag` (pill), `.title`/`.title.sm`,
`.lead`, `.subline`, `.points`(`.tight`/`.dot`) with `<li>`, `blockquote`(`.sm`), `.qbadge`, `.cite`,
`.mirror`>`.col`, `mark`/`.em` for emphasis. A `.bg` div (first child of the section) is the image/gradient layer.

## Interactive runtime (all built-in)

- **Edit text** — press `E` or hover the top-left corner. Click any text block and type. Changes are inline.
- **Format bar** (appears in edit mode when a text block is focused): **字号 A− / A+**, **行距 − / +**,
  **层级** (大标题 / 标题 / 正文 / 小字 presets), **B** (bold), **align** left/center. Operates on the focused
  block and writes inline styles, so edits survive export.
- **Organizer** — press `O` or the ☰ button. A side panel lists every slide; **drag to reorder** (or ↑ ↓),
  **＋** insert after, **⧉** duplicate, **🗑** delete, click a row to jump. This is the reordering plain
  HTML decks lack.
- **Image / API settings** — press `G` or the ⚙ button. Opt-in panel to (a) store an OpenAI-compatible
  Base URL + key + model in `localStorage`, (b) set a shared style paragraph, (c) generate a background for
  the current slide, or (d) paste a background image URL / pick a CSS gradient. Nothing here runs unless the
  user opens it. See `references/image-generation.md`.
- **Export** — the organizer's **⬇ Export HTML** downloads a clean standalone copy with the current order,
  edits, font/level/line-height changes, and backgrounds baked in (transient UI/edit state stripped).
- **Navigate** — `←` `→` / `Space` / scroll / swipe. `Home`/`End`. `?s=N` in the URL opens on slide N.
- **Motion** — staggered entrance (`.an`, `.pop`, per-bullet stagger) and a slow Ken-Burns zoom on any
  slide that has a `.bg` image. Respects `prefers-reduced-motion`.

## Rules when filling the template

1. Keep the full `<style>` and `<script>` from the template unchanged (they power all the above).
2. Only author the `<section class="slide">…</section>` list and the `:root` theme.
3. Respect the fixed-stage limits (`references/design-rules.md`): no overflow, split instead of shrinking.
4. If a slide has a dark `.bg`, add `dark` to the section so text flips light; keep a left scrim for legibility.
5. Verify a 1280×720 screenshot of a few slides before delivering.
