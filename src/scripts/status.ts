// Replaces sample status with live data when config.statusApi is set.
const root = document.querySelector<HTMLElement>("[data-status]");
const api = root?.dataset.api;
if (root && api) {
  fetch(api, { headers: { accept: "application/json" } })
    .then((r) => (r.ok ? r.json() : Promise.reject(r.status)))
    .then((d: { online: boolean; players: number; uptime: number }) => {
      root.querySelector("[data-status-sample]")?.remove();
      const dot = root.querySelector<HTMLElement>(".dot");
      if (dot) dot.dataset.online = String(d.online);
      root.querySelector("[data-status-online]")!.textContent = d.online ? "En línea" : "Fuera de línea";
      root.querySelector("[data-status-players]")!.textContent = new Intl.NumberFormat("es").format(d.players);
      root.querySelector("[data-status-uptime]")!.textContent = `${d.uptime}%`;
    })
    .catch(() => {
      // Keep the labelled sample values if the API is unreachable.
    });
}
