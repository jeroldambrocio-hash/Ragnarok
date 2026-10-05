---
name: Ragnarok Forever
description: Prontera's south plaza at evening, drawn in the 2002 Ragnarok Online client's interface language.
colors:
  stone: "#a3a8b5"
  stone-seam: "#939aa9"
  ink: "#1b2134"
  ink-soft: "#3c4560"
  paper: "#ffffff"
  win-frame: "#44538a"
  bar-top: "#dde3fb"
  bar-bottom: "#b3c0ee"
  field-wash: "#f4f6fd"
  field-edge: "#9aa5cc"
  hairline: "#c3cae6"
  npc-blue: "#2440c4"
  vend-pink: "#c42a62"
  vend-pink-deep: "#8e1743"
  vend-soft: "#fde4ee"
  chat-night: "rgba(18, 22, 38, .82)"
  chat-green: "#8ff08a"
  system-gold: "#ffd36b"
  button-face: "#e6eaf7"
  button-edge: "#6b78a8"
typography:
  display:
    fontFamily: "DotGothic16, MS Gothic, monospace"
    fontSize: "clamp(3.25rem, 8.4vw, 6rem)"
    fontWeight: 400
    lineHeight: 0.98
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "DotGothic16, MS Gothic, monospace"
    fontSize: "clamp(1.75rem, 4vw, 2.75rem)"
    fontWeight: 400
    lineHeight: 1.1
  numeral:
    fontFamily: "DotGothic16, MS Gothic, monospace"
    fontSize: "clamp(2.25rem, 5vw, 3.25rem)"
    fontWeight: 400
    lineHeight: 1
    fontFeature: "tnum"
  title:
    fontFamily: "DotGothic16, MS Gothic, monospace"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: "0.02em"
  ui:
    fontFamily: "DotGothic16, MS Gothic, monospace"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.2
  body:
    fontFamily: "Nanum Gothic, Apple SD Gothic Neo, Malgun Gothic, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Nanum Gothic, Apple SD Gothic Neo, Malgun Gothic, system-ui, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 700
    lineHeight: 1.2
rounded:
  chip: "2px"
  control: "3px"
  window: "4px"
  primary: "5px"
spacing:
  field: "0.7rem"
  window-pad: "1.25rem"
  gap: "clamp(1rem, 2.5vw, 2rem)"
  gutter: "clamp(1rem, 4vw, 4rem)"
  section: "clamp(3.5rem, 8vw, 6rem)"
components:
  window:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.window}"
  window-titlebar:
    backgroundColor: "{colors.bar-bottom}"
    textColor: "{colors.ink}"
    typography: "{typography.title}"
    padding: "0.3rem 0.7rem 0.25rem"
  button-primary:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.npc-blue}"
    typography: "{typography.ui}"
    rounded: "{rounded.primary}"
    padding: "0.55rem 1.1rem"
  button-primary-hover:
    backgroundColor: "{colors.npc-blue}"
    textColor: "{colors.paper}"
  button-primary-big:
    padding: "0.8rem 1.6rem"
  button:
    backgroundColor: "{colors.button-face}"
    textColor: "{colors.ink}"
    typography: "{typography.ui}"
    rounded: "{rounded.control}"
    padding: "0.55rem 1.1rem"
  button-hover:
    backgroundColor: "{colors.bar-top}"
  signboard:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "0.3rem 0.6rem 0.3rem 0.45rem"
  signboard-hover:
    backgroundColor: "{colors.vend-soft}"
  signboard-pink:
    backgroundColor: "{colors.vend-pink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.control}"
  input:
    backgroundColor: "{colors.field-wash}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.control}"
    padding: "0.5rem 0.6rem"
  input-invalid:
    backgroundColor: "{colors.vend-soft}"
  chip:
    backgroundColor: "{colors.vend-pink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.chip}"
    padding: "0.1rem 0.45rem"
  chat-box:
    backgroundColor: "{colors.chat-night}"
    textColor: "{colors.paper}"
    rounded: "{rounded.window}"
    padding: "1rem 1.25rem"
---

# Design System: Ragnarok Forever

## Overview

**Creative North Star: "The Prontera Evening Plaza"**

The page is a place, not a brochure: a cool grey isometric cobble plaza with evening light falling over its far side, and on top of it the 2002 client's own interface. Facts float above the stones as merchant vending signboards; the visitor signs up by talking to a Kafra NPC in a client dialog window; the guide reads as lines in the chat box. Every piece of chrome is something a classic player has already clicked a thousand times.

Density is low and scattered on the first viewport (signs at varied heights over open stone) and orderly below it, where content sits in client windows that alternate left and right down the plaza. The material is flat and small-scale: white windows, hairline navy frames, a pale periwinkle gradient title bar, small rounded grey-blue buttons. Depth comes from the ground, the light and the overlap of windows on stone, never from drop shadows on the UI.

The world refuses the private-server default: no dark epic hero, no gold serif, no giant character render, no row of rate cards.

