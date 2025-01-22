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


def opposite(a):
    if a == "u":
        return "d"
    if a == "d":
        return "u"
    if a == "l":
        return "r"
    if a == "r":
        return "l"

    return None


def sort_by_score(a, b):
    if a[3] == b[3]:
        return 0
    if a[3] < b[3]:
        return 1
    return -1

def s(d, part):
    paths = {}
    s, e = None, None

    for y, line in enumerate(lines(d)):
        for x, c in enumerate(line):
            if c != "#":
                paths[(x, y, "r")] = (math.inf, []) # I want to store the origins
                paths[(x, y, "d")] = (math.inf, [])
                paths[(x, y, "l")] = (math.inf, [])
                paths[(x, y, "u")] = (math.inf, [])
            if c == "E":
                e = (x, y)
            elif c == "S":
                s = (x, y, "r", 0)
                paths[(x, y, "r")] = (0, [])

    dnext = [s]

    while len(dnext) > 0:
        dnext = sorted(dnext, key=functools.cmp_to_key(sort_by_score))
        cur = dnext.pop()
        for dd in dirs:
            dx = dirs[dd][0] + cur[0]
            dy = dirs[dd][1] + cur[1]

            if dd == cur[2]:
                # MOVE
                if (dx, dy, dd) not in paths:
                    continue
                
                # Check if this is the quickest way to the path
                ns = cur[3] + 1
                if paths[(dx, dy, dd)][0] == ns:
                    # no need to add a search as its equal distance but we want to add history
                    paths[(dx, dy, dd)][1].append((cur[0], cur[1], cur[2]))
                elif paths[(dx, dy, dd)][0] > ns:
                    paths[(dx, dy, dd)] = (ns, [(cur[0], cur[1], cur[2])])
                    dnext.append((dx, dy, dd, ns))
            else:
                # TURN
                ns = cur[3] + 1000
                if cur[2] == opposite(dd):
                    ns += 1000

                if paths[(cur[0], cur[1], dd)][0] == ns:
                    # no need to add a search as its equal distance but we want to add history
                    paths[(cur[0], cur[1], dd)][1].append((cur[0], cur[1], cur[2]))
                elif paths[(cur[0], cur[1], dd)][0] > ns:
                    paths[(cur[0], cur[1], dd)] = (ns, [(cur[0], cur[1], cur[2])])
                    dnext.append((cur[0], cur[1], dd, ns))
    
    min_val = math.inf
    min_dir = None
    for dd in dirs:
        dval = paths[(e[0], e[1], dd)][0]
        if dval < min_val:
            min_val = dval
            min_dir = dd

    if part == 1:
        return min_val
    
    shortest_paths = set()
    next_on_paths = [(e[0], e[1], min_dir)]
    while len(next_on_paths) > 0:
        cur = next_on_paths.pop()
        shortest_paths.add((cur[0], cur[1]))
        next_on_paths.extend(paths[cur][1])
    
    return len(shortest_paths)


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
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""
    example2 = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""
    a1 = 7036
    a2 = 64
    return validate_solution((s(example, 1), s(example2, 2)), (a1, a2))


main()
