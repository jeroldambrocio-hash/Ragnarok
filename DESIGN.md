---
name: Ragnarok Forever
description: The eve of a War of Emperium, presented as a modern, quiet, premium game site.
colors:
  night: "#0b0c0f"
  night-raised: "#101217"
  graphite: "#161920"
  graphite-high: "#1d2029"
  hairline: "rgba(236, 231, 221, 0.1)"
  hairline-strong: "rgba(236, 231, 221, 0.2)"
  parchment: "#ece7dd"
  parchment-muted: "#b4afa5"
  parchment-faint: "#8a867e"
  emperium-gold: "#d4b06a"
  emperium-gold-hi: "#e8cc8f"
  gold-ink: "#17130a"
  banner-crimson: "#c23a45"
  online-green: "#6cc58a"
typography:
  display:
    fontFamily: "Faculty Glyphic, Iowan Old Style, Georgia, serif"
    fontSize: "clamp(3.4rem, 9vw, 6rem)"
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: "0.02em"
  numeral:
    fontFamily: "Faculty Glyphic, Iowan Old Style, Georgia, serif"
    fontSize: "clamp(5rem, 11vw, 7.5rem)"
    fontWeight: 400
    lineHeight: 0.85
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Faculty Glyphic, Iowan Old Style, Georgia, serif"
    fontSize: "clamp(2.1rem, 4.6vw, 3.5rem)"
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: "-0.01em"
  title:
    fontFamily: "Faculty Glyphic, Iowan Old Style, Georgia, serif"
    fontSize: "clamp(1.35rem, 2.2vw, 1.75rem)"
    fontWeight: 400
    lineHeight: 1.15
  subhead:
    fontFamily: "Onest, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 600
    lineHeight: 1.3
  body:
    fontFamily: "Onest, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.65
  counter:
    fontFamily: "Onest, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(2rem, 4vw, 2.75rem)"
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "-0.01em"
  button:
    fontFamily: "Onest, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "0.01em"
  label:
    fontFamily: "Onest, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0.12em"
rounded:
  sm: "6px"
  md: "8px"
  track: "10px"
  panel: "18px"
  pill: "999px"
spacing:
  gutter: "clamp(1.25rem, 5vw, 4.5rem)"
  max: "76rem"
  nav-h: "4rem"
  section: "clamp(5rem, 11vw, 9rem)"
  section-head: "clamp(2rem, 4vw, 3rem)"
  columns: "clamp(2rem, 5vw, 5rem)"
  row: "1rem"
components:
  button-primary:
    backgroundColor: "{colors.emperium-gold}"
    textColor: "{colors.gold-ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "0.7rem 1.15rem"
    height: "2.75rem"
  button-primary-hover:
    backgroundColor: "{colors.emperium-gold-hi}"
  button-primary-lg:
    padding: "0.9rem 1.6rem"
    height: "3.25rem"
  button-primary-disabled:
    backgroundColor: "{colors.graphite-high}"
    textColor: "{colors.parchment-muted}"
  button-secondary:
    backgroundColor: "rgba(11, 12, 15, 0.35)"
    textColor: "{colors.parchment}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "0.7rem 1.15rem"
    height: "2.75rem"
  button-ghost:
    textColor: "{colors.parchment-muted}"
    typography: "{typography.button}"
    padding: "0.7rem 0.5rem"
  input:
    backgroundColor: "{colors.night-raised}"
    textColor: "{colors.parchment}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "0.7rem 0.9rem"
    height: "3rem"
  input-focus:
    backgroundColor: "{colors.graphite}"
  tab-track:
    backgroundColor: "{colors.night-raised}"
    rounded: "{rounded.track}"
    padding: "0.25rem"
  tab-active:
    backgroundColor: "{colors.emperium-gold}"
    textColor: "{colors.gold-ink}"
    rounded: "7px"
    height: "2.5rem"
  segmented-checked:
    backgroundColor: "{colors.graphite-high}"
    textColor: "{colors.parchment}"
    rounded: "{rounded.sm}"
  sample-badge:
    textColor: "{colors.parchment-muted}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  guide-label:
    backgroundColor: "rgba(16, 18, 23, 0.82)"
    textColor: "{colors.parchment}"
    rounded: "{rounded.pill}"
    padding: "0.35rem 0.7rem"
  nav-link:
    textColor: "{colors.parchment-muted}"
    rounded: "{rounded.sm}"
    padding: "0.5rem 0.8rem"
