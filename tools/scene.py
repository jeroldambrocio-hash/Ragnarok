"""War of Emperium night siege for the hero, as pixel art drawn from code.

Run:  python3 tools/scene.py      (needs Pillow)
Writes public/scene/*.png at 480x270 (shown at 4x with pixelated scaling):
  sky.png    moon, stars, dithered night sky (opaque)
  far.png    distant moonlit mountains
  castle.png the castle on its hill: stone walls, round towers, red cone roofs,
             banners, a burning gate, siege ladders and smoke
  mid.png    the near slope with the road and the attacking army's torches
  ground.png a 120x24 tile for the foreground ridge the guides stand on
  emperium.png the golden Emperium on its pedestal, for the WoE section (72x96)
Each layer is a separate plane so the page can parallax them.
"""
import math
import random
from pathlib import Path
from PIL import Image

W, H = 480, 270
OUT = Path(__file__).resolve().parent.parent / "public" / "scene"
BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def hexc(s, a=255):
    s = s.lstrip("#")
    return (int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16), a)


def mix(a, b, k):
    return tuple(round(a[i] + (b[i] - a[i]) * k) for i in range(3)) + (a[3],)


def dith(x, y, k):
    """Ordered dither: True when the pixel should take the next tone."""
    return k * 16 > BAYER[y % 4][x % 4] + 0.5


class Layer:
    def __init__(self, w=W, h=H, fill=(0, 0, 0, 0)):
        self.w, self.h = w, h
        self.img = Image.new("RGBA", (w, h), fill)
        self.px = self.img.load()

    def set(self, x, y, c):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.px[x, y] = c

    def get(self, x, y):
        return self.px[x, y] if 0 <= x < self.w and 0 <= y < self.h else (0, 0, 0, 0)

    def rect(self, x0, y0, x1, y1, c):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                self.set(x, y, c)

    def save(self, name):
        OUT.mkdir(parents=True, exist_ok=True)
        self.img.save(OUT / name, optimize=True)


def ramp(stops, t):
    """Pick a colour from a list of (t, colour) stops with dithered steps."""
    for i in range(len(stops) - 1):
        t0, c0 = stops[i]
        t1, c1 = stops[i + 1]
        if t <= t1:
            return c0, c1, (t - t0) / (t1 - t0)
    return stops[-1][1], stops[-1][1], 0


# ---------------------------------------------------------------- sky
def sky():
    L = Layer(fill=hexc("#0a0b16"))
    stops = [(0, hexc("#07080f")), (0.35, hexc("#0d0f1f")), (0.62, hexc("#1a1428")),
             (0.8, hexc("#3a1a26")), (1, hexc("#5a2228"))]
    for y in range(H):
        for x in range(W):
            # Warm glow sits low behind the castle on the right.
            glow = max(0, 1 - math.hypot((x - 380) / 260, (y - 230) / 120))
            t = min(1, y / H * 0.85 + glow * 0.35)
            c0, c1, k = ramp(stops, t)
            # Quantise the blend into a few dithered bands.
            k = round(k * 3) / 3 if not dith(x, y, (k * 3) % 1) else math.ceil(k * 3) / 3
            L.set(x, y, mix(c0, c1, k))
    rnd = random.Random(7)
    for _ in range(170):
        x, y = rnd.randrange(W), rnd.randrange(int(H * 0.62))
        b = rnd.random()
        c = hexc("#f2ecd8") if b > 0.85 else hexc("#a9a6b8") if b > 0.5 else hexc("#5d5d78")
        L.set(x, y, c)
        if b > 0.95:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                L.set(x + dx, y + dy, hexc("#6d6a84"))
    # Moon with a dithered halo.
    mx, my, r = 236, 44, 12
    for y in range(my - 40, my + 41):
        for x in range(mx - 40, mx + 41):
            d = math.hypot(x - mx, y - my)
            if d <= r:
                c = hexc("#efe6c8")
                if (x - mx) + (y - my) > r * 0.55:
                    c = hexc("#d6caa6")
                for cx, cy, cr in ((mx - 4, my - 3, 3), (mx + 4, my + 4, 2), (mx + 1, my - 6, 1.5)):
                    if math.hypot(x - cx, y - cy) <= cr:
                        c = hexc("#cfc29e")
                L.set(x, y, c)
            elif d <= r + 26:
                k = 1 - (d - r) / 26
                if dith(x, y, k * 0.55):
                    L.set(x, y, mix(L.get(x, y), hexc("#4a4a66"), 0.6))
    return L


