"""Pixel-art job characters for the hero guides, in the style of Ragnarok Online.

Run:  python3 tools/sprites.py      (needs Pillow)
Writes public/sprites/<job>.png: a sheet of 44x72 frames.
  columns: idle, idle (breath), wave, cheer
  rows:    head front, head looking left, head looking right
Like the game, head and body are separate layers, so the head turns toward
the cursor while the body keeps its pose. Shapes are shaded with a light from
the top left in four tones and given coloured outlines ("sel-out").
"""
import math
from pathlib import Path
from PIL import Image

FW, FH = 44, 72
COLS, ROWS = 4, 3
CX = 21.5


def hexc(s):
    s = s.lstrip("#")
    return tuple(int(s[i:i + 2], 16) for i in (0, 2, 4)) + (255,)


def mix(c, t, k):
    return tuple(round(c[i] + (t[i] - c[i]) * k) for i in range(3)) + (255,)


def tones(base):
    c = hexc(base)
    return [mix(c, (255, 248, 230), 0.3), c, mix(c, (60, 30, 50), 0.28), mix(c, (40, 18, 34), 0.5)]


def outline(c):
    return mix(c, (30, 14, 18), 0.72)


class Shape:
    """A pixel mask with a shading frame (box it is lit across)."""

    def __init__(self, color, fn=None, box=None, flat=False, light_k=1.0):
        self.t = tones(color) if isinstance(color, str) else color
        self.pts = set()
        self.flat = flat
        self.box = box
        self.light_k = light_k
        if fn:
            for y in range(FH):
                for x in range(FW):
                    if fn(x + 0.5, y + 0.5):
                        self.pts.add((x, y))

    def add(self, other):
        self.pts |= other.pts
        return self

    def moved(self, dx, dy):
        s = Shape(self.t, flat=self.flat, light_k=self.light_k)
        s.t = self.t
        s.pts = {(x + dx, y + dy) for x, y in self.pts}
        s.box = None if self.box is None else (self.box[0] + dx, self.box[1] + dy, self.box[2] + dx, self.box[3] + dy)
        return s

    def mirrored(self):
        s = Shape(self.t, flat=self.flat, light_k=self.light_k)
        s.pts = {(FW - 1 - x, y) for x, y in self.pts}
        s.box = None if self.box is None else (FW - self.box[2], self.box[1], FW - self.box[0], self.box[3])
        return s

    def paint(self, px):
        if not self.pts:
            return
        xs = [p[0] for p in self.pts]
        ys = [p[1] for p in self.pts]
        x0, y0, x1, y1 = self.box or (min(xs), min(ys), max(xs) + 1, max(ys) + 1)
        for (x, y) in self.pts:
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if self.flat:
                px[x, y] = self.t[1]
                continue
            nx = ((x + 0.5) - (x0 + x1) / 2) / max(1, (x1 - x0) / 2)
            ny = ((y + 0.5) - (y0 + y1) / 2) / max(1, (y1 - y0) / 2)
            lum = -(nx * 0.75 + ny * 0.45) * self.light_k
            edge = [(x + a, y + b) in self.pts for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1))]
            if not all(edge):
                # Coloured outline: darkest against the outside.
                px[x, y] = outline(self.t[1])
                continue
            i = 0 if lum > 0.45 else 1 if lum > -0.15 else 2 if lum > -0.6 else 3
            px[x, y] = self.t[i]


def ellipse(cx, cy, rx, ry):
    return lambda x, y: ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1


def box(x0, y0, x1, y1):
    return lambda x, y: x0 <= x < x1 and y0 <= y < y1


def poly(points):
    def inside(x, y):
        n, c = len(points), False
        for i in range(n):
            (ax, ay), (bx, by) = points[i], points[(i + 1) % n]
            if (ay > y) != (by > y) and x < (bx - ax) * (y - ay) / (by - ay) + ax:
                c = not c
        return c
    return inside


def union(*fns):
    return lambda x, y: any(f(x, y) for f in fns)


def sym(points):
    """Mirror a left-half outline around the centre line."""
    right = [(2 * CX - x, y) for x, y in reversed(points)]
    return points + right


SKIN = "#f6d3b2"

# ------------------------------------------------------------------ heads

def face_shape(dx):
    head = lambda x, y: (((x - CX - dx * 0.3) / 11.5) ** 2 + ((y - 19) / 12) ** 2 <= 1) and not (
        y > 27 and abs(x - CX - dx * 0.4) > 11.5 - (y - 27) * 1.15)
    return Shape(SKIN, head, box=(9, 7, 34, 32), light_k=0.45)


