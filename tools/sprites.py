"""Pixel-art guides for the hero, drawn from code (original art, Ragnarok-style).

Run:  python3 tools/sprites.py      (needs Pillow)
Writes public/sprites/<class>.png: a sheet of 32x48 frames.
  columns: idle, idle (breath), wave, cheer
  rows:    head front, head looking left, head looking right
Like the game, head and body are separate layers, so the head can turn
toward the cursor while the body keeps its pose.
"""
from pathlib import Path
from PIL import Image

W, H = 32, 48
COLS, ROWS = 4, 3


def hexc(s):
    s = s.lstrip("#")
    return tuple(int(s[i:i + 2], 16) for i in (0, 2, 4)) + (255,)


def mix(c, t, k):
    return tuple(round(c[i] + (t[i] - c[i]) * k) for i in range(3)) + (255,)


def shade(c, k=0.24):
    return mix(c, (40, 20, 30), k)


def light(c, k=0.22):
    return mix(c, (255, 250, 235), k)


def line(c):
    return mix(c, (22, 12, 14), 0.74)


class Part:
    """A filled shape that gets the sprite treatment: outline, shade, highlight."""

    def __init__(self, color, pts=None, flat=False):
        self.c = hexc(color)
        self.pts = set(pts or [])
        self.flat = flat

    def rect(self, x0, y0, x1, y1):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                self.pts.add((x, y))
        return self

    def ellipse(self, cx, cy, rx, ry):
        for y in range(int(cy - ry) - 1, int(cy + ry) + 2):
            for x in range(int(cx - rx) - 1, int(cx + rx) + 2):
                if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1.0:
                    self.pts.add((x, y))
        return self

    def cut(self, pts):
        self.pts -= set(pts)
        return self

    def shift(self, dx, dy):
        return Part.__new__(Part).__init_from(self, dx, dy)

    def __init_from(self, o, dx, dy):
        self.c, self.flat = o.c, o.flat
        self.pts = {(x + dx, y + dy) for x, y in o.pts}
        return self

    def mirror(self):
        p = Part.__new__(Part)
        p.c, p.flat = self.c, self.flat
        p.pts = {(W - 1 - x, y) for x, y in self.pts}
        return p

    def paint(self, px):
        m = self.pts
        for (x, y) in m:
            if not (0 <= x < W and 0 <= y < H):
                continue
            if self.flat:
                px[x, y] = self.c
                continue
            edge = any((x + a, y + b) not in m for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)))
            if edge:
                col = line(self.c)
            elif (x + 2, y) not in m or (x, y + 2) not in m:
                col = shade(self.c)
            elif (x - 2, y) not in m and (x, y - 2) not in m:
                col = light(self.c)
            else:
                col = self.c
            px[x, y] = col


def from_half(rows, key, y0=0, extra=()):
    """Build a symmetric mask from left-half text rows (16 wide)."""
    pts = set()
    for j, r in enumerate(rows):
        assert len(r) <= 16, r
        for i, ch in enumerate(r):
            if ch == key:
                pts.add((i, y0 + j))
                pts.add((W - 1 - i, y0 + j))
    pts |= set(extra)
    return pts


SKIN = "#f4cfac"

HAIR = {
    "spiky": [
        "..........h.....",
        "......h..hh....h",
        ".......hhhhh..hh",
        "......hhhhhhhhhh",
        ".....hhhhhhhhhhh",
        "....hhhhhhhhhhhh",
        "...hhhhhhhhhhhhh",
        "..hhhhhhhhhhhhhh",
        "...hhhhhhhhhhhhh",
        "....hhhhhhh.hhhh",
        "....hhhhhh...hhh",
        "....hhhhh.....hh",
        ".....hhh........",
        ".....hh.........",
        "......h.........",
    ],
    "short": [
        "................",
        "................",
        "........hhhhhhhh",
        "......hhhhhhhhhh",
        ".....hhhhhhhhhhh",
        "....hhhhhhhhhhhh",
        "....hhhhhhhhhhhh",
        "....bbbbbbbbbbbb",
        "....bbbbbbbbbbbb",
        "....hhhh.hhhhhhh",
        "....hhh...hhhh.h",
        "....hh.......h..",
        "....h...........",
    ],
    "long": [
        "................",
        "................",
        ".........hhhhhhh",
        ".......hhhhhhhhh",
        "......hhhhhhhhhh",
        ".....hhhhhhhhhhh",
        "....hhhhhhhhhhhh",
        "....hhhhhhhhhhh.",
        "...hhhhhhhhhhh..",
        "...hhhhhhhhhh...",
        "...hhhhhhhhh....",
        "...hhhhhh.......",
        "...hhhh.........",
        "...hhh..........",
        "...hhh..........",
        "...hhh..........",
        "...hhh..........",
        "....hh..........",
    ],
    "bandana": [
        "................",
        "................",
        ".........bbbbbbb",
        ".......bbbbbbbbb",
        "......bbbbbbbbbb",
        ".....bbbbbbbbbbb",
        ".....bbbbbbbbbbb",
        "....bbbbbbbbbbbb",
        "....hhhhhhhhhhhh",
        "....hhhhh.hhhhhh",
        "....hhhh...hhhhh",
        "...hhhh.....hhh.",
        "...hhh..........",
        "....h...........",
    ],
}

