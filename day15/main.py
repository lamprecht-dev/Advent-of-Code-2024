import sys
import collections
import datetime
import itertools
import functools
import math
from operator import itemgetter as ig
import pprint as pp
import re
# import bisect
# import heapq
# sys.setrecursionlimit(1000000)

sys.path.append('../')
from utils import *


def get_next_position(f, t):
    x1, y1 = f
    x2, y2 = t

    return (x2 + (x2 - x1), y2) if x1 == x2 else (x2, y2 + (y2 - y1))

def s(d, part):
    if part == 2:
        return 0

    walls, boxes = set(), set()
    pos = (0, 0)
    map, inst = d.split("\n\n")
    data = map.split("\n")
    h, w = len(data), len(data[0])
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == "#":
                walls.add((x, y))
            elif c == "O":
                boxes.add((x, y))
            elif c == "@":
                pos = (x, y)

    def attemptMove(f, t, isRobot=False):
        if t[0] < 0 or t[1] < 0 or t[0] >= w or t[1] >= h or t in walls:
            return False

        if t in boxes:
            attemptMove(t, )

        attemptMove()

        return True

    for i in inst:
        if i == "^":
            nx, ny = pos[0], pos[1] - 1
            d = "u"
        elif i == "v":
            nx, ny = pos[0], pos[1] + 1
            d = "d"
        elif i == "<":
            nx, ny = pos[0] - 1, pos[1]
            d = "l"
        elif i == ">":
            nx, ny = pos[0] + 1, pos[1]
            d = "r"

        attemptMove(pos, (nx, ny), True)


    return 0


def main():
    if test():
        file = inp(os.path.join(os.path.dirname(__file__), 'input.txt'))
        solutions = (s(file, 1), s(file, 2))
        print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
        for sol in solutions:
            print(sol)
    else:
        print("\n\n" + BColors.FAIL + "Not All Test Successful" + BColors.ENDC)


def test():
    example = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""
    example2 = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
    a1 = 2028
    a2 = 10092
    return validate_solution((s(example, 1), s(example2, 1)), (a1, a2))


main()