# ---------------------------------------------------------------- far mountains
def ridge(seed, base, amp, freq):
    rnd = random.Random(seed)
    ph = [rnd.random() * 6 for _ in range(3)]
    return [base - amp * (0.55 * math.sin(x * freq + ph[0]) + 0.3 * math.sin(x * freq * 2.3 + ph[1])
                          + 0.15 * math.sin(x * freq * 5.1 + ph[2])) for x in range(W)]


def far():
    L = Layer()
    for seed, base, amp, freq, col, rim in ((3, 172, 26, 0.018, "#171826", "#3a3d58"),
                                           (5, 196, 18, 0.026, "#11121c", "#2c2e44")):
        top = ridge(seed, base, amp, freq)
        for x in range(W):
            t = int(top[x])
            for y in range(t, H):
                L.set(x, y, hexc(col))
            # Moonlight catches the ridge line on slopes facing left.
            if x > 0 and top[x] < top[x - 1] + 0.4:
                L.set(x, t, hexc(rim))
    return L


# ---------------------------------------------------------------- castle
STONE = hexc("#6c6a7c")
STONE_L = hexc("#8e8b9e")
STONE_D = hexc("#474657")
STONE_DD = hexc("#2c2b3a")
ROOF = hexc("#8e2c36")
ROOF_L = hexc("#b8484a")
ROOF_D = hexc("#5a1c2a")
ROOF_DD = hexc("#361322")
LINE = hexc("#1c1622")


def stone_tone(x, x0, x1, y):
    """Cylinder-ish shading: moonlight from the left, dark on the right."""
    t = (x - x0) / max(1, x1 - x0)
    if t < 0.18:
        c = STONE_L
    elif t < 0.55:
        c = STONE
    elif t < 0.82:
        c = STONE_D if not dith(x, y, 0.5) or t > 0.7 else STONE
    else:
        c = STONE_DD
    return c


def bricks(L, x0, y0, x1, y1, flat=False):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            c = STONE if flat else stone_tone(x, x0, x1, y)
            if flat:
                c = STONE_D if (y - y0) % 2 else STONE
                c = mix(c, STONE_DD, 0.35)
            row = (y - y0) // 4
            if (y - y0) % 4 == 3 or ((x - x0 + (row % 2) * 4) % 8 == 0 and (y - y0) % 4 != 3):
                c = mix(c, LINE, 0.45)
            L.set(x, y, c)
    for y in range(y0, y1 + 1):
        L.set(x0, y, LINE)
        L.set(x1, y, LINE)


def merlons(L, x0, x1, y, step=6, w=4, h=4):
    for x in range(x0, x1 - w + 2, step):
        for yy in range(y - h, y):
            for xx in range(x, x + w):
                L.set(xx, yy, stone_tone(xx, x0, x1, yy))
        L.set(x - 1, y - 1, LINE)
        for xx in range(x, x + w):
            L.set(xx, y - h - 1, LINE)


def cone(L, cx, base, half, height):
    for y in range(base - height, base + 1):
        k = (y - (base - height)) / height
        hw = int(round(half * k))
        for x in range(cx - hw, cx + hw + 1):
            t = (x - (cx - hw)) / max(1, 2 * hw)
            c = ROOF_L if t < 0.22 else ROOF if t < 0.58 else ROOF_D if t < 0.85 else ROOF_DD
            if (base - y) % 5 == 0:
                c = mix(c, ROOF_DD, 0.5)
            L.set(x, y, c)
        L.set(cx - hw - 1, y, LINE)
        L.set(cx + hw + 1, y, LINE)
    for x in range(cx - half - 2, cx + half + 3):
        L.set(x, base + 1, ROOF_DD)


