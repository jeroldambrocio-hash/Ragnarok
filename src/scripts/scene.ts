// Hero scene: pointer/scroll parallax across layers and a light ember canvas.
const scene = document.querySelector<HTMLElement>(".scene");
const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (scene && !reduced) {
  const layers = Array.from(scene.querySelectorAll<HTMLElement>("[data-depth]"));
  const fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  let mx = 0;
  let my = 0;
  let sy = 0;
  let queued = false;
  let visible = true;

  const apply = () => {
    queued = false;
    for (const l of layers) {
      const d = Number(l.dataset.depth || 0);
      const x = -mx * 14 * d;
      const y = -my * 8 * d + sy * 0.18 * d;
      l.style.transform = `translate3d(${x.toFixed(1)}px, ${y.toFixed(1)}px, 0)`;
    }
  };
  const request = () => {
    if (!queued && visible) {
      queued = true;
      requestAnimationFrame(apply);
    }
  };

  if (fine) {
    window.addEventListener(
      "pointermove",
      (e) => {
        mx = e.clientX / innerWidth - 0.5;
        my = e.clientY / innerHeight - 0.5;
        request();
      },
      { passive: true },
    );
  }
  window.addEventListener(
    "scroll",
    () => {
      sy = Math.min(scrollY, innerHeight);
      request();
    },
    { passive: true },
  );

  // Embers
  const canvas = scene.querySelector<HTMLCanvasElement>("[data-embers]");
  const ctx = canvas?.getContext("2d");
  if (canvas && ctx) {
    type P = { x: number; y: number; vx: number; vy: number; r: number; life: number; max: number };
    const dpr = Math.min(devicePixelRatio || 1, 1.5);
    let w = 0;
    let h = 0;
    let parts: P[] = [];
    const count = () => (innerWidth < 760 ? 16 : 34);

    const portrait = window.matchMedia("(max-width: 760px), (max-aspect-ratio: 1/1)");
    const spawn = (initial = false): P => {
      // Embers rise from the castle: right side on wide screens, top band in portrait.
      const originX = w * (portrait.matches ? 0.66 : 0.76);
      const top = portrait.matches ? 0.22 : 0.62;
      return {
        x: originX + (Math.random() - 0.5) * w * 0.32,
        y: initial ? Math.random() * h * (portrait.matches ? 0.5 : 1) : h * (top + Math.random() * 0.14),
        vx: (Math.random() - 0.4) * 0.25,
        vy: -(0.25 + Math.random() * 0.55),
        r: 0.6 + Math.random() * 1.5,
        life: 0,
        max: 260 + Math.random() * 260,
      };
    };
    const resize = () => {
      w = scene.clientWidth;
      h = scene.clientHeight;
      canvas.width = Math.round(w * dpr);
      canvas.height = Math.round(h * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      parts = Array.from({ length: count() }, () => spawn(true));
    };
    resize();
    let rt = 0;
    window.addEventListener("resize", () => {
      clearTimeout(rt);
      rt = window.setTimeout(resize, 150);
    });

    let raf = 0;
    const tick = () => {
      ctx.clearRect(0, 0, w, h);
      for (let i = 0; i < parts.length; i++) {
        const p = parts[i];
        p.life++;
        p.x += p.vx + Math.sin((p.life + i * 20) / 40) * 0.18;
        p.y += p.vy;
        const t = p.life / p.max;
        if (t >= 1 || p.y < -10) {
          parts[i] = spawn();
          continue;
        }
        const a = Math.sin(t * Math.PI) * 0.85;
        ctx.beginPath();
        ctx.fillStyle = `rgba(255, ${170 + Math.round(60 * (1 - t))}, 100, ${a.toFixed(3)})`;
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fill();
      }
      raf = requestAnimationFrame(tick);
    };
    const start = () => {
      if (!raf) raf = requestAnimationFrame(tick);
    };
    const stop = () => {
      cancelAnimationFrame(raf);
      raf = 0;
    };

    // Only animate while the hero is on screen and the tab is visible.
    new IntersectionObserver(([entry]) => {
      visible = entry.isIntersecting;
      if (visible && !document.hidden) start();
      else stop();
    }).observe(scene);
    document.addEventListener("visibilitychange", () => (document.hidden || !visible ? stop() : start()));
  }
}
