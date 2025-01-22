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


def best_cheats(paths, path_vals, s, e, max_diff):
    over_100 = 0
    for p in paths:
        for p2 in paths:
            if p == p2 or path_vals[p] > path_vals[p2]:
                continue
            dist = abs(p[0] - p2[0]) + abs(p[1] - p2[1])
            if dist > max_diff:
                continue
            val_diff = abs(path_vals[p] - path_vals[p2])
            total_diff = val_diff - dist
            
            if total_diff >= 100:
                over_100 += 1

    return over_100


def s(d, part):
    path_vals = {}
    paths = set()
    s, e = (0, 0), (0, 0)

    ll = lines(d)
    for y, line in enumerate(ll):
        for x, c in enumerate(line):
            if c == ".":
                path_vals[(x, y)] = -math.inf
                paths.add((x, y))
            elif c == "E":
                e = (x, y)
                path_vals[(x, y)] = -math.inf
                paths.add((x, y))
            elif c == "S":
                s = (x, y)
                path_vals[(x, y)] = 0
                paths.add((x, y))

    dfs = [s]
    seen = set()
    while len(dfs) > 0:
        cur = dfs.pop()
        for dd in dirs:
            d = (dirs[dd][0] + cur[0], dirs[dd][1] + cur[1])
            if d in paths and d not in seen:
                dfs.append(d)
                path_vals[d] = path_vals[(cur[0], cur[1])] + 1
        seen.add(cur)
    
    return best_cheats(paths, path_vals, s, e, 2 if part == 1 else 20)

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
    example = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
    a1 = 0
    a2 = 0
    return validate_solution((s(example, 1), s(example, 2)), (a1, a2))


main()
