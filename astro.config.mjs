import { defineConfig } from "astro/config";

// GitHub Pages serves the site from /Ragnarok/ on jeroldambrocio-hash.github.io.
export default defineConfig({
  site: "https://jeroldambrocio-hash.github.io",
  base: "/Ragnarok",
  trailingSlash: "ignore",
});