CLASSES = {
    "novice": dict(hair="spiky", hc="#7a4a2a", band=None, top="#d8c39a", sleeve="#d8c39a",
                   pants="#7c5537", boots="#4a3122", belt="#6b4428"),
    "swordman": dict(hair="short", hc="#3b2a24", band="#c23a45", top="#8f3b2e", sleeve="#8f3b2e",
                     pants="#3c3f4a", boots="#5a3a24", belt="#4a3122"),
    "mage": dict(hair="long", hc="#4a3566", band=None, top="#4a3b7c", sleeve="#4a3b7c",
                 pants="#4a3b7c", boots="#3a2a22", belt="#d4b06a"),
    "merchant": dict(hair="bandana", hc="#d8893c", band="#2f6b5a", top="#efe2c6", sleeve="#efe2c6",
                     pants="#6d5040", boots="#5a3a24", belt="#5a3a24"),
}


def head_parts(cfg, look):
    """look: 0 front, -1 left. (Right is the mirror of left.)"""
    dx = -2 if look else 0
    parts = []
    if cfg["hair"] == "long":
        parts.append(("back", Part(cfg["hc"]).rect(6, 10, 25, 28).cut(
            {(x, y) for x in (6, 25) for y in (27, 28)})))
    ears = Part(SKIN).rect(6 + (1 if look else 0), 12, 7 + (1 if look else 0), 15)
    if not look:
        ears.rect(24, 12, 25, 15)
    parts.append(("head", ears))
    parts.append(("head", Part(SKIN).ellipse(15.5 + dx * 0.25, 12.5, 8.6, 8.6)))
    rows = HAIR[cfg["hair"]]
    hair = Part(cfg["hc"], from_half(rows, "h"))
    band = Part(cfg["band"] or cfg["hc"], from_half(rows, "b"))
    if cfg["hair"] == "short":
        band.pts |= {(26, 8), (27, 8), (27, 9), (28, 9), (28, 10), (27, 11)}
    if cfg["hair"] == "bandana":
        band.pts |= {(26, 6), (27, 6), (27, 7), (28, 7), (28, 8), (27, 9)}
    if look:
        # Turned head: hair slides a pixel toward the look direction.
        hair.pts = {(x - 1, y) for x, y in hair.pts}
        band.pts = {(x - 1, y) for x, y in band.pts}
    face = []
    eye = hexc("#3a2620")
    hi = hexc("#ffffff")
    for ex in (11 + dx, 19 + dx):
        for y in (13, 14, 15):
            for x in (ex, ex + 1):
                face.append((x, y, eye))
        face.append((ex, 13, hi))
    mouth = hexc("#b0645a")
    face += [(15 + dx, 18, mouth), (16 + dx, 18, mouth)]
    blush = hexc("#f0a98f")
    face += [(9 + dx, 17, blush), (22 + dx, 17, blush)] if not look else [(8 + dx + 1, 17, blush), (20 + dx, 17, blush)]
    parts.append(("hair", hair))
    if band.pts:
        parts.append(("hair", band))
    return parts, face


