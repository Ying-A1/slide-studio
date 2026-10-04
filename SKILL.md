---
name: slide-studio
description: Build beautiful, EDITABLE HTML slide decks — a single self-contained file (fixed 16:9, zero dependencies) whose output lets the user reorder / add / delete / duplicate slides, change font size · hierarchy level · line spacing, edit text in the browser, and OPTIONALLY add AI-generated backgrounds via their OWN image API. Also converts PowerPoint (.pptx) to web, offers "show, don't tell" style discovery (curated presets + a 34-item bold template pack), and exports to PDF or a live Vercel URL. Use whenever the user wants to make, edit, restyle, reorder, or convert a presentation / slides / deck / talk. A superset of the frontend-slides skill plus in-browser editing and opt-in AI art.
---

# slide-studio

Generate ONE self-contained `.html` deck with a real in-browser editor baked in — reorder / add / delete
slides, a text format bar (**font size · level · line spacing**), inline editing, optional AI backgrounds,
and one-click export. Zero dependencies, fixed 16:9, offline-capable. It does everything the
`frontend-slides` skill does (style discovery, PPTX conversion, PDF/Vercel export) **and** adds the editing
layer that plain HTML decks never had.

## Golden rules (read first)

1. Obey [references/design-rules.md](references/design-rules.md): design system first; text is always a
   layer over images; one shared style paragraph; compose around the words; readable + semantic; test the
   first image; and the fixed-stage invariants (1920×1080, scale whole stage, never reflow, `.active`/`.visible`).
2. **Reuse the engine verbatim.** Copy the entire `<style>` + `<script>` from
   [assets/deck-template.html](assets/deck-template.html). You author only the `:root` theme and the
   `<section class="slide">…</section>` list — the editor / organizer / format-bar / export come for free
   ([references/runtime-features.md](references/runtime-features.md)). Don't delete or reinvent them.
3. **Images are opt-in.** Never generate images unless the user chose to configure an image API; a deck is
   first-class with CSS backgrounds ([references/image-generation.md](references/image-generation.md)).
4. **No AI slop.** Distinctive typography and a committed palette; verify a real screenshot before delivery.

## Phase 0 — Detect mode

- **New deck** → Phase 1.
- **PPTX conversion** (`.pptx` given) → Phase 4.
- **Enhance an existing slide-studio deck** → read it, keep the user's content & order, change only what's
  asked, preserve the engine, re-verify fixed-stage fit. When adding content, count elements first and split
  a slide rather than overflow it.