def eyes(dx, iris):
    """RO-style big eyes: dark lash on top, coloured iris, white sparkle."""
    out = []
    lash = hexc("#2a1814")
    ir = hexc(iris)
    ir_d = mix(ir, (20, 10, 10), 0.45)
    white = hexc("#fffaf0")
    for ex in (14 + dx, 25 + dx):
        for x in range(ex, ex + 5):
            out.append((x, 19, lash))
        out.append((ex - 1 if ex < 20 + dx else ex + 5, 19, lash))
        for y in range(20, 25):
            for x in range(ex, ex + 4 if ex < 20 + dx else ex + 4):
                c = ir_d if y < 22 else ir
                if x in (ex, ex + 3) and y in (20, 24):
                    continue
                out.append((x + (0 if ex < 20 + dx else 1), y, c))
        sx = ex + (1 if ex < 20 + dx else 2)
        out.append((sx, 21, white))
        out.append((sx + 1, 21, white))
        out.append((sx + 1, 22, white))
    out.append((21 + dx, 28, hexc("#c06a5a")))
    out.append((22 + dx, 28, hexc("#c06a5a")))
    blush = hexc("#f2ad96")
    for bx in (12 + dx, 30 + dx):
        out.append((bx, 26, blush))
        out.append((bx + 1, 26, blush))
    return out


def hair_spiky(color, dx):
    """Novice / Swordman: a crown of chunky spikes and pointed bangs."""
    cap = ellipse(CX + dx * 0.5, 15, 13.5, 11)
    spikes = [
        poly([(8, 16), (2, 12), (9, 10)]), poly([(9, 10), (4, 3), (13, 6)]),
        poly([(13, 6), (12, -1), (19, 4)]), poly([(19, 4), (23, -2), (25, 4)]),
        poly([(25, 4), (32, 0), (31, 7)]), poly([(31, 7), (40, 4), (35, 11)]),
        poly([(35, 12), (42, 13), (35, 17)]),
    ]
    bangs = [poly([(10, 12), (11, 25), (15, 13)]), poly([(14, 12), (17, 21), (20, 12)]),
             poly([(19, 12), (22, 19), (25, 12)]), poly([(24, 12), (28, 21), (30, 12)]),
             poly([(29, 12), (33, 25), (34, 13)])]
    sideburn = union(box(8.5, 16, 11, 26), box(32.5, 16, 35, 26))
    fn = union(lambda x, y: cap(x, y) and y < 14, *spikes, *bangs, sideburn)
    shifted = lambda x, y: fn(x - dx, y)
    return Shape(color, shifted, box=(4, 0, 40, 26))


def hair_long(color, dx):
    cap = ellipse(CX + dx * 0.5, 15, 13.5, 11.5)
    part = lambda x, y: abs(x - CX - dx) < 0.8 and y > 6 and y < 13
    bangs = [poly([(9, 12), (10, 30), (15, 13)]), poly([(15, 12), (19, 19), (21, 11)]),
             poly([(22, 11), (25, 19), (29, 12)]), poly([(28, 12), (34, 30), (35, 13)])]
    fn = union(lambda x, y: cap(x, y) and y < 14 and not part(x, y), *bangs)
    return Shape(color, lambda x, y: fn(x - dx, y), box=(7, 3, 37, 30))


def hair_back_long(color):
    return Shape(color, union(box(8, 14, 36, 44), ellipse(CX, 44, 13.5, 4)), box=(8, 14, 36, 48), light_k=0.6)


def hair_bandana(color, band, dx):
    cap = ellipse(CX + dx * 0.5, 15, 13.5, 11)
    tufts = [poly([(8, 13), (4, 18), (10, 18)]), poly([(35, 13), (40, 18), (34, 18)]),
             poly([(11, 13), (12, 22), (16, 14)]), poly([(16, 13), (19, 19), (22, 13)]),
             poly([(22, 13), (26, 20), (28, 13)]), poly([(28, 13), (32, 22), (33, 14)])]
    hair = Shape(color, lambda x, y: union(lambda a, b: cap(a, b) and 10 <= b < 15, *tufts)(x - dx, y), box=(4, 8, 40, 22))
    scarf = Shape(band, lambda x, y: (cap(x - dx, y) and y < 12) or poly([(33, 8), (41, 11), (39, 16), (35, 12)])(x - dx, y), box=(8, 2, 40, 14))
    return [hair, scarf]


# ------------------------------------------------------------------ bodies

def legs(pants, boots, robe=False):
    out = []
    if not robe:
        out.append(Shape(pants, union(box(15, 48, 21.2, 61), box(22.8, 48, 29, 61)), box=(15, 48, 29, 61)))
    b = union(box(14, 59, 21, 67), ellipse(16.8, 67, 4, 2.6), box(23, 59, 30, 67), ellipse(27.2, 67, 4, 2.6))
    out.append(Shape(boots, b, box=(13, 58, 31, 70)))
    return out