**Key Characteristics:**
- Authored isometric cobble tile as the only background, under an evening gradient on the first viewport.
- White client windows with a 1px navy frame and a periwinkle gradient title bar.
- Pixel face (DotGothic16) for every in-game voice; Nanum Gothic for running text.
- Three game accents with fixed jobs: NPC blue, vending pink, chat green.
- Outlined white name tags as headings.
- Idle bob on floating signboards; NPC text types out once.

## Colors

A cool, low-chroma stone-and-paper base carrying three saturated accents borrowed directly from the client's own colour coding.

### Primary
- **NPC Name Blue** (npc-blue): NPC names, the primary action ("Crear cuenta", "Descargar cliente"), rate and class names, links, focus ring on fields. It means "talk to this / do this".

### Secondary
- **Vending Pink** (vend-pink): the vending cart glyph, rate numerals, the pre-renewal chip and the one featured signboard, selection and the global focus outline, invalid fields. It means "this is on offer".
- **Vending Pink Deep** (vend-pink-deep): frame of the pink signboard only.
- **Vending Blush** (vend-soft): hover wash on signboards and the background of an invalid field.

### Tertiary
- **Chat Green** (chat-green): speaker names in the chat box only.
- **System Gold** (system-gold): the system line closing the chat box only.

### Neutral
- **Plaza Stone** (stone): page background colour beneath the cobble tile and the scrollbar track; the tile's seams use **Stone Seam** (stone-seam).
- **Night Ink** (ink): all body text, the outline of name tags.
- **Slate Ink** (ink-soft): form labels, hints, table headers and secondary table cells.
- **Window Paper** (paper): window bodies, signboards, name-tag fill.
- **Window Frame Navy** (win-frame): the 1px frame on every window and signboard.
- **Title Bar Periwinkle** (bar-top to bar-bottom): the vertical gradient on window title bars; bar-top doubles as the plain-button hover.
- **Field Wash / Field Edge** (field-wash, field-edge): input fill and 1px stroke.
- **Hairline Lilac** (hairline): dashed and solid dividers inside windows.
- **Chat Night** (chat-night): translucent dark panel behind the chat box; the plaza lede and footer use the same ink at .78 and .86.
- **Button Face / Button Edge** (button-face, button-edge): the plain client button.

### Named Rules
**The Client Colour Code Rule.** Each accent keeps the job it has in the game: blue for NPCs and actions, pink for vending and offers, green for chat speakers. Never swap them for decoration.

**The Night Panel Rule.** White running text over the plaza always sits on a Chat Night panel; the stone itself is too light (white on stone is 2.4:1).

## Typography

**Display Font:** DotGothic16 (with MS Gothic, monospace)
**Body Font:** Nanum Gothic (with Apple SD Gothic Neo, Malgun Gothic, system-ui)

**Character:** The pixel face is the game speaking: signs, tags, window titles, buttons, NPC names, chat. Nanum Gothic, the client's Korean-heritage gothic, carries anything a visitor reads for more than a line. Both are self-hosted woff2.

### Hierarchy
- **Display** (400, clamp(3.25rem, 8.4vw, 6rem), 0.98): the giant name tag "Ragnarok Forever" only; white fill with a 0.11em Night Ink stroke painted under the fill.
- **Headline** (400, clamp(1.75rem, 4vw, 2.75rem), 1.1): section name tags, same outlined treatment at 0.12em; the closing call uses clamp(2.25rem, 6vw, 4rem).
- **Numeral** (400, clamp(2.25rem, 5vw, 3.25rem), 1, tabular): rate multipliers in Vending Pink.
- **Title** (400, 0.9375rem, 1.3, +0.02em): window title bars and signboards.
- **UI** (400, 1rem, 1.2): buttons, NPC names, NPC menu options, chat lines; nav links at 0.875rem.
- **Body** (400, 1rem, 1.6): running text; rate descriptions cap at 52ch.
- **Label** (700, 0.875rem, 1.2): form labels and table headers in Slate Ink.

### Named Rules
**The Two Voices Rule.** If the game would say it, it is DotGothic16; if the website explains it, it is Nanum Gothic. Never set paragraphs in the pixel face outside the chat box.

**The Name Tag Rule.** Headings on the plaza are white text with a Night Ink stroke (`-webkit-text-stroke` plus `paint-order: stroke fill`), like a character name over a sprite. They sit directly on stone, never in a box.

## Layout

The first viewport is a full-bleed plaza: a two-column grid (fluid title column, NPC window column of minmax(20rem, 27rem)) under a slim nav window spanning the top. Signboards are absolutely positioned over the whole plaza from per-sign `--x`/`--y` custom properties, at varied heights, each with a wooden cart and a soft ground shadow beneath it.

Below the fold, sections are capped at 76rem and alternate sides on desktop (left, right, left, right), each a name tag over one window: rates at up to 56rem, the class shop at up to 48rem, chat box at up to 46rem, download window at 30rem. Section rhythm is clamp(3.5rem, 8vw, 6rem) top padding; page gutters are clamp(1rem, 4vw, 4rem).

