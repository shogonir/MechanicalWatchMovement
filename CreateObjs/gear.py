#! /usr/bin/env python
# -*- coding:utf-8 -*-

import math
import sys

if __name__ == '__main__':

    if len(sys.argv) < 5:
        print 'uncorrect number of system arguments'
        sys.exit(1)

    GEAR_NAME = sys.argv[1]
    NUM_TOOTH = int(sys.argv[2])
    OUTER_RADIUS = 0.5
    YS = [0.5, -0.5]
    INNER_RADIUS = float(sys.argv[3])
    MIDDLE_RAIUDS = ((OUTER_RADIUS - INNER_RADIUS) * 2.0 / 3.0) + INNER_RADIUS
    HOLE_RADIUS = float(sys.argv[4])

    print HOLE_RADIUS, INNER_RADIUS, MIDDLE_RAIUDS, OUTER_RADIUS

    if INNER_RADIUS > OUTER_RADIUS or HOLE_RADIUS > INNER_RADIUS:
        print 'uncorrect radius'
        sys.exit(1)

    with open('../Assets/Objs/gear_{0}.obj'.format(GEAR_NAME), 'w') as f:
        f.write('g gear_{0}\n'.format(GEAR_NAME))

        # 1. VERTICES

        # 1.1. HOLE VERTICES
        for y in YS:
            for i in range(1, NUM_TOOTH + 1):
                PREV_RADIAN = 2.0 * math.pi * (i - 1) / NUM_TOOTH
                CURR_RADIAN = 2.0 * math.pi * i / NUM_TOOTH
                MIDD_RADIAN = (PREV_RADIAN + CURR_RADIAN) / 2.0
                f.write('v {0:7.4f} {1:7.4f} {2:7.4f}\n'.format(
                    HOLE_RADIUS * math.cos(MIDD_RADIAN),
                    y,
                    HOLE_RADIUS * math.sin(MIDD_RADIAN)))
                f.write('v {0:7.4f} {1:7.4f} {2:7.4f}\n'.format(
                    HOLE_RADIUS * math.cos(CURR_RADIAN),
                    y,
                    HOLE_RADIUS * math.sin(CURR_RADIAN)))

        # 1.2. GEAR VERTICES
        for y in YS:
            for i in range(1, NUM_TOOTH + 1):
                PREV_RADIAN = 2.0 * math.pi * (i - 1) / NUM_TOOTH
                CURR_RADIAN = 2.0 * math.pi * i / NUM_TOOTH
                FIRST_RADIAN = ((CURR_RADIAN - PREV_RADIAN)
                                * 1.0 / 5.0) + PREV_RADIAN
                SECOND_RADIAN = ((CURR_RADIAN - PREV_RADIAN)
                                 * 3.0 / 10.0) + PREV_RADIAN
                THIRD_RADIAN = ((CURR_RADIAN - PREV_RADIAN)
                                * 2.0 / 5.0) + PREV_RADIAN
                FOURTH_RADIAN = ((CURR_RADIAN - PREV_RADIAN)
                                 * 3.0 / 5.0) + PREV_RADIAN
                FIFTH_RADIAN = ((CURR_RADIAN - PREV_RADIAN)
                                * 7.0 / 10.0) + PREV_RADIAN
                SIXTH_RADIAN = ((CURR_RADIAN - PREV_RADIAN)
                                * 4.0 / 5.0) + PREV_RADIAN
                f.write('v {0:7.4f} {1:7.4f} {2:7.4f}\n'.format(
                    INNER_RADIUS * math.cos(FIRST_RADIAN),
                    y,
                    INNER_RADIUS * math.sin(FIRST_RADIAN)))
                f.write('v {0:7.4f} {1:7.4f} {2:7.4f}\n'.format(
                    MIDDLE_RAIUDS * math.cos(SECOND_RADIAN),
                    y,
                    MIDDLE_RAIUDS * math.sin(SECOND_RADIAN)))
                f.write('v {0:7.4f} {1:7.4f} {2:7.4f}\n'.format(
                    OUTER_RADIUS * math.cos(THIRD_RADIAN),
                    y,
                    OUTER_RADIUS * math.sin(THIRD_RADIAN)))
                f.write('v {0:7.4f} {1:7.4f} {2:7.4f}\n'.format(
                    OUTER_RADIUS * math.cos(FOURTH_RADIAN),
                    y,
                    OUTER_RADIUS * math.sin(FOURTH_RADIAN)))
                f.write('v {0:7.4f} {1:7.4f} {2:7.4f}\n'.format(
                    MIDDLE_RAIUDS * math.cos(FIFTH_RADIAN),
                    y,
                    MIDDLE_RAIUDS * math.sin(FIFTH_RADIAN)))
                f.write('v {0:7.4f} {1:7.4f} {2:7.4f}\n'.format(
                    INNER_RADIUS * math.cos(SIXTH_RADIAN),
                    y,
                    INNER_RADIUS * math.sin(SIXTH_RADIAN)))
                f.write('v {0:7.4f} {1:7.4f} {2:7.4f}\n'.format(
                    INNER_RADIUS * math.cos(CURR_RADIAN),
                    y,
                    INNER_RADIUS * math.sin(CURR_RADIAN)))

        # 2. FACES

        # 2.1. TOP FACES
        for i in range(1, NUM_TOOTH + 1):
            NT2 = NUM_TOOTH * 2
            NT4 = NUM_TOOTH * 4
            NT7 = NUM_TOOTH * 7
            I7 = i * 7
            I2 = i * 2
            for j in range(6):
                f.write('f {0:3d} {1:3d} {2:3d}\n'.format(
                    I2 - 1, NT4 + I7 - 5 + j, NT4 + I7 - 6 + j))
            f.write('f {0:3d} {1:3d} {2:3d}\n'.format(
                I2 - 1, I2, NT4 + I7))
            if i != NUM_TOOTH:
                f.write('f {0:3d} {1:3d} {2:3d}\n'.format(
                    I2, NT4 + I7 + 1, NT4 + I7 - 0))
                f.write('f {0:3d} {1:3d} {2:3d}\n'.format(
                    I2, I2 + 1, NT4 + I7 + 1))
        f.write('f {0:3d} {1:3d} {2:3d}\n'.format(NT2, 1, NT4 + 1))
        f.write('f {0:3d} {1:3d} {2:3d}\n'.format(NT2, NT4 + 1, NT4 + NT7))

        # 2.2. HOLE WALLS
        for i in range(1, NUM_TOOTH + 1):
            I2 = i * 2
            NT2 = NUM_TOOTH * 2
            NT4 = NUM_TOOTH * 4
            f.write('f {0:3d} {1:3d} {2:3d}\n'.format(
                NT2 + I2 - 1, I2, I2 - 1))
            f.write('f {0:3d} {1:3d} {2:3d}\n'.format(
                NT2 + I2 - 1, NT2 + I2, I2))
            if i != NUM_TOOTH:
                f.write('f {0:3d} {1:3d} {2:3d}\n'.format(
                    NT2 + I2, I2 + 1, I2))
                f.write('f {0:3d} {1:3d} {2:3d}\n'.format(
                    NT2 + I2, NT2 + I2 + 1, I2 + 1))
        f.write('f {0:3d} {1:3d} {2:3d}\n'.format(NT4, 1, NT2))
        f.write('f {0:3d} {1:3d} {2:3d}\n'.format(NT4, NT2 + 1, 1))

        # 2.3. OUTER WALLS
        for i in range(1, NUM_TOOTH + 1):
            NT4 = NUM_TOOTH * 4
            NT7 = NUM_TOOTH * 7
            NT11 = NT4 + NT7
            NT18 = NT11 + NT7
            I7 = i * 7
            for j in range(7):
                if j != 6 or i != NUM_TOOTH:
                    f.write('f {0:3d} {1:3d} {2:3d}\n'.format(
                        NT11 + I7 - 5 + j, NT4 + I7 - 6 + j, NT4 + I7 - 5 + j))
                    f.write('f {0:3d} {1:3d} {2:3d}\n'.format(
                        NT11 + I7 - 5 + j, NT11 + I7 - 6 + j, NT4 + I7 - 6 + j))
        f.write('f {0:3d} {1:3d} {2:3d}\n'.format(NT11 + 1, NT11, NT4 + 1))
        f.write('f {0:3d} {1:3d} {2:3d}\n'.format(NT11 + 1, NT18, NT11))

        # 2.4. BOTTOM FACES
        for i in range(1, NUM_TOOTH + 1):
            NT2 = NUM_TOOTH * 2
            NT4 = NUM_TOOTH * 4
            NT11 = NUM_TOOTH * 11
            NT18 = NUM_TOOTH * 18
            I7 = i * 7
            I2 = i * 2
            for j in range(6):
                f.write('f {0:3d} {1:3d} {2:3d}\n'.format(
                    NT2 + I2 - 1, NT11 + I7 - 6 + j, NT11 + I7 - 5 + j))
            f.write('f {0:3d} {1:3d} {2:3d}\n'.format(
                NT2 + I2 - 1, NT11 + I7, NT2 + I2))
            if i != NUM_TOOTH:
                f.write('f {0:3d} {1:3d} {2:3d}\n'.format(
                    NT2 + I2, NT11 + I7, NT11 + I7 + 1))
                f.write('f {0:3d} {1:3d} {2:3d}\n'.format(
                    NT2 + I2, NT11 + I7 + 1, NT2 + I2 + 1))
        f.write('f {0:3d} {1:3d} {2:3d}\n'.format(NT4, NT11 + 1, NT2 + 1))
        f.write('f {0:3d} {1:3d} {2:3d}\n'.format(NT4, NT18, NT11 + 1))