def torso(color, robe=False):
    pts = sym([(CX, 32), (15, 32), (12, 34), (13, 40), (14.5, 49)])
    if robe:
        pts = sym([(CX, 32), (15, 32), (12, 34), (12.5, 45), (11, 63), (13, 64)])
    return Shape(color, poly(pts), box=(11, 31, 33, 64 if robe else 50))


def arm_down(sleeve, right=False):
    s = [Shape(sleeve, ellipse(11.5, 37.5, 3.2, 4.6), box=(8, 33, 15, 42)),
         Shape(SKIN, union(box(9.5, 40, 13.5, 47)), box=(9, 40, 14, 47)),
         Shape(SKIN, ellipse(11.5, 48, 2.6, 2.4), box=(9, 45, 14, 51))]
    return [p.mirrored() for p in s] if right else s


def arm_up(sleeve, right=False):
    s = [Shape(sleeve, ellipse(11.5, 36.5, 3.2, 4.2), box=(8, 32, 15, 41)),
         Shape(SKIN, poly([(9, 35), (12.5, 35), (8.5, 23), (5, 23)]), box=(4, 22, 13, 36)),
         Shape(SKIN, ellipse(6.6, 21, 2.7, 2.6), box=(3, 18, 10, 24))]
    return [p.mirrored() for p in s] if right else s


JOBS = {
    "novice": dict(hair="spiky", hc="#7a4a26", iris="#7a4a2a", shirt="#efe4c8", sleeve="#efe4c8",
                   pants="#9a7550", boots="#5e3d26"),
    "swordman": dict(hair="spiky", hc="#4a3a5a", iris="#4a5a8a", shirt="#9c3a32", sleeve="#9c3a32",
                     pants="#4a4652", boots="#5a3a24"),
    "mage": dict(hair="long", hc="#3e2e5c", iris="#6a4aa0", shirt="#4b3c86", sleeve="#4b3c86",
                 pants="#4b3c86", boots="#3a2a22"),
    "merchant": dict(hair="bandana", hc="#d9893a", band="#3a7a62", iris="#5a7a3a", shirt="#efe4c8",
                     sleeve="#efe4c8", pants="#7a5a42", boots="#5a3a24"),
}


def body(job, cfg, pose, dy):
    """Returns (behind_head, body_layers, raised_arms) for a pose."""
    robe = job == "mage"
    lower = legs(cfg["pants"], cfg["boots"], robe)
    up = []
    neck = Shape(SKIN, box(19, 29, 25, 34), box=(19, 29, 25, 34))
    t = torso(cfg["shirt"], robe)
    up += [neck, t]
    if job == "novice":
        # Tan vest over the shirt, open at the front, belt and a small pouch.
        up.append(Shape("#b8834e", poly([(12.5, 34), (15, 32), (19.5, 33), (19, 47), (14.5, 47)]), box=(12, 32, 20, 48)))
        up.append(Shape("#b8834e", poly([(31.5, 34), (29, 32), (24.5, 33), (25, 47), (29.5, 47)]), box=(24, 32, 32, 48)))
        up.append(Shape("#5e3d26", box(14, 46, 30, 49), box=(14, 46, 30, 49)))
        up.append(Shape("#e2c06a", box(20.5, 46, 23.5, 49), flat=True))
        up.append(Shape("#7a5232", ellipse(28.5, 50, 2.6, 2.4), box=(26, 48, 32, 53)))
    if job == "swordman":
        up.append(Shape("#b7c0cc", poly([(14, 34), (CX, 33), (30, 34), (28.5, 42), (CX, 44), (15.5, 42)]), box=(13, 32, 31, 45)))
        up.append(Shape("#4a3122", box(14, 46, 30, 49), box=(14, 46, 30, 49)))
        up.append(Shape("#e2c06a", box(20.5, 46, 23.5, 49), flat=True))
    if job == "mage":
        up.append(Shape("#e2c06a", box(20.6, 38, 22.4, 64), flat=True))
        up.append(Shape("#5c4c9c", poly(sym([(CX, 34), (16, 30), (14, 33), (17, 35)])), box=(13, 29, 31, 36)))
        up.append(Shape("#e2c06a", box(14, 45, 30, 46.4), flat=True))
    if job == "merchant":
        up.append(Shape("#a85a48", poly([(12.5, 34), (15, 32), (19, 33), (18.5, 47), (14.5, 47)]), box=(12, 32, 20, 48)))
        up.append(Shape("#a85a48", poly([(31.5, 34), (29, 32), (25, 33), (25.5, 47), (29.5, 47)]), box=(24, 32, 32, 48)))
        up.append(Shape("#d9734a", poly(sym([(CX, 37), (17.5, 31), (16.5, 33)])), box=(16, 30, 28, 38)))
        up.append(Shape("#5a3a24", box(14, 46, 30, 49), box=(14, 46, 30, 49)))
        lower.insert(0, Shape("#8a6a45", union(box(28, 44, 36, 54), ellipse(32, 44, 4, 2)), box=(28, 42, 36, 54)))
    if pose == "idle":
        arms_low, arms_high = arm_down(cfg["sleeve"]) + arm_down(cfg["sleeve"], True), []
    elif pose == "wave":
        arms_low, arms_high = arm_down(cfg["sleeve"]), arm_up(cfg["sleeve"], True)
    else:
        arms_low, arms_high = [], arm_up(cfg["sleeve"]) + arm_up(cfg["sleeve"], True)
    props = []
    if job == "swordman":
        # Sheathed sword at the left hip; pauldrons over the shoulders.
        props.append(Shape("#3e2a1e", poly([(9, 49), (11, 48), (6, 67), (4, 66)]), box=(4, 48, 11, 67)))
        props.append(Shape("#e2c06a", box(7.5, 45, 14, 47), flat=True))
        arms_low += []
        pads = [Shape("#b7c0cc", ellipse(12, 34.5, 4.2, 3.2), box=(8, 31, 16, 38))]
        pads.append(pads[0].mirrored())
        up_over = pads
    else:
        up_over = []
    if job == "mage":
        top = 26 if pose != "cheer" else 12
        sx = 8 if pose != "cheer" else 5
        staff = [Shape("#7a5236", box(sx, top, sx + 2, top + 44), box=(sx, top, sx + 2, top + 44)),
                 Shape("#8fd6ff", ellipse(sx + 1, top - 1.5, 2.6, 2.6), box=(sx - 2, top - 4, sx + 4, top + 1))]
        if pose == "cheer":
            arms_high = staff + arms_high
        else:
            props += staff
    shift = lambda items: [s.moved(0, dy) for s in items]
    return props + lower, shift(up) + shift(arms_low) + shift(up_over), shift(arms_high)