---

# Design System: Ragnarok Forever

## Overview

**Creative North Star: "The Eve of the Siege"**

The site is a night hill facing a lit castle under siege. Everything else is quiet so that scene can speak: a near-black charcoal ground, graphite planes used sparingly, warm off-white text, and two disciplined accents. Emperium gold marks what the visitor should do or remember (the primary action, key numerals, focus, the selected tab). Banner crimson belongs to the war and to live state: the WoE band, its countdown rules, castle dividers, the offline dot, invalid fields. Nothing else is coloured.

Structure is carried by hairlines and space, not by boxes. Content lists are rows divided by 1px rules at 10% off-white; sections breathe on a large clamped rhythm; containers are rare and quiet. Display type is Faculty Glyphic, a slightly carved fantasy serif that says Ragnarok without costume; everything a player reads to act is set in Onest, modern and plain. The cinematic layer lives in pixel-art layers and a light ember canvas behind the hero, with subtle pointer and scroll parallax that never touches legibility, and a band of original pixel-art job characters (Novice, Swordman, Mage, Merchant) who act as the hero's navigation. The hero scene is original pixel art too: a moonlit siege of a red-roofed castle, built as parallax layers by `tools/scene.py`; the WoE section carries a floating pixel Emperium. No official art is used.

The system refuses the old private-server page (banners, bevelled buttons, dense tables of colour) and the generic dark gaming template (neon glows, glassy card grids, six feature tiles).

**Key Characteristics:**
- Dark only (`color-scheme: dark`); charcoal ground, graphite used for inputs, tab tracks and selected states.
- Gold is scarce and meaningful; crimson is reserved for war and live state.
- Hairline-ruled rows instead of cards; generous clamped section spacing.
- Faculty Glyphic for display and numerals, Onest for all functional text.
- Pixel art for every illustration (scene layers at 480x270, Emperium, job sprite sheets at 44x72 frames), always rendered with `image-rendering: pixelated`; a single-stroke SVG icon set for UI. No official or third-party art.
- Motion is small, eased (`cubic-bezier(0.16, 1, 0.3, 1)`), and fully disabled under reduced motion.
- Illustrative data is always marked with a dashed sample badge; unavailable actions render as disabled buttons that say why.

## Colors

A night palette of warm-neutral charcoals and parchment whites, lit by one gold and, only where war or live state is involved, one crimson.

### Primary
- **Emperium Gold** (`emperium-gold`): the filled primary button ("Jugar ahora", "Jugar", "Crear cuenta"), the brand diamond and "Forever" in the wordmark, hero "FOREVER", the rates numeral, the first-place rank, the active tab ink, nav underline, focus outlines, text caret and selection. **Emperium Gold High** (`emperium-gold-hi`) is its hover state only. **Gold Ink** (`gold-ink`) is the text colour on any gold fill.

### Secondary
- **Banner Crimson** (`banner-crimson`): the War of Emperium world. The WoE section's radial wash and 25% border, the 2px top rule over each countdown unit, castle realm dividers (35% alpha), the scene's banners and fire falloff, the offline status dot, and invalid input borders.

### Tertiary
- **Online Green** (`online-green`): the status dot when the server is up, with a 15% halo ring. Never used for anything else.

