---
name: slide-studio
description: Build beautiful, EDITABLE HTML slide decks — a single self-contained file (fixed 16:9, zero dependencies) whose generated output lets the user reorder / add / delete / duplicate slides, change font size, hierarchy level and line spacing, edit text in the browser, and OPTIONALLY drop in AI-generated backgrounds via their OWN image API. Use when the user wants to make or edit a presentation, slides, a deck or a talk; turn notes into slides; restyle or reorder a deck; or add generated background art. Builds on frontend-slides ideas plus a distilled set of AI-slide design rules.
---

# slide-studio

Generate ONE self-contained `.html` deck with a real in-browser editor baked in: reorder / add / delete
slides, a text format bar (font size · level · line spacing), inline editing, optional AI backgrounds, and
one-click export. Zero dependencies, fixed 16:9, works offline.

## Golden rules (read these first)

1. Obey [references/design-rules.md](references/design-rules.md) — design system first; text is always a
   layer over images; one shared style paragraph; compose around the words; readable + semantic; test the
   first image. Plus the fixed-stage invariants.
2. **Reuse the engine verbatim.** Copy the entire `<style>` and `<script>` from
   [assets/deck-template.html](assets/deck-template.html). You only author the `:root` theme and the
   `<section class="slide">…</section>` list. The editor/organizer/format-bar/export all come for free —
   do not reinvent or delete them. See [references/runtime-features.md](references/runtime-features.md).
3. **Images are opt-in.** Never generate images unless the user chose to configure an image API. The deck
   is first-class with CSS backgrounds. See [references/image-generation.md](references/image-generation.md).

## Phase 0 — Detect mode

- **New deck** → Phase 1.
- **Edit existing slide-studio deck** → read it, keep the user's content/order, change only what's asked
  (theme, a slide, images, animation). Preserve the engine. Re-verify fixed-stage fit after changes.
- **From notes / a doc / a transcript** → extract the real wording (don't over-summarize), then Phase 1.

## Phase 1 — Content & density (ask together, once)

Ask: purpose, rough length, is content ready, and **density** (speaker-led vs reading-first — this drives
type scale and words-per-slide). If the user has material, use their real words. Don't ask about editing;
it's always on.

## Phase 2 — Aesthetic

Commit to one cohesive system (see [references/aesthetics.md](references/aesthetics.md)); the Mono Editorial
default is a safe, premium start. For a bigger decision, show 2–3 single-slide previews ("show, don't tell")
and let the user pick before building the whole deck. Lock fonts + palette into `:root`.

## Phase 3 — Generate

1. Copy `assets/deck-template.html` to the output path (next to any `bg/` folder).
2. Edit only `:root` (theme/fonts) and the slide list. Pick slide types from
   [references/runtime-features.md](references/runtime-features.md): `cover`, `divider`, `.p.ink` quote,
   content (`.title` + `.points`), `mirror`, `closing`.
3. Apply the density choice; never let a slide overflow — split instead of shrinking.
4. Keep the FULL `<style>`/`<script>` engine intact.

## Phase 4 — Optional AI backgrounds (only if the user opted in)

1. Confirm the user wants AI images and has an OpenAI-compatible endpoint; collect Base URL + key + model.
   **Never hardcode or commit a key.**
2. Write ONE shared style paragraph. Generate the **cover first**, show it, get approval (design rule 6).
3. Generate the rest with the same style paragraph; save to a `bg/` folder beside the deck; wire each via a
   `.bg` layer + `dark` section class + scrim. Prefer `scripts/gen_image.py`; the deck's `G` panel is the
   in-browser alternative. If skipped, use CSS gradient backgrounds — equally valid.

## Phase 5 — Verify & deliver

1. Screenshot a few slides at 1280×720 (headless) and fix any overflow/overlap.
2. `open` the deck. Tell the user the shortcuts: `E` edit, `O` organizer (reorder/add/delete), `G` images,
   arrows/space to navigate, `?s=N` to deep-link, and the organizer's **⬇ Export HTML** to save changes.
3. Note how to retheme (`:root`) and that any `bg/` images must travel with the file.

## Supporting files

| File | Purpose |
|---|---|
| [references/design-rules.md](references/design-rules.md) | The design doctrine + fixed-stage invariants (read first) |
| [references/aesthetics.md](references/aesthetics.md) | Default theme, palettes, font pairings, how to re-skin |
| [references/runtime-features.md](references/runtime-features.md) | Slide types + every built-in editor/organizer feature |
| [references/image-generation.md](references/image-generation.md) | Opt-in AI image workflow + prompt recipe |
| [assets/deck-template.html](assets/deck-template.html) | The deck engine — copy wholesale, fill `:root` + slides |
| [scripts/gen_image.py](scripts/gen_image.py) | Optional image generator (reads env; no bundled key) |
