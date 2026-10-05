// Novices: look toward the cursor, then react and lead to their section on click.
const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
const novices = Array.from(document.querySelectorAll<HTMLAnchorElement>("[data-novice]"));

if (novices.length && finePointer && !reduced) {
  let px = -1e4;
  let py = -1e4;
  let queued = false;

  const update = () => {
    queued = false;
    for (const el of novices) {
      const r = el.getBoundingClientRect();
      if (r.bottom < 0 || r.top > innerHeight) continue;
      const cx = r.left + r.width / 2;
      const cy = r.top + r.height * 0.45;
      const dx = px - cx;
      const dy = py - cy;
      const dist = Math.hypot(dx, dy);
      // Strong attention nearby, fading out by ~700px.
      const k = Math.max(0, 1 - dist / 700);
      const nx = dist ? dx / dist : 0;
      const ny = dist ? dy / dist : 0;
      el.style.setProperty("--lx", (nx * 2.2 * k).toFixed(2));
      el.style.setProperty("--ly", (ny * 1.6 * k).toFixed(2));
      el.style.setProperty("--tilt", (nx * 9 * k).toFixed(2));
    }
  };

  window.addEventListener(
    "pointermove",
    (e) => {
      px = e.clientX;
      py = e.clientY;
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

for (const el of novices) {
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
    setTimeout(go, 260);
    setTimeout(() => el.classList.remove("is-go"), 700);
  });
}