### Neutral
- **Night** (`night`): page ground, scrollbar track, opaque mobile menu.
- **Night Raised** (`night-raised`): input wells, tab track, segmented control, character label fill (82% alpha).
- **Graphite** (`graphite`): focused input background; start of the community panel gradient.
- **Graphite High** (`graphite-high`): checked segment, disabled primary button.
- **Hairline** (`hairline`) and **Hairline Strong** (`hairline-strong`): every divider, row rule and quiet border; the strong value for table heads, inputs and secondary button borders.
- **Parchment** (`parchment`): primary text and headings.
- **Parchment Muted** (`parchment-muted`): ledes, nav links, secondary values, ghost buttons.
- **Parchment Faint** (`parchment-faint`): hints, table column heads, captions, legal text, rank numbers below first.

### Named Rules
**The Gold Means Act Rule.** Gold fills only the primary action and the active tab. Elsewhere gold is a stroke, a numeral or a word, never a surface.

**The Crimson Is War Rule.** Crimson appears only in the WoE world and in live or error state. A crimson accent on a generic section is off-system.

## Typography

**Display Font:** Faculty Glyphic (with Iowan Old Style, Georgia, serif)
**Body Font:** Onest 400/500/600/700 (with system-ui, -apple-system, Segoe UI, sans-serif)

**Character:** A carved, faintly runic serif for names, places and big numbers, paired with a clean contemporary grotesque for everything the player reads to act. Display is always weight 400; emphasis comes from size and gold, never bold.

### Hierarchy
- **Display** (400, `clamp(3.4rem, 9vw, 6rem)`, 0.92, uppercase, +0.02em): the hero wordmark only, stacked on two lines with the second line in gold. The WoE section title uses the same voice at `clamp(2.6rem, 7vw, 5rem)`/0.95 uppercase.
- **Numeral** (400, `clamp(5rem, 11vw, 7.5rem)`, 0.85, -0.02em): the rates figure ("5x"), in gold.
- **Headline** (400, `clamp(2.1rem, 4.6vw, 3.5rem)`, 1.05, -0.01em): section titles. Closing sections scale it up (Download `clamp(2.4rem, 6vw, 4.25rem)`) or down (Community `clamp(2rem, 4.4vw, 3.25rem)`).
- **Title** (400, `clamp(1.35rem, 2.2vw, 1.75rem)`, 1.15): claim titles; smaller display moments (realm names 1.2rem, fact values 1.35rem, WoE quote up to 1.6rem in muted parchment).
- **Subhead** (Onest 600, 1.0625rem, 1.3): small block heads like "Estado en vivo", "Próxima WoE", "Castillos".
- **Body** (Onest 400, 1rem, 1.65): default text; ledes at 1.0625rem in muted parchment with `max-width` 32 to 38rem.
- **Counter** (Onest 500, `clamp(2rem, 4vw, 2.75rem)`, 1): countdown digits. Live stats use Onest 600 1.5rem with tabular numerals.
- **Button** (Onest 600, 0.9375rem, +0.01em; 1rem in the large size).
- **Label** (Onest 500 to 600, 0.75 to 0.8125rem, +0.06 to +0.14em, uppercase): hero meta line, character labels, table column heads, countdown units.

### Named Rules
**The Two Voices Rule.** Faculty Glyphic names and counts things; Onest instructs. Buttons, forms, tables and stats are never set in the display face.

**The Tabular Truth Rule.** Any changing number (players, uptime, levels, schedule times) uses `font-variant-numeric: tabular-nums`.

## Layout

A single centred column, `max-width: calc(76rem + gutter * 2)` with a fluid gutter (`clamp(1.25rem, 5vw, 4.5rem)`). A fixed 4rem nav sits on top; anchor scrolling is offset by nav height plus 1rem. Sections open with `clamp(5rem, 11vw, 9rem)` of space above and a headline block `clamp(2rem, 4vw, 3rem)` from content. Inside sections, content splits into two asymmetric columns (roughly 1.2fr / 1fr, or 0.9fr / 1.4fr in WoE) with `clamp(2rem, 5vw, 5rem)` gaps, and collapses to one column at 900px. Rows inside lists run 1rem vertical padding between hairlines.

