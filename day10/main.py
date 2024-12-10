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


def s(d, part):
    g = []
    trailheads = []
    ll = lines(d)
    w, h = len(ll[0]), len(ll)
    for y in range(len(ll)):
        row = []
        for x in range(len(ll[y])):
            row.append(int(ll[y][x]))
            if ll[y][x] == "0":  
                trailheads.append((x, y))
        g.append(row)

    score = 0
    for th in trailheads:
        seen = []
        queue = collections.deque([(th[0], th[1], 0)])
        foundTHEnd = set()
        while len(queue) > 0:
            cur = queue.popleft()
            seen.append(cur)
            for di in dirs:
                d = dirs[di]
                dx, dy = cur[0] + d[0], cur[1] + d[1]
                if dx < 0 or dy < 0 or dx >= w or dy >= h or g[dy][dx] != cur[2] + 1:
                    continue
                nex = (dx, dy, cur[2] + 1)
                if nex in seen and part == 1:
                    continue
                if nex[2] == 9:
                    if part == 1:
                        foundTHEnd.add((dx, dy))
                    else:
                        score += 1
                else:
                    queue.append(nex)
        if part == 1:
            score += len(foundTHEnd)

    return score


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
    example = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
    a1 = 36
    a2 = 81
    return validate_solution((s(example, 1), s(example, 2)), (a1, a2))


main()