def tower(L, cx, top, base, half, roof_h, flag=True):
    bricks(L, cx - half, top, cx + half, base)
    merlons(L, cx - half, cx + half, top, step=5, w=3, h=3)
    cone(L, cx, top - 4, half + 3, roof_h)
    # Narrow lit window.
    for y in range(top + 8, top + 13):
        L.set(cx - 1, y, hexc("#ffcf6a"))
        L.set(cx, y, hexc("#e8913a"))
    if flag:
        py = top - 4 - roof_h
        for y in range(py - 10, py + 1):
            L.set(cx, y, LINE)
        for i, y in enumerate(range(py - 10, py - 5)):
            for x in range(cx + 1, cx + 8 - abs(i - 2)):
                L.set(x, y, ROOF_L if i < 2 else ROOF)


def flame(L, x, y, s=1.0, seed=0):
    rnd = random.Random(seed)
    h = int(9 * s)
    for j in range(h):
        k = j / h
        hw = max(0, int((1 - k) ** 0.8 * 3.2 * s + rnd.random() * 0.8))
        for i in range(-hw, hw + 1):
            d = abs(i) / (hw + 0.01)
            c = hexc("#fff2b0") if d < 0.3 and k < 0.6 else hexc("#ffc14a") if d < 0.65 else hexc("#e8642c")
            if k > 0.75:
                c = hexc("#c2382c")
            L.set(x + i + int(math.sin(j * 0.9 + seed) * 1.2 * k), y - j, c)


def smoke(L, x, y, h, seed):
    rnd = random.Random(seed)
    for j in range(h):
        k = j / h
        cx = x + math.sin(j * 0.08 + seed) * 6 * k + j * 0.12
        r = 3 + k * 14
        for yy in range(-1, 1):
            for xx in range(int(cx - r), int(cx + r) + 1):
                d = abs(xx - cx) / r
                a = (1 - d) * (1 - k) * 0.85
                if dith(xx, y - j, a) and L.get(xx, y - j)[3] == 0:
                    L.set(xx, y - j, hexc("#2a2230"))


def light(L, sources, strength=1.0):
    """Warm firelight on the stone, posterised into dithered steps."""
    warm = hexc("#ff9a4a")
    for y in range(L.h):
        for x in range(L.w):
            c = L.px[x, y]
            if c[3] == 0:
                continue
            a = 0
            for sx, sy, r in sources:
                d = math.hypot(x - sx, (y - sy) * 1.2)
                if d < r:
                    a = max(a, (1 - d / r) ** 1.6)
            if a <= 0:
                continue
            a *= strength
            steps = 4
            q = math.floor(a * steps) / steps + (1 / steps if dith(x, y, (a * steps) % 1) else 0)
            if q > 0:
                L.px[x, y] = mix(c, warm, min(0.62, q * 0.62))