def head(job, cfg, look, dy):
    dx = -2 if look else 0
    behind, front = [], []
    if cfg["hair"] == "long":
        behind.append(hair_back_long(cfg["hc"]))
    ear = Shape(SKIN, union(ellipse(9.2 + dx * 0.5, 22, 1.8, 2.6), ellipse(33.8 + dx * 0.5, 22, 1.8, 2.6)), box=(7, 19, 37, 25))
    front += [ear, face_shape(dx)]
    if cfg["hair"] == "spiky":
        front.append(hair_spiky(cfg["hc"], dx // 2))
    elif cfg["hair"] == "long":
        front.append(hair_long(cfg["hc"], dx // 2))
    else:
        front += hair_bandana(cfg["hc"], cfg["band"], dx // 2)
    if job == "swordman":
        front.append(Shape("#c23a45", lambda x, y: 9 < x - dx // 2 < 35 and 9 <= y < 11.5, box=(9, 9, 35, 12)))
    feats = [(x, y + dy, c) for x, y, c in eyes(dx, cfg["iris"])]
    return [s.moved(0, dy) for s in behind], [s.moved(0, dy) for s in front], feats


def frame(job, cfg, pose, dy, look):
    img = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    px = img.load()
    behind_b, body_l, high = body(job, cfg, pose, dy)
    hb, hf, feats = head(job, cfg, -1 if look else 0, dy)
    for s in hb + behind_b + body_l:
        s.paint(px)
    h = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    hp = h.load()
    for s in hf:
        s.paint(hp)
    for x, y, c in feats:
        if 0 <= x < FW and 0 <= y < FH:
            hp[x, y] = c
    if look == 1:
        h = h.transpose(Image.FLIP_LEFT_RIGHT)
    img.alpha_composite(h)
    px = img.load()
    for s in high:
        s.paint(px)
    return img


def main():
    out = Path(__file__).resolve().parent.parent / "public" / "sprites"
    out.mkdir(parents=True, exist_ok=True)
    poses = [("idle", 0), ("idle", 1), ("wave", 0), ("cheer", 0)]
    for job, cfg in JOBS.items():
        sheet = Image.new("RGBA", (FW * COLS, FH * ROWS), (0, 0, 0, 0))
        for r, look in enumerate((0, -1, 1)):
            for c, (pose, dy) in enumerate(poses):
                sheet.alpha_composite(frame(job, cfg, pose, dy, look), (c * FW, r * FH))
        sheet.save(out / f"{job}.png", optimize=True)
        print("wrote", out / f"{job}.png")


if __name__ == "__main__":
    main()
