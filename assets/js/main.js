// Ragnarok Forever: NPC dialog typing, register form validation, download placeholder.
(() => {
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // The Kafra types her greeting once, like an NPC dialog in the client.
  const line = document.querySelector("[data-type]");
  if (line && !reduced) {
    const full = line.textContent.trim();
    line.setAttribute("aria-label", full);
    line.textContent = "";
    let i = 0;
    const tick = () => {
      i += 2;
      line.textContent = full.slice(0, i);
      if (i < full.length) setTimeout(tick, 22);
      else line.removeAttribute("aria-label");
    };
    setTimeout(tick, 350);
  }

  // Register form. There is no account server yet: valid input gets an honest notice.
  const form = document.getElementById("registro");
  const msg = form.querySelector(".form-msg");
  const messages = {
    usuario: (el) =>
      el.validity.valueMissing ? "Escribe un nombre de usuario." :
      el.validity.tooShort ? "El usuario necesita al menos 4 caracteres." :
      el.validity.patternMismatch ? "Usa solo letras, números o _ en el usuario." : "",
    correo: (el) =>
      el.validity.valueMissing ? "Escribe tu correo." :
      el.validity.typeMismatch ? "Ese correo no parece válido. Revisa la @ y el dominio." : "",
    clave: (el) =>
      el.validity.valueMissing ? "Escribe una contraseña." :
      el.validity.tooShort ? "La contraseña necesita al menos 6 caracteres." : "",
    sexo: (el) => (el.validity.valueMissing ? "Elige el sexo de la cuenta." : ""),
  };

  const show = (text, kind) => {
    msg.textContent = text;
    msg.dataset.kind = kind;
  };

  form.addEventListener("input", (e) => {
    if (e.target.getAttribute("aria-invalid") === "true" && e.target.checkValidity()) {
      e.target.removeAttribute("aria-invalid");
      if (!form.querySelector('[aria-invalid="true"]')) show("", "");
    }
  });

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    let first = null;
    let firstText = "";
    for (const [name, check] of Object.entries(messages)) {
      const el = form.elements[name];
      const text = check(el);
      if (text) {
        el.setAttribute("aria-invalid", "true");
        if (!first) { first = el; firstText = text; }
      } else {
        el.removeAttribute("aria-invalid");
      }
    }
    if (first) {
      show(firstText, "error");
      first.focus();
      return;
    }
    const user = form.elements.usuario.value;
    show(`¡Gracias, ${user}! El registro todavía no está abierto. Guarda tus datos: lo anunciaremos aquí cuando abra.`, "ok");
  });

  // Download link is a placeholder until the owner publishes the client.
  document.querySelectorAll("[data-download]").forEach((a) => {
    if (a.getAttribute("href") !== "#") return;
    a.addEventListener("click", (e) => {
      e.preventDefault();
      const note = a.parentElement.querySelector("[data-download-note]");
      if (note) note.hidden = false;
    });
  });
})();
