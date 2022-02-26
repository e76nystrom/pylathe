#!/cygdrive/c/Python39/Python.exe

# from PIL import Image, ImageFont, ImageDraw
from math import cos, sin, pi, radians

# r = 2556

# im = Image.new('RGB', (2*r, 2*r), 0)

# draw = ImageDraw.Draw(im)
# font = ImageFont.truetype("arial.ttf", 10, encoding="unic")
# draw.ellipse((0, 0, 2*r-1, 2*r-1), outline='red')
# draw.text((r, r), u"10", 'blue', font=font, align='center')
# r0 = r - 100
# for i in range(100):
#     a = radians((i / 100) * 360)
#     x0 = r0 * cos(a) + r
#     y0 = r0 * sin(a) + r
#     x1 = r * cos(a) + r
#     y1 = r * sin(a) + r
#     # print(i, x0, y0, x1, y1)
#     draw.line([(x0, y0), (x1, y1)], fill='blue')
# im.save("test.png", "PNG")

import math
import cairo

WIDTH, HEIGHT = 1024, 1024

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas

# pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
# pat.add_color_stop_rgba(1, 0.7, 0, 0, 0.5)  # First stop, 50% opacity
# pat.add_color_stop_rgba(0, 0.9, 0.7, 0.2, 1)  # Last stop, 100% opacity

# ctx.rectangle(0, 0, 1, 1)  # Rectangle(x0, y0, x1, y1)
# ctx.set_source(pat)
# ctx.fill()

ctx.set_font_size(0.05)
ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)

fontFace = ctx.get_font_face()

r = 0.5
r0 = 0.9 * r
rc = 0.99 * r
ctx.translate(r, r)  # Changing the current transformation matrix

ctx.move_to(rc, 0)

ctx.arc(0.0, 0.0, rc, 0.0, 2*pi)

for i in range(100):
    a = radians((i / 100) * 360) - pi/2
    if i % 10 == 0:
        r0 = 0.8 * r
        label = True
    else:
        rem = i % 5
        if rem == 0:
            r0 = 0.85 * r
        # elif (rem == 2) or (rem == 3):
        #     r0 = 0.85 * r
        else:
            r0 = 0.9 * r
    x0 = r0 * cos(a)
    y0 = r0 * sin(a)
    x1 = rc * cos(a)
    y1 = rc * sin(a)
    # print(i, x0, y0, x1, y1)
    ctx.move_to(x0, y0)
    ctx.line_to(x1, y1)
    if label:
        txt = str(i)
        extents = ctx.text_extents(txt)
        r1 = r0 - 0.01
        x0 = r1 * cos(a)
        y0 = r1 * sin(a)
        xOffset = 0
        yOffset = 0
        if i == 0:
            xOffset = -extents.x_advance / 2
            yOffset = extents.height
        elif i == 10:
            xOffset = -extents.x_advance
            yOffset = extents.height *.75
        elif i == 20:
            xOffset = -extents.x_advance
            yOffset = extents.height / 2
        elif i == 30:
            xOffset = -extents.x_advance
            yOffset = extents.height / 2
        elif i == 40:
            xOffset = -extents.x_advance
            yOffset = extents.height *.25
        elif i == 50:
            xOffset = -extents.x_advance / 2
        elif i == 60:
            yOffset = extents.height * .25
        elif i == 70:
            yOffset = extents.height / 2
        elif i == 80:
            yOffset = extents.height / 2
        elif i == 90:
            yOffset = extents.height *.75
        ctx.move_to(x0 + xOffset, y0 + yOffset)
        ctx.show_text(str(i))
        label = False

ctx.set_source_rgb(0.3, 0.2, 0.5)  # Solid color
ctx.set_line_width(0.002)
ctx.stroke()

# # Arc(cx, cy, radius, start_angle, stop_angle)
# ctx.arc(0.2, 0.1, 0.1, -math.pi / 2, 0)
# ctx.line_to(0.5, 0.1)  # Line to (x,y)
# # Curve(x1, y1, x2, y2, x3, y3)
# ctx.curve_to(0.5, 0.2, 0.5, 0.4, 0.2, 0.8)
# ctx.close_path()

if False:
    ctx.arc(0, 0, 0.05 * r, 0, 2 * pi)
    ctx.fill()

    ctx.move_to(0, 0)
    ctx.line_to(0.75 * r, 0)
    ctx.set_source_rgb(1.0, 0.0, 0.0)
    ctx.set_line_width(0.01)
    ctx.stroke()

    ctx.move_to(0.75 * r, 0)
    ctx.line_to(0.95 * r, 0)
    ctx.set_source_rgb(1.0, 0.0, 0.0)
    ctx.set_line_width(0.002)
    ctx.stroke()

surface.write_to_png("example.png")  # Output to PNG
