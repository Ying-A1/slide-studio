# Slide design rules

The rules the skill must follow when generating or editing a deck. Most are distilled from the
"vibe code AI slides" workflow; the rest are fixed-stage invariants.

## 1. Lock the design system *before* making slides

Decide, and write into `:root`, before the first slide:

- **One base/canvas color**, **one text color**, **one accent** used sparingly (ideally once per slide).
- **A display font + a body font.** Avoid generic defaults (Inter/Roboto/Arial/system). For Chinese,
  pair a strong sans for headings (e.g. 思源黑体 / Noto Sans SC heavy) with a *non-thin, non-Song* body
  face — 霞鹜文楷 (LXGW WenKai, a 楷体) reads warm and premium. Never use the thinnest Song weights.
- Keep it cohesive. Dominant color + sharp accent beats a timid, evenly-spread palette.

This single decision is what keeps 15 slides looking like one deck instead of three.

## 2. Text is always a layer *on top* of imagery

- **Never bake words, numbers, or charts into a background image.** Generated text warps and can't be fixed.
- Backgrounds carry **no logos, no lettering, no signage** on surfaces.
- Charts/tables are HTML on top of (or beside) the image, never painted into it. Keep every number in
  one editable place so fixing a figure never means regenerating art.

## 3. One shared "style paragraph" for every image

Write a single paragraph describing lighting, materials, palette, mood, and the two rules above, then
**append it verbatim to every image prompt.** Scene first, style paragraph last. This is what makes a
set of images feel shot by the same person on the same day.

## 4. Compose each frame around the words that don't exist yet

Four moves in every image prompt:

1. **Name the empty side** — e.g. "leave generous negative space on the LEFT". Models center everything otherwise.
2. **Push the subject to the opposite side**, into the area the text won't cover.
3. **Make the empty space mean something** — soft light, a shadow, a wall in gentle focus. A flat blank patch looks like a mistake; a lit one looks intentional.
4. **Keep key elements in the middle two-thirds** — phone and PDF crops eat the edges.

## 5. Readable + semantic beats decorative

- A bright, legible background reads better than a busy dark one — especially for small text / thin lines on a phone.
- Put charts in their own clean panel over the image, not loose on the photo where labels get lost.
- Give colors meaning (one hue per category) so a chart can read with few or no labels.
- Match motion/scroll direction to the content.

## 6. Test the first image before batching

Generate one image, confirm the look and composition, *then* generate the rest. Don't burn API credits
on an unproven style. (The skill surfaces the first image to the user before continuing.)

---

## Content density (ask once)

Ask whether this is a **speaker-led** deck or a **reading-first** deck, then commit:

| Mode | Best for | Behavior |
|---|---|---|
| Low density / speaker-led | talks, keynotes, live sharing | one idea per slide, big type, 1–3 bullets, more slides |
| High density / reading-first | reports, handouts, async review | self-contained slides, grids/tables, 4–8 bullets when readable |

Never shrink text until it's cramped. If content overflows the mode, **split into more slides**.

## How much goes on one page

- A section slide = a number + a title + one line.
- A content slide = an eyebrow + one headline + 3–5 short bullets (speaker) or a tight grid (reading).
- A quote slide = one quote + attribution. Let it breathe.
- Prefer the user's / source's **real words** over your paraphrase. Don't over-summarize.

## Fixed 16:9 stage (non-negotiable)

- Author every slide inside a fixed **1920×1080** stage; scale the whole stage to the viewport.
- Stay 16:9 on every screen (letterbox/pillarbox); never reflow slide content for phones.
- Switch slides with `.active` / `.visible` (visibility/opacity), never `display:none`.
- Include `prefers-reduced-motion` support. Verify no overflow / overlap in a real screenshot at 1280×720.
