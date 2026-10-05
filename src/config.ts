/**
 * Site configuration. Everything the owner still has to provide lives here.
 * Leave a value empty and the matching button shows a disabled "Próximamente"
 * state instead of a fake link.
 */
export const config = {
  name: "Ragnarok Forever",
  /** Discord invite, e.g. "https://discord.gg/xxxx". */
  discordUrl: "",
  /** Direct link to the client installer or archive. */
  downloadUrl: "",
  /** Client details shown next to the download button. null = not published yet. */
  client: { version: null as string | null, size: null as string | null },
  /** POST endpoint for account creation (JSON: usuario, correo, clave, sexo). */
  registerEndpoint: "",
  /** GET endpoint returning live status JSON (see src/data/server.ts). */
  statusApi: "",
};
