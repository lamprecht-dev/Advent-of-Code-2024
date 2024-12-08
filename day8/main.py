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


def inbound(node, grid):
    if node[0] < 0 or node[1] < 0 or node[0] >= len(grid[0]) or node[1] >= len(grid): return False
    return True


def addChain(dx, dy, part, origin, ll, anitnodes, d = 1):
    i = 1
    while True:
        if i > 1 and part == 1:
            break
        n = (origin[0] + dx * i * d, origin[1] + dy * i * d)
        if not inbound(n, ll):
            break
        anitnodes.add(n)
        i+=1
    return anitnodes


def s(d, part):
    signals = {}
    anitnodes = set()
    ll = lines(d)
    for y in range(len(ll)):
        line = ll[y]
        for x in range(len(line)):
            if line[x] == ".":
                continue
            if line[x] not in signals:
                signals[line[x]] = []
            signals[line[x]].append((x, y))
            if part == 2:
                anitnodes.add((x, y))

    for s in signals:
        for s1 in range(len(signals[s])):
            for s2 in range(s1 + 1, len(signals[s])):
                dx, dy = signals[s][s1][0] - signals[s][s2][0], signals[s][s1][1] - signals[s][s2][1]
                anitnodes = addChain(dx, dy, part, signals[s][s1], ll, anitnodes)
                anitnodes = addChain(dx, dy, part, signals[s][s2], ll, anitnodes, -1)

    return len(anitnodes)


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
    example = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
    a1 = 14
    a2 = 34
    return validate_solution((s(example, 1), s(example, 2)), (a1, a2))


main()
