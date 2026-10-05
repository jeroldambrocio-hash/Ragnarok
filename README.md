# Ragnarok Forever

Web del servidor privado de Ragnarok Online **Ragnarok Forever** (clásico, pre-renewal, rates 5x).

- Web publicada: https://jeroldambrocio-hash.github.io/Ragnarok/
- Hecha con [Astro](https://astro.build): `npm install`, `npm run dev` para verla en local, `npm run build` para generarla.
- Se publica sola en GitHub Pages con cada cambio en `main` (`.github/workflows/deploy.yml`).

## Lo que falta rellenar

Todo está en `src/config.ts`: enlace de Discord, enlace de descarga, versión y tamaño del cliente, endpoint de registro y API de estado. Mientras estén vacíos, los botones salen desactivados con "aún no está publicado".

Los datos de ejemplo (estado, jugadores, rankings, horario de WoE) están en `src/data/` y aparecen marcados en la web.

## Arte provisional

El fondo de War of Emperium (`src/components/WoeScene.astro`) es una ilustración SVG provisional.

Los personajes del hero (Novice, Swordman, Mage y Merchant) son pixel art original generado con `python3 tools/sprites.py` (necesita Pillow), en `public/sprites/`. Cada hoja tiene fotogramas de 32x48: columnas reposo, respiración, saludo y celebración; filas cabeza de frente, mirando a la izquierda y a la derecha. Para cambiar un personaje, sustituye su hoja por otra con la misma cuadrícula.

El arte oficial de Ragnarok Online (`public/art/`) lo aportó el dueño del servidor y pertenece a Gravity.

Incluye la skill [impeccable](https://github.com/pbakaus/impeccable) (Apache 2.0) en `.claude/skills/impeccable`.