The hero is full-bleed and at least `clamp(38rem, 100svh, 60rem)` tall: copy centre-left over a left-to-right shade, castle in the right third, four job characters standing on the foreground ridge in two bands either side of centre. In portrait or under 760px the castle takes the top band (about 52% height, masked out at the bottom), copy sits below it, the primary button goes full width, and the characters become a four-column dock with labels always visible. The nav collapses to a menu button at 860px; the mobile menu is an opaque drop panel of 1.0625rem links divided by hairlines.

Breakpoints in use: 560px (single-column forms and lists, full-width tabs), 760px (portrait hero, footer stack), 860px (nav), 900px (two-column sections collapse), 1100px (larger characters).

## Elevation & Depth

Flat and tonal. Depth comes from the night ground stepping to graphite, from hairlines, and from the hero's layered SVG with parallax; it does not come from shadows on surfaces. The one structural shadow is a soft warm under-glow beneath the gold primary button. The scrolled nav uses a translucent night fill with backdrop blur. Focus and state are drawn with rings and outlines, not lifts.

### Shadow Vocabulary
- **Gold under-glow** (`box-shadow: 0 8px 24px -10px rgba(212, 176, 106, 0.55)`; hover `0 10px 28px -10px rgba(232, 204, 143, 0.7)`): primary button only.
- **Focus well** (`box-shadow: 0 0 0 3px rgba(212, 176, 106, 0.18)`): focused input, with gold border.
- **Status halo** (`box-shadow: 0 0 0 4px rgba(108, 197, 138, 0.15)`, crimson equivalent when offline): the live status dot.

### Named Rules
**The Hairline Not Box Rule.** Separate content with 1px rules at `hairline` or `hairline-strong`. Reach for a filled container only for controls (inputs, tab track, segmented control) or one closing call to action.

**The Scene Carries Depth Rule.** Atmospheric gradients, glows, smoke and embers live in the authored scene and the WoE band. UI surfaces stay flat.

## Shapes

Gently rounded and consistent: 6px for small interactive targets (nav links, segments), 8px for buttons, inputs, the segmented control and confirmation notes, 10px for the tab track with 7px tab ink inside it, full pills for metadata badges and character labels, and 18px for the single community panel. Default focus outlines are 2px gold at a 3px offset with a 4px radius. Dividers are always 1px, except the 2px crimson rule over countdown units. Icons are an authored 24px-grid line set at 1.6 stroke with round caps and joins, sized 16 to 22px and coloured by `currentColor`. The brand mark is a nested diamond.

## Components

### Buttons
Calm, solid, and specific: one filled voice, one outlined, one textual.
- **Shape:** gently rounded (`rounded.md`), minimum 2.75rem tall (3.25rem large), optional 18px leading icon with a 0.55rem gap.
- **Primary:** gold fill with gold ink text and the gold under-glow. Use it for the main action in a viewport or block: "Jugar ahora" in the hero, "Jugar" in the nav, the form submit and the Download and Discord calls to action.
- **Secondary:** transparent night fill (35%) with a `hairline-strong` border; hover raises the border to 45% parchment and adds a 6% parchment wash.
- **Ghost:** muted text only, tight 0.5rem inline padding; hover returns to full parchment.
- **Hover / Active:** scale to 1.02 on hover and 0.98 on press, over `--fast` (160ms) with the house ease-out.
- **Pending (unavailable):** a real disabled button at 55% opacity (primary drops to graphite with muted text), with a 0.8125rem faint note beneath saying why. Never a fake working link.

### Chips (sample badge)
- **Style:** 1px dashed `hairline-strong` pill, muted text at 0.75rem/500 with +0.04em tracking. It marks any illustrative data ("Datos de ejemplo", "Horario de ejemplo") and sits beside the block head it qualifies.

### Cards / Containers
- Content is not carded. The only filled panel is the closing Community block: `rounded.panel`, a 135° graphite-to-night-raised wash, 1px hairline border, `clamp(2rem, 5vw, 3.5rem)` padding.

