#!/usr/bin/env python3
"""Rebuild the text-free reusable template PNG assets."""

from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

TRANSPARENT = (0, 0, 0, 0)
GRID_BG = (227, 227, 227, 255)
GRID_LINE = (245, 245, 245, 255)
BLUE = (131, 165, 194, 255)
BLUE_DARK = (83, 121, 156, 255)
BLUE_LIGHT = (198, 225, 245, 255)
BLUE_ACCENT = (158, 207, 241, 255)
PEACH = (255, 220, 201, 255)
BLACK = (20, 20, 20, 255)
WHITE = (255, 255, 255, 255)


def draw_grid(draw: ImageDraw.ImageDraw, width: int, height: int, step: int) -> None:
    for x in range(0, width + 1, step):
        draw.line((x, 0, x, height), fill=GRID_LINE, width=1)
    for y in range(0, height + 1, step):
        draw.line((0, y, width, y), fill=GRID_LINE, width=1)


def ellipse_hatching(
    image: Image.Image,
    box: tuple[int, int, int, int],
    color: tuple[int, int, int, int],
    spacing: int = 7,
    line_width: int = 2,
) -> None:
    x0, y0, x1, y1 = box
    width, height = x1 - x0, y1 - y0
    hatch = Image.new("RGBA", (width, height), TRANSPARENT)
    hatch_draw = ImageDraw.Draw(hatch)
    for start in range(-height, width + height, spacing):
        hatch_draw.line((start, height, start + height, 0), fill=color, width=line_width)
    mask = Image.new("L", (width, height), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, width - 1, height - 1), fill=255)
    image.alpha_composite(Image.composite(hatch, Image.new("RGBA", hatch.size, TRANSPARENT), mask), (x0, y0))


def four_point_star(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    radius: int,
    fill: tuple[int, int, int, int],
    outline: tuple[int, int, int, int] = BLACK,
    outline_width: int = 3,
) -> None:
    cx, cy = center
    inner = max(3, radius // 5)
    points = [
        (cx, cy - radius),
        (cx + inner, cy - inner),
        (cx + radius, cy),
        (cx + inner, cy + inner),
        (cx, cy + radius),
        (cx - inner, cy + inner),
        (cx - radius, cy),
        (cx - inner, cy - inner),
    ]
    draw.polygon(points, fill=fill, outline=outline, width=outline_width)


def build_vertical() -> None:
    size = (1080, 1920)

    header = Image.new("RGBA", size, TRANSPARENT)
    draw = ImageDraw.Draw(header)
    draw.rectangle((0, 0, 1080, 204), fill=GRID_BG)
    grid_layer = Image.new("RGBA", (1080, 204), TRANSPARENT)
    draw_grid(ImageDraw.Draw(grid_layer), 1080, 204, 56)
    header.alpha_composite(grid_layer)

    draw.line(((37, 105), (244, 105), (278, 140)), fill=BLACK, width=2)
    draw.line(((278, 105), (1043, 105)), fill=BLACK, width=2)

    ellipse_hatching(header, (855, 82, 1018, 205), WHITE, spacing=6, line_width=2)
    draw.ellipse((944, 36, 1102, 194), fill=BLUE_ACCENT)
    draw.ellipse((978, 104, 1098, 198), fill=BLUE_LIGHT)
    four_point_star(draw, (84, 306), 55, PEACH, outline_width=3)
    four_point_star(draw, (160, 281), 27, PEACH, outline_width=3)

    band = Image.new("RGBA", size, TRANSPARENT)
    band_draw = ImageDraw.Draw(band)
    band_draw.polygon(((0, 1794), (1080, 1729), (1080, 1920), (0, 1920)), fill=BLUE)
    ellipse_hatching(band, (72, 1765, 305, 1900), WHITE, spacing=6, line_width=2)
    band_draw.ellipse((-55, 1688, 112, 1855), fill=BLUE_LIGHT)
    band_draw.ellipse((48, 1687, 129, 1820), fill=BLUE_ACCENT)

    full = Image.alpha_composite(header, band)
    header.save(ASSETS / "vertical-header.png", optimize=True)
    band.save(ASSETS / "vertical-subtitle-band.png", optimize=True)
    full.save(ASSETS / "vertical-full-overlay.png", optimize=True)


def build_cover() -> None:
    size = (1920, 1080)
    image = Image.new("RGBA", size, GRID_BG)
    draw = ImageDraw.Draw(image)
    draw_grid(draw, 1920, 1080, 64)

    ellipse_hatching(image, (1210, 32, 1780, 398), WHITE, spacing=7, line_width=2)
    draw.ellipse((1478, -78, 1842, 286), fill=BLUE)
    draw.ellipse((1490, 45, 1748, 286), fill=BLUE_LIGHT)

    ellipse_hatching(image, (164, 245, 600, 520), WHITE, spacing=7, line_width=2)
    draw.ellipse((-72, 405, 248, 748), fill=BLUE_LIGHT)
    draw.ellipse((-70, 405, 170, 748), fill=BLUE_ACCENT)
    four_point_star(draw, (115, 548), 48, PEACH, outline_width=3)
    four_point_star(draw, (178, 520), 24, PEACH, outline_width=3)

    for offset in range(5):
        y = 258 + offset * 31
        draw.line(((55, y), (78, y + 24)), fill=BLACK, width=3)

    for row in range(8):
        for col in range(5):
            cx = 1788 + col * 32
            cy = 196 + row * 32
            draw.ellipse((cx - 5, cy - 5, cx + 5, cy + 5), fill=PEACH)

    draw.polygon(((0, 935), (1920, 865), (1920, 1080), (0, 1080)), fill=BLUE)
    image.save(ASSETS / "cover-background.png", optimize=True)


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    build_vertical()
    build_cover()


if __name__ == "__main__":
    main()