def body_parts(cfg, name, pose, dy):
    """pose: idle | wave | cheer.  dy: breathing offset for the upper body."""
    under, mid, over = [], [], []
    legs = Part(cfg["pants"]).rect(11, 34, 14, 42).rect(17, 34, 20, 42)
    boots = Part(cfg["boots"]).rect(10, 41, 14, 45).rect(17, 41, 21, 45)
    under += [legs, boots]
    neck = Part(SKIN).rect(14, 20 + dy, 17, 23 + dy)
    torso = Part(cfg["top"]).rect(10, 24 + dy, 21, 34 + dy).rect(11, 23 + dy, 20, 23 + dy)
    mid += [neck, torso]
    if name == "novice":
        mid.append(Part("#f2ead8", flat=True).rect(14, 24 + dy, 17, 24 + dy).rect(15, 25 + dy, 16, 26 + dy))
    if name == "swordman":
        mid.append(Part("#aab3bf").ellipse(15.5, 26.5 + dy, 5.6, 3.8))
        mid.append(Part("#7d8794", flat=True).rect(15, 24 + dy, 16, 29 + dy))
        under.insert(0, Part("#4a3122").rect(4, 30, 5, 43))
        under.insert(1, Part("#6b4428").rect(4, 26, 5, 28))
        under.insert(2, Part("#d4b06a").rect(2, 29, 7, 29))
    if name == "mage":
        robe = Part(cfg["top"]).rect(10, 24 + dy, 21, 44).rect(9, 36, 22, 44)
        mid[-1] = robe
        mid.append(Part("#d4b06a", flat=True).rect(15, 26 + dy, 16, 44))
        mid.append(Part("#5b4a96").rect(12, 22 + dy, 19, 24 + dy))
    if name == "merchant":
        mid.append(Part("#b0614c").rect(10, 24 + dy, 13, 33 + dy).rect(18, 24 + dy, 21, 33 + dy))
        mid.append(Part("#d98c6a").rect(13, 22 + dy, 18, 24 + dy))
        under.append(Part("#8a6a45").rect(21, 30, 25, 37))
    if name != "mage":
        mid.append(Part(cfg["belt"]).rect(10, 31 + dy, 21, 32 + dy))
        mid.append(Part("#d4b06a", flat=True).rect(15, 31 + dy, 16, 32 + dy))
    else:
        mid.append(Part(cfg["belt"]).rect(10, 31 + dy, 21, 31 + dy))

    def arm_down(left):
        a = Part(cfg["sleeve"]).rect(7, 24 + dy, 9, 33 + dy)
        h = Part(SKIN).rect(7, 33 + dy, 9, 35 + dy)
        return [a, h] if left else [a.mirror(), h.mirror()]

    def arm_up(left):
        a = Part(cfg["sleeve"]).rect(4, 16 + dy, 6, 21 + dy).rect(5, 20 + dy, 7, 23 + dy).rect(7, 22 + dy, 9, 25 + dy)
        h = Part(SKIN).rect(3, 13 + dy, 5, 16 + dy)
        return [a, h] if left else [a.mirror(), h.mirror()]

    arms_low, arms_high = [], []
    if pose == "idle":
        arms_low = arm_down(True) + arm_down(False)
    elif pose == "wave":
        arms_low = arm_down(True)
        arms_high = arm_up(False)
    else:
        arms_high = arm_up(True) + arm_up(False)
    if name == "swordman":
        pads = [Part("#aab3bf").rect(7, 23 + dy, 10, 25 + dy)]
        pads.append(pads[0].mirror())
        over += pads
    if name == "mage":
        top = 16 if pose in ("idle", "wave") else 6
        sx = 4 if top == 16 else 3
        staff = [Part("#7a5236").rect(sx, top, sx + 1, top + 30), Part("#8fd0ff").ellipse(sx + 0.5, top - 1, 1.8, 1.8)]
        (arms_low if top == 16 else arms_high)[:0] = staff
    return under, mid, arms_low, over, arms_high


def frame(cfg, name, pose, dy, look):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    px = img.load()
    under, mid, arms_low, over, arms_high = body_parts(cfg, name, pose, dy)
    hparts, face = head_parts(cfg, -1 if look else 0)
    shift = lambda p: p.shift(0, dy)
    for kind, p in hparts:
        if kind == "back":
            shift(p).paint(px)
    for p in under + mid + arms_low + over:
        p.paint(px)
    head = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    hp = head.load()
    for kind, p in hparts:
        if kind != "back":
            shift(p).paint(hp)
    for x, y, c in face:
        hp[x, y + dy] = c
    if look == 1:
        head = head.transpose(Image.FLIP_LEFT_RIGHT)
    img.alpha_composite(head)
    px = img.load()
    for p in arms_high:
        p.paint(px)
    return img


def main():
    out = Path(__file__).resolve().parent.parent / "public" / "sprites"
    out.mkdir(parents=True, exist_ok=True)
    poses = [("idle", 0), ("idle", 1), ("wave", 0), ("cheer", 0)]
    for name, cfg in CLASSES.items():
        sheet = Image.new("RGBA", (W * COLS, H * ROWS), (0, 0, 0, 0))
        for r, look in enumerate((0, -1, 1)):
            for c, (pose, dy) in enumerate(poses):
                sheet.alpha_composite(frame(cfg, name, pose, dy, look), (c * W, r * H))
        sheet.save(out / f"{name}.png", optimize=True)
        print("wrote", out / f"{name}.png")


if __name__ == "__main__":
    main()