### Inputs / Fields
- **Style:** night-raised well, 1px `hairline-strong` border, `rounded.md`, 3rem minimum height, 1rem Onest text; labels sit above at 0.875rem/500 in muted parchment, hints below at 0.8125rem in faint parchment.
- **Hover:** border rises to 32% parchment.
- **Focus:** gold border, graphite fill, 3px gold focus well; the default outline is suppressed only here.
- **Error:** crimson border; form messages sit in a polite live region.
- **Segmented control:** a night-raised track with 0.25rem padding; the checked option fills graphite-high with full parchment text; focus shows a 2px gold outline.

### Navigation
- **Top bar:** fixed, transparent over the hero; after 24px of scroll it turns 78% night with a 14px blur and a hairline bottom. Wordmark in Faculty Glyphic 1.125rem with "Forever" in gold, behind the gold diamond mark.
- **Links:** Onest 500 0.875rem, +0.04em, muted; hover and the section in view (`aria-current`) turn full parchment and draw a 1px gold underline that scales in from the left over 220ms.
- **Actions:** a muted Discord text link with icon and a compact primary "Jugar" button (2.4rem).
- **Mobile:** below 860px a 2.75rem menu button opens an opaque night panel that slides 8px down and fades in; Escape closes it and returns focus.

### Tabs (Rankings)
- A night-raised track with a hairline border; the selected tab is shown by a gold ink slab that slides and resizes between tabs (260ms ease-out) under gold-ink text. Tables beneath use uppercase faint column heads over a strong hairline, 1rem row padding, a 3% parchment row hover, display-face rank numbers, and a larger gold first place.

### Job Guides (signature)
Four original pixel-art characters, one per first job (Novice → Servidor, Swordman → WoE, Mage → Rankings, Merchant → Descargar), are the hero's navigation. Sheets come from `tools/sprites.py`: 44x72 frames, columns idle / breath / wave / cheer, rows head front / left / right, with head and body as separate layers like the game. They idle on a two-frame breath with staggered delays. With a fine pointer their head turns toward the cursor (front, left or right); when the cursor rests they glance around on their own. On hover they hop, wave, and get a soft gold glow, and their pill label goes to full opacity. On click they cheer and leap, and the page scrolls to the section after 300ms. Labels carry a gold line icon and uppercase Onest. All idle and hover motion stops under reduced motion.

### Siege Scene (signature)
The hero background is layered pixel art from `tools/scene.py` (dithered night sky with moon and stars, moonlit far mountains, a stone castle with red cone roofs, banners, burning walls and gate, siege ladders and smoke, a near slope with a trebuchet and torch war-bands, and a tiled ground ridge with an amber rim) plus an ember canvas (16 particles on mobile, 34 on desktop). Layers parallax with the pointer and with scroll by depth. A night shade on the left (or bottom in portrait) protects the copy. The WoE section echoes it with a crimson-washed band and dark castle silhouettes at its base.

## Do's and Don'ts

### Do:
- **Do** keep gold to the primary action, the active tab, key numerals, the wordmark accent and focus.
- **Do** keep crimson to the WoE world, the offline state and invalid fields.
- **Do** divide lists and stats with 1px hairlines and let section spacing (`clamp(5rem, 11vw, 9rem)`) do the grouping.
- **Do** set names, titles and big numbers in Faculty Glyphic at weight 400, and every control, form, table and stat in Onest.
- **Do** mark illustrative data with the dashed sample badge, and render unavailable actions as disabled buttons with a note.
- **Do** draw icons from the single-stroke 24px set (1.6 stroke, round caps) and colour them with `currentColor`.
- **Do** ease all state changes with `cubic-bezier(0.16, 1, 0.3, 1)` at 160 to 260ms, and switch off animation under `prefers-reduced-motion`.

### Don't:
- **Don't** build grids of feature cards or glassy panels; content lives in ruled rows and columns.
- **Don't** add drop shadows to surfaces; the gold under-glow belongs to the primary button alone.
- **Don't** put gradients on controls or text; gradients belong to the scene, the WoE band and the one closing panel.
- **Don't** bold the display face or set body copy in it.
- **Don't** introduce another accent hue; new states reuse gold, crimson or green by meaning.
