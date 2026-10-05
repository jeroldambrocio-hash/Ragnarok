// Plaza: each adventurer lights up and leads to its section on click.
const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

for (const el of document.querySelectorAll<HTMLAnchorElement>("[data-spot]")) {
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
    setTimeout(go, 280);
    setTimeout(() => el.classList.remove("is-go"), 700);
  });
}
