// On small screens show one realm at a time.
if (window.matchMedia("(max-width: 900px)").matches) {
  document.querySelectorAll<HTMLDetailsElement>("[data-realms] details").forEach((d, i) => (d.open = i === 0));
}

// Countdown to the next WoE session from the (sample) schedule, in local time.
const root = document.querySelector<HTMLElement>("[data-woe]");
if (root) {
  const sessions: { day: number; start: string; end: string }[] = JSON.parse(root.dataset.schedule || "[]");
  const days = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"];
  const when = root.querySelector<HTMLElement>("[data-woe-when]")!;
  const units = Object.fromEntries(
    Array.from(root.querySelectorAll<HTMLElement>("[data-u]")).map((el) => [el.dataset.u!, el]),
  );

  const next = (now: Date) => {
    let best: { start: Date; end: Date; day: number } | null = null;
    for (const s of sessions) {
      const [sh, sm] = s.start.split(":").map(Number);
      const [eh, em] = s.end.split(":").map(Number);
      for (let add = 0; add <= 7; add++) {
        const d = new Date(now);
        d.setDate(now.getDate() + ((s.day - now.getDay() + 7) % 7) + add * 7);
        const start = new Date(d.getFullYear(), d.getMonth(), d.getDate(), sh, sm);
        const end = new Date(d.getFullYear(), d.getMonth(), d.getDate(), eh, em);
        if (end > now) {
          if (!best || start < best.start) best = { start, end, day: s.day };
          break;
        }
      }
    }
    return best;
  };

  const pad = (n: number) => String(n).padStart(2, "0");
  const tick = () => {
    const now = new Date();
    const n = next(now);
    if (!n) return;
    const live = n.start <= now;
    const ms = Math.max(0, (live ? n.end : n.start).getTime() - now.getTime());
    const s = Math.floor(ms / 1000);
    units.d.textContent = pad(Math.floor(s / 86400));
    units.h.textContent = pad(Math.floor((s % 86400) / 3600));
    units.m.textContent = pad(Math.floor((s % 3600) / 60));
    units.s.textContent = pad(s % 60);
    const hhmm = `${pad(n.start.getHours())}:${pad(n.start.getMinutes())}`;
    when.textContent = live ? "En curso ahora. Termina en:" : `El ${days[n.day]} a las ${hhmm} (tu hora local). Empieza en:`;
    root.classList.toggle("is-live", live);
  };
  tick();
  setInterval(tick, 1000);
}
