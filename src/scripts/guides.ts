// Character guides: turn their head toward the cursor (front, left, right),
// glance around when idle, then cheer and lead to their section on click.
const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
const guides = Array.from(document.querySelectorAll<HTMLAnchorElement>("[data-guide]"));

const look = (el: HTMLElement, row: 0 | 1 | 2) => el.style.setProperty("--row", String(row));

if (guides.length && !reduced) {
  let px = -1e4;
  let py = -1e4;
  let queued = false;
  let lastMove = 0;

  const update = () => {
    queued = false;
    for (const el of guides) {
      const r = el.getBoundingClientRect();
      if (r.bottom < 0 || r.top > innerHeight) continue;
      const dx = px - (r.left + r.width / 2);
      const dy = py - (r.top + r.height / 2);
      // Turn only when the cursor is nearby and clearly to one side.
      const near = Math.hypot(dx, dy) < 700;
      look(el, !near || Math.abs(dx) < 40 ? 0 : dx < 0 ? 1 : 2);
    }
  };

  if (finePointer) {
    window.addEventListener(
      "pointermove",
      (e) => {
        px = e.clientX;
        py = e.clientY;
        lastMove = performance.now();
        if (!queued) {
          queued = true;
          requestAnimationFrame(update);
        }
      },
      { passive: true },
    );
    document.addEventListener("pointerleave", () => {
      px = py = -1e4;
      requestAnimationFrame(update);
    });
  }

  // Idle glances, so the guides feel alive on touch screens and when the cursor rests.
  window.setInterval(() => {
    if (document.hidden || performance.now() - lastMove < 4000) return;
    const el = guides[Math.floor(Math.random() * guides.length)];
    look(el, Math.random() < 0.5 ? 1 : 2);
    window.setTimeout(() => look(el, 0), 900);
  }, 2600);
}

for (const el of guides) {
  el.addEventListener("click", (e) => {
    const hash = el.hash;
    const target = hash ? document.querySelector<HTMLElement>(hash) : null;
    if (!target || e.metaKey || e.ctrlKey || e.shiftKey) return;
    e.preventDefault();
    const go = () => {
      history.pushState(null, "", hash);
      target.scrollIntoView({ behavior: reduced ? "auto" : "smooth", block: "start" });
      // Move focus to the section heading so keyboard and screen reader users land there too.
      const heading = target.querySelector<HTMLElement>("h2");
      if (heading) {
        heading.setAttribute("tabindex", "-1");
        heading.focus({ preventScroll: true });
      }
    };
    if (reduced) return go();
    el.classList.add("is-go");
    setTimeout(go, 300);
    setTimeout(() => el.classList.remove("is-go"), 800);
  });
}
