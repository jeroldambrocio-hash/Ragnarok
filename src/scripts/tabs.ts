// Accessible tabs (roving tabindex, arrow keys) with a sliding indicator.
for (const root of document.querySelectorAll<HTMLElement>("[data-tabs]")) {
  const tabs = Array.from(root.querySelectorAll<HTMLButtonElement>('[role="tab"]'));
  const ink = root.querySelector<HTMLElement>(".rk-ink");

  const place = (tab: HTMLButtonElement) => {
    if (!ink) return;
    ink.style.setProperty("--x", `${tab.offsetLeft}px`);
    ink.style.setProperty("--w", `${tab.offsetWidth}px`);
  };
  const select = (tab: HTMLButtonElement, focus = false) => {
    for (const t of tabs) {
      const on = t === tab;
      t.setAttribute("aria-selected", String(on));
      t.tabIndex = on ? 0 : -1;
      const panel = document.getElementById(t.getAttribute("aria-controls")!);
      if (panel) panel.hidden = !on;
    }
    place(tab);
    if (focus) tab.focus();
  };

  tabs.forEach((t, i) => {
    t.addEventListener("click", () => select(t));
    t.addEventListener("keydown", (e) => {
      const dir = e.key === "ArrowRight" ? 1 : e.key === "ArrowLeft" ? -1 : 0;
      if (dir) {
        e.preventDefault();
        select(tabs[(i + dir + tabs.length) % tabs.length], true);
      } else if (e.key === "Home") {
        e.preventDefault();
        select(tabs[0], true);
      } else if (e.key === "End") {
        e.preventDefault();
        select(tabs[tabs.length - 1], true);
      }
    });
  });

  const current = () => tabs.find((t) => t.getAttribute("aria-selected") === "true") ?? tabs[0];
  place(current());
  addEventListener("resize", () => place(current()));
  document.fonts?.ready.then(() => place(current()));

  // Links elsewhere (e.g. "Ver ranking de guilds") can open a specific tab.
  document.querySelectorAll<HTMLAnchorElement>("[data-tab-link]").forEach((a) => {
    a.addEventListener("click", () => {
      const t = tabs.find((x) => x.dataset.tab === a.dataset.tabLink);
      if (t) select(t);
    });
  });
}