def castle():
    L = Layer()
    # Hill the castle stands on.
    top = [210 - 34 * max(0, 1 - abs(x - 370) / 170) ** 0.6 for x in range(W)]
    for x in range(W):
        t = int(top[x])
        for y in range(t, H):
            c = hexc("#1d1a26")
            if y - t < 2:
                c = hexc("#3a3346")
            elif dith(x, y, 0.2) and y - t < 8:
                c = hexc("#28232f")
            L.set(x, y, c)
    base = 182
    # Back curtain wall and keep.
    bricks(L, 300, 140, 448, base, flat=True)
    merlons(L, 300, 448, 140)
    bricks(L, 340, 98, 404, base)
    merlons(L, 340, 404, 98)
    tower(L, 346, 86, 140, 7, 22)
    tower(L, 398, 86, 140, 7, 22)
    tower(L, 372, 64, 120, 9, 34)
    # Front wall with round towers.
    bricks(L, 284, 150, 462, base + 14)
    merlons(L, 284, 462, 150)
    tower(L, 284, 122, base + 16, 12, 30)
    tower(L, 462, 122, base + 16, 12, 30)
    tower(L, 328, 136, base + 14, 8, 20, flag=False)
    tower(L, 420, 136, base + 14, 8, 20, flag=False)
    # Gate: arch with a burning portcullis.
    gx, gy = 373, base + 14
    for y in range(gy - 22, gy + 1):
        for x in range(gx - 10, gx + 11):
            if y > gy - 14 or math.hypot(x - gx, y - (gy - 14)) <= 10:
                k = (y - (gy - 22)) / 22
                c = hexc("#ffd36b") if k > 0.65 else hexc("#f08a3a") if k > 0.3 else hexc("#b8402c")
                if (x - gx) % 4 == 0 or (y - gy) % 4 == 0:
                    c = hexc("#3a1a1a")
                L.set(x, y, c)
    for y in range(gy - 24, gy + 1):
        for x in range(gx - 12, gx + 13):
            if (y > gy - 14 and abs(x - gx) in (11, 12)) or (y <= gy - 14 and 10 < math.hypot(x - gx, y - (gy - 14)) <= 12):
                L.set(x, y, STONE_L if x < gx else STONE_D)
    # Hanging banners with a gold emblem.
    for bx in (306, 350, 396, 440):
        for y in range(156, 176):
            for x in range(bx, bx + 7):
                tip = y > 172 and abs(x - bx - 3) < (y - 172)
                if not tip:
                    L.set(x, y, ROOF_L if x == bx else ROOF if x < bx + 5 else ROOF_D)
        L.set(bx + 3, 162, hexc("#e8c46a"))
        L.set(bx + 2, 163, hexc("#e8c46a"))
        L.set(bx + 4, 163, hexc("#e8c46a"))
        L.set(bx + 3, 164, hexc("#c99a3a"))
        for x in range(bx - 1, bx + 8):
            L.set(x, 155, LINE)
    # Lit windows on the keep.
    for wx, wy in ((356, 110), (388, 110), (366, 124), (378, 124)):
        L.rect(wx, wy, wx + 1, wy + 3, hexc("#ffcf6a"))
        L.set(wx + 1, wy + 3, hexc("#e8913a"))
    # Siege ladders against the wall.
    for lx, top_y, lean in ((300, 150, -1), (444, 150, 1), (338, 150, -1)):
        for j in range(0, 48):
            y = top_y + j
            x = lx + lean * (j // 4)
            L.set(x - 2, y, hexc("#5a3a24"))
            L.set(x + 2, y, hexc("#3e2818"))
            if j % 4 == 0:
                for xx in range(x - 2, x + 3):
                    L.set(xx, y, hexc("#6b4a2e"))
    fires = [(290, 150, 1.4), (318, 150, 1.0), (432, 150, 1.6), (452, 150, 0.9),
             (346, 98, 0.9), (402, 98, 1.2), (373, base - 10, 1.8)]
    for i, (fx, fy, s) in enumerate(fires):
        flame(L, fx, fy, s, seed=i)
    smoke(L, 300, 128, 70, 1)
    smoke(L, 436, 128, 80, 2)
    smoke(L, 402, 84, 60, 3)
    light(L, [(fx, fy, 34 * s) for fx, fy, s in fires] + [(373, base + 6, 70)], 1.0)
    # Seat the whole castle a little lower so its spires clear the page header.
    low = Layer()
    low.img.paste(L.img.crop((0, 0, W, H - 12)), (0, 12))
    return low


# ---------------------------------------------------------------- mid slope and army
def mid():
    L = Layer()
    top = [236 - 22 * math.sin((x - 40) / 150) - 6 * math.sin(x / 37) for x in range(W)]
    for x in range(W):
        t = int(top[x])
        for y in range(t, H):
            c = hexc("#141219")
            if y - t < 1:
                c = hexc("#2c2632")
            L.set(x, y, c)
    # Road winding up toward the gate.
    road = []
    for j in range(120):
        k = j / 119
        x = 150 + k * 225 + math.sin(k * 7) * 12
        y = 268 - k * 82
        road.append((x, y))
        for i in range(-3, 4):
            if L.get(int(x + i), int(y))[3]:
                L.set(int(x + i), int(y), hexc("#2a2228") if abs(i) < 3 else hexc("#1c1820"))
    # Trebuchet silhouette on the left of the slope.
    tx, ty = 120, int(top[120])
    for j in range(26):
        L.set(tx - 8 + j // 3, ty - j, hexc("#0c0b10"))
        L.set(tx + 8 - j // 3, ty - j, hexc("#0c0b10"))
    for j in range(40):
        L.set(tx - 18 + j, ty - 26 - int(j * 0.45), hexc("#0c0b10"))
    L.rect(tx - 14, ty - 4, tx + 14, ty - 1, hexc("#0c0b10"))
    # Torches in war-bands along the road.
    rnd = random.Random(11)
    for band in (0.08, 0.3, 0.52, 0.74):
        for _ in range(9):
            k = band + (rnd.random() - 0.5) * 0.1
            x, y = road[int(max(0, min(119, k * 119)))]
            x += rnd.randint(-9, 9)
            y += rnd.randint(-3, 3)
            for yy in range(-4, 5):
                for xx in range(-4, 5):
                    d = math.hypot(xx, yy)
                    if d < 4.5 and dith(int(x + xx), int(y + yy), (1 - d / 4.5) * 0.7):
                        if L.get(int(x + xx), int(y + yy))[3]:
                            L.set(int(x + xx), int(y + yy), hexc("#7a3a26"))
            L.set(int(x), int(y), hexc("#ffe08a"))
            L.set(int(x), int(y) - 1, hexc("#ff9a3a"))
            L.set(int(x), int(y) + 1, hexc("#3a2016"))
            L.set(int(x), int(y) + 2, hexc("#3a2016"))
    return L


# ---------------------------------------------------------------- ground tile
def ground():
    L = Layer(120, 24)
    rnd = random.Random(4)
    for x in range(120):
        t = 6 + int(2 * math.sin(x / 9) + math.sin(x / 3.1))
        for y in range(t, 24):
            c = hexc("#0b0c0f")
            if y == t:
                c = hexc("#5e3c26")
            elif y == t + 1:
                c = hexc("#2a1c1a")
            L.set(x, y, c)
        if rnd.random() < 0.35:
            h = rnd.randint(1, 3)
            for j in range(1, h + 1):
                L.set(x, t - j, hexc("#3a2a24") if j == h else hexc("#1c1416"))
    return L


# ---------------------------------------------------------------- emperium
def emperium():
    L = Layer(72, 96)
    cx, top, mid_y, bot, hw = 36, 8, 40, 70, 15

    def inside(x, y):
        if y < top or y > bot:
            return False
        if y <= mid_y:
            return abs(x - cx) <= hw * (y - top) / (mid_y - top)
        return abs(x - cx) <= hw * (bot - y) / (bot - mid_y)

    # Soft dithered halo.
    for y in range(96):
        for x in range(72):
            d = math.hypot((x - cx) / 30, (y - mid_y) / 38)
            if d < 1 and dith(x, y, (1 - d) * 0.5):
                L.set(x, y, hexc("#5a4420"))
    gold = [hexc("#fff6c8"), hexc("#ffe07a"), hexc("#f2b63e"), hexc("#c27c22"), hexc("#7a4612")]
    for y in range(top, bot + 1):
        for x in range(cx - hw, cx + hw + 1):
            if not inside(x, y):
                continue
            upper = y <= mid_y
            left = x < cx
            # Four facets lit from the top left, plus an inner facet line.
            i = (0 if left else 2) if upper else (1 if left else 3)
            if abs(x - (cx - 4 if upper else cx + 3)) < 1 and 12 < y < 64:
                i = max(0, i - 1)
            if not inside(x - 1, y) or not inside(x + 1, y) or not inside(x, y - 1) or not inside(x, y + 1):
                i = 4
            L.set(x, y, gold[i])
    for sx, sy in ((cx - 7, 24), (cx - 9, 30), (cx + 2, 52)):
        L.set(sx, sy, gold[0])
    for sx, sy, r in ((12, 18, 2), (60, 30, 2), (56, 12, 1), (14, 56, 1)):
        for k in range(-r, r + 1):
            L.set(sx + k, sy, hexc("#fff2b0"))
            L.set(sx, sy + k, hexc("#fff2b0"))
    # Stone pedestal.
    for y in range(76, 92):
        w = 14 if y < 80 else 18 if y < 88 else 22
        for x in range(cx - w, cx + w):
            t = (x - (cx - w)) / (2 * w)
            c = hexc("#8e8b9e") if t < 0.2 else hexc("#6c6a7c") if t < 0.65 else hexc("#474657")
            if y in (79, 87) or x in (cx - w, cx + w - 1):
                c = LINE
            L.set(x, y, c)
    return L


if __name__ == "__main__":
    # The hero now uses the owner's plaza illustration; only the Emperium ships.
    # The siege layers above stay available: call sky(), far(), castle(), mid(), ground().
    emperium().save("emperium.png")
    print("wrote", OUT / "emperium.png")
