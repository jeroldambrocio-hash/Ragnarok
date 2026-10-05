/** Confirmed facts about the server (PRODUCT.md). Safe to show as real. */
export const facts = {
  /** Episode number not confirmed yet. */
  episode: null as string | null,
  rates: [
    { label: "Base EXP", value: "5x" },
    { label: "Job EXP", value: "5x" },
    { label: "Drop", value: "5x" },
    // Provisional, approved by the owner on 2026-10-05.
    { label: "MVP", value: "5x" as string | null },
  ],
};

/**
 * Live status. These are SAMPLE values for layout only; the page labels them.
 * When config.statusApi is set, src/scripts/status.ts replaces them with the
 * API response: { online: boolean, players: number, uptime: number }.
 */
export const sampleStatus = {
  sample: true,
  online: true,
  players: 1248,
  uptime: 99.4,
};
