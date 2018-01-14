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
    INNER_RADIUS = float(sys.argv[3])
    MIDDLE_RAIUDS = (OUTER_RADIUS - INNER_RADIUS * 2.0 / 3.0) + INNER_RADIUS
    HOLE_RADIUS = float(sys.argv[4])

    if INNER_RADIUS > OUTER_RADIUS or HOLE_RADIUS > INNER_RADIUS:
        print 'uncorrect radius'
        sys.exit(1)

    with open('../Assets/Objs/gear_{0}.obj'.format(GEAR_NAME), 'w') as f:
        f.write('g gear_{0}\n'.format(GEAR_NAME))

        # 1. VERTICES

        # 1.1. HOLE VERTICES
        for i in range(1, NUM_TOOTH + 1):
            PREV_RADIAN = 2.0 * math.pi * (i - 1) / NUM_TOOTH
            CURR_RADIAN = 2.0 * math.pi * i / NUM_TOOTH
            MIDD_RADIAN = (PREV_RADIAN + CURR_RADIAN) / 2.0
            f.write('v {0:7.4f} {1:7.4f} {2:7.4f}\n'.format(
                HOLE_RADIUS * math.cos(MIDD_RADIAN),
                0.0,
                HOLE_RADIUS * math.sin(MIDD_RADIAN)))
            f.write('v {0:7.4f} {1:7.4f} {2:7.4f}\n'.format(
                HOLE_RADIUS * math.cos(CURR_RADIAN),
                0.0,
                HOLE_RADIUS * math.sin(CURR_RADIAN)))

        # 1.2. GEAR VERTICES
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
                0.0,
                INNER_RADIUS * math.sin(FIRST_RADIAN)))
            f.write('v {0:7.4f} {1:7.4f} {2:7.4f}\n'.format(
                MIDDLE_RAIUDS * math.cos(SECOND_RADIAN),
                0.0,
                MIDDLE_RAIUDS * math.sin(SECOND_RADIAN)))
            f.write('v {0:7.4f} {1:7.4f} {2:7.4f}\n'.format(
                OUTER_RADIUS * math.cos(THIRD_RADIAN),
                0.0,
                OUTER_RADIUS * math.sin(THIRD_RADIAN)))
            f.write('v {0:7.4f} {1:7.4f} {2:7.4f}\n'.format(
                OUTER_RADIUS * math.cos(FOURTH_RADIAN),
                0.0,
                OUTER_RADIUS * math.sin(FOURTH_RADIAN)))
            f.write('v {0:7.4f} {1:7.4f} {2:7.4f}\n'.format(
                MIDDLE_RAIUDS * math.cos(FIFTH_RADIAN),
                0.0,
                MIDDLE_RAIUDS * math.sin(FIFTH_RADIAN)))
            f.write('v {0:7.4f} {1:7.4f} {2:7.4f}\n'.format(
                INNER_RADIUS * math.cos(SIXTH_RADIAN),
                0.0,
                INNER_RADIUS * math.sin(SIXTH_RADIAN)))

        # 2. FACES