Under 900px the plaza collapses to one column: nav window stacks title bar over links, signboards become an inline wrapped cluster of three (the extra three hide, carts and bob are dropped), and the NPC window goes full width. Under 560px form pairs and rate rows stack, and the class table drops its weapon column.

## Elevation & Depth

The UI is flat. No window, button or sign carries a box-shadow. Depth belongs to the world: the cobble tile, the evening overlay (a top-down navy wash plus a warm radial glow at the upper right), windows laid over stone, and soft radial ground shadows under the vending carts.

### Shadow Vocabulary
- **Cart ground shadow** (`radial-gradient(closest-side, rgba(27,33,52,.38), transparent)`, 3.5rem by 1.1rem): under each cart on desktop only.

### Named Rules
**The Flat Client Rule.** Interface chrome is framed, not lifted: a 1px Window Frame Navy border does the work a shadow would. Only things standing on the ground cast a shadow, and only onto the ground.

## Shapes

Small, gentle corners everywhere, matching the client's slightly rounded bitmaps: 4px on windows and panels, 3px on buttons, signs and fields, 5px on the primary button (with a 2px frame), 2px on chips. Borders are 1px hairlines; dividers inside windows are dashed. Window title bars round only their top corners and close with a 1px frame line. Icons are inline SVG line drawings (1.8 stroke, round caps) from one sprite; the cart is a small authored colour illustration.

## Components

### Client Window
Plain, framed, utilitarian.
- **Frame:** Window Paper body, 1px Window Frame Navy border, 4px corners.
- **Title bar:** Title-scale pixel text on the periwinkle gradient, 1px frame line beneath; it names the window ("Kafra", "Información del servidor", "Descarga").
- **Body padding:** 1rem to 1.25rem; a tinted footer strip (#f2f4fc) may close a window with a hairline above.

### Buttons
- **Primary:** NPC Name Blue pixel text, 2px blue frame, 5px corners, white-to-periwinkle vertical gradient, 0.55rem 1.1rem (big: 0.8rem 1.6rem at 1.25rem).
- **Hover:** fills solid blue gradient with white text. **Active:** nudges down 1px. **Busy:** 0.7 opacity, progress cursor.
- **Plain:** grey-blue client button (white to Button Face gradient, 1px Button Edge, 3px), hover to bar-top. Defined in CSS; the current page ships only primary buttons.

### Vending Signboard (signature)
- **Style:** Window Paper, 1px frame, 3px corners, Title-scale pixel text prefixed with the client's own "S>" (selling) or "B>" (buying) marker and a pink cart glyph.
- **Featured:** one sign at most in solid Vending Pink with a Vending Pink Deep frame.
- **Behaviour:** links to the section that "sells" the fact; bobs 4px over 3.6s ease-in-out with staggered delays; hover washes to Vending Blush. Motion stops under reduced motion.

### Inputs / Fields
- **Style:** Field Wash fill, 1px Field Edge, 3px corners, body-face text; label above in Label style, hint below at 0.8125rem.
- **Focus:** 2px NPC Name Blue outline, fill turns white.
- **Error:** Vending Pink border on Vending Blush, with one message in the status line above the submit button.

### NPC Dialog
A client window whose body opens with the NPC's bracketed name in blue pixel text, then a dialog line that types out once (2 characters per 22ms, skipped under reduced motion), then the form, then a dashed-rule menu of chevron options in pixel text.

### Chat Box
Chat Night panel, 4px corners, pixel text at 1rem/1.7 in white; speaker names in Chat Green, links in pale periwinkle (#b9c7ff), closing system line in System Gold.

### Chips
Vending Pink, white pixel text at 0.875rem, 2px corners; used inline as a label inside a window, never above a heading.

### Navigation
A slim client window: title bar holding the server name on the left, pixel links at 0.875rem to the right; hover turns links blue and underlined. On mobile the title bar stacks above the links.

## Do's and Don'ts

### Do:
- **Do** put every new block of content inside a client window or the chat box, framed in 1px Window Frame Navy with a periwinkle title bar.
- **Do** keep the accents on their game jobs: NPC Name Blue for actions and NPC names, Vending Pink for offers and numerals, Chat Green for chat speakers.
- **Do** head plaza sections with outlined white name tags in DotGothic16.
- **Do** use the cobble tile (220px by 110px) as the only page background.
- **Do** place white text on the plaza only over a Chat Night panel.
- **Do** stop the signboard bob and NPC typing under `prefers-reduced-motion`.

### Don't:
- **Don't** add drop shadows to windows, buttons or signboards; only grounded objects cast shadows.
- **Don't** use a dark epic hero, gold serif type, a large character render, or a row of rate cards.
- **Don't** set paragraphs in DotGothic16 outside the chat box.
- **Don't** show invented player counts, uptime, launch dates or reviews on signboards or anywhere else.
- **Don't** feature more than one signboard in solid Vending Pink.
