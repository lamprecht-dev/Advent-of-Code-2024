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
    if part == 2:
        return 0

    units = d.split("\n\n")
    keys, locks = [], []
    height = len(units[0].split("\n")) - 2
    for u in units:
        lines = u.split("\n")
        if lines[0][0] == "#": # lock
            locks.append([x.count("#") - 1 for x in zip(*lines)])
        else:                   # key
            keys.append([x.count("#") - 1 for x in zip(*lines)])
    
    fits = 0
    for k in keys:
        for l in locks:
            test_overlap = [l[i] + k[i] for i in range(len(l))]
            if max(test_overlap) <= 5:
                fits += 1

    return fits


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
    example = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""
    a1 = 3
    a2 = None
    return validate_solution((s(example, 1), s(example, 2)), (a1, a2))


main()
