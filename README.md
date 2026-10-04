# slide-studio

> Build beautiful, **editable**, animation-rich HTML slide decks by talking to an AI — then reorder, restyle, and (optionally) drop in AI-generated backgrounds, all in the browser.

`slide-studio` is a [Claude Code / Agent **Skill**](https://docs.claude.com/en/docs/claude-code/skills). It teaches the agent to generate a single self-contained `.html` deck (fixed 16:9, zero dependencies) that ships with a real in-browser editor:

- ✍️ **Edit text in place** — click any text, type.
- 🔤 **Change font size, hierarchy level, and line spacing** — a floating format bar, no code.
- ↕️ **Reorder / add / delete / duplicate slides** — a drag-and-drop organizer. *(The thing plain HTML decks never let you do.)*
- 🖼️ **Optional AI backgrounds** — generate cinematic backgrounds with your **own** image API. Entirely opt-in; the deck looks great with pure-CSS backgrounds if you never configure one.
- 🎬 **Motion** — staggered entrances + slow Ken-Burns on image slides.
- ⬇️ **Export** a clean standalone `.html` with your new order/edits baked in.

It is built on top of the ideas in Anthropic's `frontend-slides` skill, plus a set of **slide-design rules** distilled from the YouTube guide *"How to Vibe Code AI Slides"* by **Isa does AI**.

## Install

Copy the folder into your skills directory:

```bash
# Claude Code (user-level skills)
cp -R slide-studio ~/.claude/skills/slide-studio
```

Then just ask: *"Use slide-studio to make a deck about …"*.

## The design rules (why the decks look good)

These are enforced by the skill and documented in [`references/design-rules.md`](references/design-rules.md):

1. **Lock a design system first** — one base color, one text color, one accent used sparingly; a display font + a body font. Decide it before making a single slide.
2. **Never bake text into background images** — all words/numbers/charts are a layer on top. Images carry no logos or lettering (generated text warps).
3. **One shared "style paragraph"** appended to every image prompt → every image looks like the same art direction.
4. **Compose around the words** — name the empty side, push the subject to the opposite side, make the empty space meaningful (light/shadow), keep key elements in the middle two-thirds (edges get cropped on phones/PDF).
5. **Bright, legible, semantic** — readable backgrounds, charts in their own panels, colors that mean something.
6. **Test the first image before batching** — don't burn API credits on an unproven look.

## Optional: AI background images (opt-in)

The skill **never** generates images unless *you* choose to configure an image API. Two ways:

- **In the browser** — open the deck, press **`G`** (or the ⚙ button), paste your OpenAI-compatible **Base URL + API key + model**, write a scene, generate. Config is stored only in your browser's `localStorage`.
- **Via script** — set env vars and run [`scripts/gen_image.py`](scripts/gen_image.py).

```bash
export IMAGE_API_BASE="https://your-endpoint/v1"
export IMAGE_API_KEY="sk-..."          # your key, never committed
export IMAGE_MODEL="gpt-image-2"
python scripts/gen_image.py "a vast floating celestial city above a sea of clouds" out/cover.png
```

No key ships with this repo. See [`references/image-generation.md`](references/image-generation.md).

## Keyboard shortcuts (in a generated deck)

| Key | Action |
|---|---|
| `←` `→` / `Space` | Prev / next slide |
| `E` | Toggle edit mode |
| `O` | Toggle slide organizer (reorder / add / delete) |
| `G` | Toggle image / API settings |
| `?s=5` (URL) | Jump straight to slide 5 |

## Credits

- Design-thinking workflow inspired by Anthropic's **frontend-slides** skill.
- Slide-design rules distilled from **"How to Vibe Code AI Slides (Beginner Friendly)"** by *Isa does AI* (YouTube). This project is an independent re-implementation of the *ideas*, not affiliated with that creator or Higgsfield.

## License

[MIT](LICENSE) © 2026 Ying-A1