- **From notes / a doc / a transcript** → extract the real wording (don't over-summarize), then Phase 1.
## Phase 1 — Content & density (ask together, once)

Ask: **purpose**, rough **length**, is **content** ready, and **density** (speaker-led vs reading-first —
drives type scale and words-per-slide; see the table in design-rules). Use the user's real words. If the
user provides images, scan & inspect each (usable? what it shows, dominant colors) and co-design the outline
around text **and** images from the start. Don't ask about editing — it's always on.

## Phase 2 — Style discovery ("show, don't tell")

Most people can't name a style; show it. Generate **3 distinct single-slide previews** and let the user pick:

- **1 safe preset** from [references/STYLE_PRESETS.md](references/STYLE_PRESETS.md),
- **≥1 bold template** from [bold-template-pack/selection-index.json](bold-template-pack/selection-index.json)
  (read the compact index; shortlist by `mood`/`tone`/`best_for`/`formality`/`density`/`scheme`; read only the
  shortlisted `preview.md`; read a template's full `design.md` **only after** it's chosen),
- **1 wildcard** (a second bold template or a self-authored custom direction).

The slide-studio default aesthetic (Mono Editorial, [references/aesthetics.md](references/aesthetics.md)) is a
strong safe option. Preview authenticity: every preview must look like a real first slide — never render
"preview / option A / template name / audience notes" on the slide. Save previews under
`.slide-studio/previews/` and open them. If the user already named a direction, honor it and build fewer previews.

## Phase 3 — Generate

1. Copy `assets/deck-template.html` to the output path (beside any `bg/` folder).
2. Edit only `:root` (theme/fonts from the chosen style) and the slide list. Slide types
   ([references/runtime-features.md](references/runtime-features.md)): `cover`, `divider`, `.p.ink` quote,
   content (`.title` + `.points`), `mirror`, `closing`. Pull animation ideas from
   [references/animation-patterns.md](references/animation-patterns.md).
3. If a bold template was chosen, treat its `design.md` as the recipe (fonts, palette, decorative vocabulary,
   spacing) and translate any viewport-fluid values into fixed 1920×1080 stage coordinates. Keep it a single
   self-contained file; keep the full engine `<style>`/`<script>`.
4. Apply the density choice; never let a slide overflow — split instead of shrinking.
5. Verify: screenshot a few slides headless at 1280×720; fix any overflow/overlap.

## Phase 4 — PPTX conversion

1. `python scripts/extract-pptx.py <input.pptx> <output_dir>` (install `python-pptx` if needed).
2. Confirm extracted titles / content / image counts with the user.
3. Go to Phase 2 for style, then Phase 3 — preserve all text, images (from `assets/`), slide order, and
   speaker notes (as HTML comments).
## Phase 5 — Optional AI backgrounds (only if the user opts in)

1. Ask if they want AI backgrounds; they need an OpenAI-compatible endpoint. If no → use CSS gradients
   (first-class). If yes → collect **Base URL + key + model**. **Never hardcode or commit a key.**
2. Write ONE shared style paragraph. Generate the **cover first**, show it, get approval (design rule 6),
   then the rest with the same paragraph. Save to a `bg/` folder beside the deck; wire via a `.bg` layer +
   `dark` section class + scrim. Prefer `scripts/gen_image.py`; the deck's `G` panel is the in-browser way.
   See [references/image-generation.md](references/image-generation.md).

## Phase 6 — Deliver, then share/export

1. `open` the deck. Tell the user the shortcuts: `E` edit · `O` organizer (reorder / add / delete / duplicate)
   · `G` images · arrows/space/scroll to navigate · `?s=N` to deep-link · the organizer's **⬇ Export HTML** to
   save a clean copy with the new order/edits baked in. Note how to retheme (`:root`) and that `bg/` images
   must travel with the file.
2. Offer sharing (optional):
   - **Live URL** — `bash scripts/deploy.sh <path>` (Vercel; works on phones). Bundle `bg/` with the deck.
   - **PDF** — `bash scripts/export-pdf.sh <path.html> [out.pdf]` (headless screenshots; static). Add
     `--compact` if the PDF > 10 MB. Also: the deck has `@media print`, so browser "Print → Save as PDF" works too.

## Supporting files

| File | Purpose | When |
|---|---|---|
| [references/design-rules.md](references/design-rules.md) | Design doctrine + fixed-stage invariants | first |
| [references/aesthetics.md](references/aesthetics.md) | Default theme, palettes, font pairings, re-skin | style |
| [references/runtime-features.md](references/runtime-features.md) | Slide types + every built-in editor feature | generate |
| [references/STYLE_PRESETS.md](references/STYLE_PRESETS.md) | Curated visual presets | style previews |
| [bold-template-pack/selection-index.json](bold-template-pack/selection-index.json) | 34 bold templates (progressive) | style previews |
| [references/animation-patterns.md](references/animation-patterns.md) | CSS/JS animation snippets | generate |
| [assets/deck-template.html](assets/deck-template.html) | The engine — copy wholesale, fill `:root` + slides | generate |
| [assets/viewport-base.css](assets/viewport-base.css) | Canonical fixed-stage CSS (already inside the template) | reference |
| [scripts/gen_image.py](scripts/gen_image.py) | Optional AI image generator (reads env; no bundled key) | Phase 5 |
| [scripts/extract-pptx.py](scripts/extract-pptx.py) | PPTX content extraction | Phase 4 |
| [scripts/export-pdf.sh](scripts/export-pdf.sh) · [scripts/deploy.sh](scripts/deploy.sh) | PDF export · Vercel deploy | Phase 6 |

Credits & licensing: this skill is a superset of **frontend-slides** (MIT © 2025 Zara Zhang) and vendors some
of its files; the slide-design doctrine is distilled from *"How to Vibe Code AI Slides"* by *Isa does AI*.
See [NOTICE.md](NOTICE.md).
