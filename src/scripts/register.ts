// Register form: validation, then POST to config.registerEndpoint when it exists.
const form = document.querySelector<HTMLFormElement>("[data-register]");
if (form) {
  const msg = form.querySelector<HTMLElement>(".reg-msg")!;
  const submit = form.querySelector<HTMLButtonElement>('[type="submit"]')!;
  const endpoint = form.dataset.endpoint;

  const rules: Record<string, (el: HTMLInputElement) => string> = {
    usuario: (el) =>
      el.validity.valueMissing ? "Escribe un nombre de usuario." :
      el.validity.tooShort ? "El usuario necesita al menos 4 caracteres." :
      el.validity.patternMismatch ? "Usa solo letras, números o _ en el usuario." : "",
    correo: (el) =>
      el.validity.valueMissing ? "Escribe tu correo." :
      el.validity.typeMismatch ? "Ese correo no parece válido." : "",
    clave: (el) =>
      el.validity.valueMissing ? "Escribe una contraseña." :
      el.validity.tooShort ? "La contraseña necesita al menos 6 caracteres." : "",
  };
  const show = (text: string, kind: "error" | "ok" | "") => {
    msg.textContent = text;
    msg.dataset.kind = kind;
  };

  form.addEventListener("input", (e) => {
    const el = e.target as HTMLInputElement;
    if (el.getAttribute("aria-invalid") === "true" && el.checkValidity()) {
      el.removeAttribute("aria-invalid");
      if (!form.querySelector('[aria-invalid="true"]')) show("", "");
    }
  });

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    let first: HTMLInputElement | null = null;
    let firstText = "";
    for (const [name, check] of Object.entries(rules)) {
      const el = form.elements.namedItem(name) as HTMLInputElement;
      const text = check(el);
      if (text) {
        el.setAttribute("aria-invalid", "true");
        if (!first) { first = el; firstText = text; }
      } else el.removeAttribute("aria-invalid");
    }
    if (first) {
      show(firstText, "error");
      first.focus();
      return;
    }

    const data = Object.fromEntries(new FormData(form));
    if (!endpoint) {
      show(`¡Gracias, ${data.usuario}! El registro todavía no está abierto. Lo anunciaremos en Discord en cuanto abra.`, "ok");
      return;
    }
    submit.setAttribute("aria-busy", "true");
    submit.disabled = true;
    try {
      const r = await fetch(endpoint, { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(data) });
      if (!r.ok) throw new Error(String(r.status));
      form.reset();
      show(`Cuenta creada. ¡Bienvenido, ${data.usuario}! Descarga el cliente y entra con tu usuario.`, "ok");
    } catch {
      show("No pudimos crear la cuenta ahora mismo. Inténtalo de nuevo en unos minutos.", "error");
    } finally {
      submit.removeAttribute("aria-busy");
      submit.disabled = false;
    }
  });
}
