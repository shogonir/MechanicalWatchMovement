#! /usr/bin/env python
# -+- coding:utf-8 -*-


import os
import math
from PIL import Image, ImageDraw


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

groove_height = 0.01
kana_radius = 0.01


class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, coef):
        return Point(self.x * coef, self.y * coef)

    def __str__(self):
        return 'Point({0:8.4f}, {1:8.4f})'.format(self.x, self.y)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


class Circle:

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


class Gear:
    
    def __init__(self, name, num_tooth, num_kana_tooth, circle):
        self.name = name
        self.num_tooth = num_tooth
        self.num_kana_tooth = num_kana_tooth
        self.circle = circle

    def __str__(self):
        return """
        Gear
            name           : {0}
            num_tooth      : {1}
            kana_num_tooth : {2}
            outer_radius   : {3:9.6f}
            inner_radius   : {4:9.6f}
            hole_radius    : {5:9.6f}
            center         : {6}
        """.format(self.name, self.num_tooth, self.num_kana_tooth,
            self.circle.radius + groove_height,
            self.circle.radius,
            self.circle.radius - (groove_height * 2),
            self.circle.center)

    def command(self):
        index = self.name.find('(')
        name = self.name if index == -1 else self.name[:index]
        command = 'python gear.py {0} {1} {2} {3} {4}\n'.format(
            name, self.num_tooth, self.circle.radius,
            self.circle.radius - (groove_height * 2),
            self.circle.radius + groove_height)
        if self.num_kana_tooth != 0:
            command += 'python gear.py {0} {1} {2} {3} {4}\n'.format(
                name + '_kana', self.num_kana_tooth, kana_radius,
                0.0, kana_radius + groove_height)
        return command


def draw_circle(draw, side, center, radius, fill_color=None, outline_color=WHITE):
    offset = Point(0.5, 0.5)
    left_top = (offset + center - Point(radius, radius)) * side
    right_bottom = (offset + center + Point(radius, radius)) * side
    coords = (left_top.x, left_top.y, right_bottom.x, right_bottom.y)
    draw.ellipse(coords, outline=outline_color)


if __name__ == '__main__':
    
    side = 512

    image = Image.new('RGB', (side + 1, side + 1), WHITE)
    draw = ImageDraw.Draw(image)

    draw.line((side / 2, 0, side / 2, side), fill=BLACK, width=1)
    draw.line((0, side / 2, side, side / 2), fill=BLACK, width=1)

    radian = 30.0 / 180.0 * math.pi

    circle2 = Circle(Point(0, 0), 0.14)
    
    circle4 = Circle(Point(0, 0.25), 0.08)

    coef = circle2.radius + groove_height + kana_radius
    center3 = Point(-coef *  math.sin(radian), coef * math.cos(radian))
    radius3 = (circle4.center - center3).magnitude() - (kana_radius + groove_height)
    circle3 = Circle(center3, radius3)

    center_escape = circle4.center
    center_escape += Point(math.sqrt(3) / 2.0, 0.5) * (circle4.radius + groove_height * 2)
    radius_escape = 0.06
    escape = Circle(center_escape, radius_escape)

    barrel_radius = 0.18
    radian = 250 * math.pi / 180
    vector = Point(math.cos(radian), math.sin(radian))
    barrel_center = vector * (barrel_radius + groove_height + kana_radius)
    barrel = Circle(barrel_center, barrel_radius)

    hinoura_radius = 0.1
    radian = 0 * math.pi / 180
    vector = Point(math.cos(radian), math.sin(radian))
    hinoura_center = vector * (hinoura_radius + groove_height + kana_radius)
    hinoura = Circle(hinoura_center, hinoura_radius)

    tsutsu_radius = hinoura_radius
    tsutsu_center = Point(0, 0)
    tsutsu = Circle(tsutsu_center, tsutsu_radius)

    circles = [barrel, circle2, circle3, circle4, escape, hinoura, tsutsu]

    gear_barrel = Gear('barrel(koubako)', 72, 0, barrel)
    gear2 = Gear('second', 80, 12, circle2)
    gear3 = Gear('third', 75, 10, circle3)
    gear4 = Gear('fourth', 80, 18, circle4)
    gear_escape = Gear('escape(gangi)', 15, 8, escape)
    gear_hinoura = Gear('hionura', 30, 30, hinoura)
    gear_tsutsu = Gear('tsutsu', 120, 10, tsutsu)

    gears = [
        gear_barrel, 
        gear2,
        gear3,
        gear4,
        gear_escape,
        gear_hinoura,
        gear_tsutsu
    ]
    
    for gear in gears:
        print gear

    for gear in gears:
        print gear.command()

    # case
    draw_circle(draw, side, circle2.center, 0.5, outline_color=BLACK)

    # temp
    coef = 0.3
    radian = 30 * math.pi / 180
    temp_center = Point(coef * math.cos(radian), coef * math.sin(radian))
    draw_circle(draw, side, temp_center, 0.12, outline_color=BLACK)

    for c in circles:
        # kana
        draw_circle(draw, side, c.center, kana_radius, outline_color=RED)
        draw_circle(draw, side, c.center, kana_radius + groove_height, outline_color=BLUE)
        # gear
        draw_circle(draw, side, c.center, c.radius, outline_color=RED)
        draw_circle(draw, side, c.center, c.radius + groove_height, outline_color=BLUE)

    image.show()
    image.save('./movement.png')

