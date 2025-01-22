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


# For the second part I can imagine a connected GRAPH! Each time we add a byte we update the graph and cut connections
# The moment this cannot be represented in a single graph its over

def s(d, part, test = False):
    if part == 2:
        return 0

    bits = set()

    ll = lines(d)
    for row, line in enumerate(ll):
        if row == 1024 and test == False or (row == 12 and test == True):
            break
        bits.add(tuple(ints(line, ",")))

    s = (0, 0, 0)
    e = (70, 70)
    if test:
        e = (6, 6)

    bfs = collections.deque([s])
    seen = set()
    while len(bfs) > 0:
        cur = bfs.popleft()
        print(cur)
        if (cur[0] == e[0] and cur[1] == e[1]):
            return cur[2]

        for dd in dirs:
            d = (dirs[dd][0] + cur[0], dirs[dd][1] + cur[1])
            if e[0] < d[0] or d[0] < 0 or e[1] < d[1] or d[1] < 0:
                continue
            if d in seen or d in bits:
                continue

            bfs.append((d[0], d[1], cur[2] + 1))
            seen.add(d)


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
    example = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""
    a1 = 22
    a2 = None
    return validate_solution((s(example, 1, True), s(example, 2, True)), (a1, a2))


main()
