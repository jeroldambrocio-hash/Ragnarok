---
version: 1
slug: "src-pages-index-astro"
primary_target: "src/pages/index.astro"
related_targets: []
---

# Surface: home page (src/pages/index.astro)

Mode: Persuade. Replaces the earlier Prontera-plaza page (redesign requested by the owner on 2026-10-05; the old look is evidence, not authority). Visitor: Spanish-speaking classic-RO player, often on a phone from Discord, deciding fast. Actions: Jugar ahora (register, 3 fields), Descargar, Discord. Content without real data (status, players, rankings, WoE schedule, castles) ships as sample data that is labelled on the page and wired for an API.

Direction: pinned by the owner's brief (no concept roll). Build path: code-led (no image generation).

## Direction contract

THESIS: The eve of a War of Emperium. The visitor stands on a dark hill facing a lit castle under siege, and a small band of Novices waits beside them to take them anywhere on the page. It refuses both the old private-server page (banners, tables, bevelled buttons) and the generic dark gaming template (neon glow, glass cards, a grid of six feature tiles).

OWN-WORLD: Night charcoal ground, graphite planes, off-white text, gold used only for the primary action, key numerals and focus, and banner crimson used only for WoE and live states. Faculty Glyphic for display, Onest for text. Hairline rules instead of boxes, very few containers, generous space. The scene is authored layered SVG (sky, far hills, castle, wall fires, banners, near ridge) with canvas embers. Novices are authored SVG characters with a sprite slot.

STORY: The visitor reads RAGNAROK FOREVER and "El Ragnarok clásico. Para siempre.", sees pre-renewal 5x, and can play from the hero. The Novices lead to Servidor, WoE, Rankings and Descargar. Then: server at a glance, why play, WoE (castles, next siege, schedule), rankings, download, a 3-field register, and Discord.

FIRST VIEWPORT: Desktop: a full-bleed night siege scene. The castle sits on the far right third; title stacked centre-left at display scale; tagline and one meta line under it; then "Jugar ahora" (gold, the only filled button), "Descargar" (outline) and "Discord" (text). Four Novices stand on the foreground ridge along the bottom edge, two each side of centre, with labels. Compact sticky nav on top. Mobile: the scene is cropped to the castle, the title and actions stack, and the Novices become a 4-up touch dock with labels always visible.

FORM: Pinned by the brief; no roll. The direction was derived by hand from the brief: WoE eve, modern premium UI. Seed key: none (pinned). Signature interaction: the Novices turn their eyes and heads toward the cursor and hop on hover with a label; on click one salutes and runs off, and the page scrolls to its section. The hero layers parallax subtly with the pointer and with scroll.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
