/**
 * War of Emperium. Realm and castle names are the classic pre-renewal ones.
 * Which castles are active and who owns them is not confirmed: owners stay
 * null ("Sin conquistar") until a real API provides them.
 */
export const realms = [
  { realm: "Valkyrie Realms", town: "Prontera", castles: ["Kriemhild", "Swanhild", "Fadhgridh", "Skoegul", "Gondul"] },
  { realm: "Britoniah", town: "Geffen", castles: ["Repherion", "Eeyolbriggar", "Yesnelph", "Bergel", "Mersetzdeitz"] },
  { realm: "Luina", town: "Al De Baran", castles: ["Neuschwanstein", "Hohenschwangau", "Nuernberg", "Wuerzburg", "Rothenburg"] },
  { realm: "Greenwood Lake", town: "Payon", castles: ["Bright Arbor", "Scarlet Palace", "Holy Shadow", "Sacred Altar", "Bamboo Grove Hill"] },
];

/**
 * SAMPLE schedule (not confirmed). day: 0 = domingo … 6 = sábado, server time UTC-3
 * is NOT assumed: times are interpreted in the visitor's local time until the
 * owner sets real ones.
 */
export const schedule = {
  sample: true,
  sessions: [
    { day: 3, start: "21:00", end: "22:00" },
    { day: 6, start: "20:00", end: "22:00" },
  ],
};
