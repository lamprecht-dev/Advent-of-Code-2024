import sys
import collections as col
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

class Grid:
    def __init__(self, d):
        ll = lines(d)
        self.h = len(ll)
        self.w = len(ll[0])
        self.obs = []
        for y in range(self.h):
            for x in range(self.w):
                icon = ll[y][x]
                if icon == "#":
                    self.obs.append((x, y))
                elif icon == "^":
                    self.start = (x, y)
        self.dir = 0
        self.pos = self.start
        return 

    def getNext(self):
        possible = "NA"
        if self.dir == 1:
            possible = self.w - 1
        elif self.dir == 2:
            possible = self.h - 1
        else:
            possible = -1
        state = "OUT"
        for o in self.obs:
            if self.dir == 0 and o[0] == self.pos[0] and o[1] < self.pos[1]:
                if possible <= o[1]:
                    possible = o[1] + 1
                    state = "IN"
            if self.dir == 2 and o[0] == self.pos[0] and o[1] > self.pos[1]:
                if possible >= o[1]:
                    possible = o[1] - 1
                    state = "IN"
            if self.dir == 3 and o[1] == self.pos[1] and o[0] < self.pos[0]:
                if possible <= o[0]:
                    possible = o[0] + 1
                    state = "IN"
            if self.dir == 1 and o[1] == self.pos[1] and o[0] > self.pos[0]:
                if possible >= o[0]:
                    possible = o[0] - 1
                    state = "IN"

        if self.dir % 2 == 0:
            nex = (self.pos[0], possible)
        else:
            nex = (possible, self.pos[1])
        
        self.dir = (self.dir + 1) % 4
        self.pos = nex
        return (state, nex, self.dir)

    def print(self, seen):
        for y in range(self.h):
            row = ""
            for x in range(self.w):
                if (x, y) in self.obs:
                    row += "#"
                elif (x, y) in seen:
                    row += "+"
                elif (x, y) == self.start:
                    row += "^"
                else:
                    row += "."
            print(row)

    def loop(self):
        states = [("IN", self.start, 0)]
        while True:
            s = self.getNext()
            if s in states:
                return 1
            elif s[0] == "OUT":
                return 0
            states.append(s)
        return 0


def s(d, part):
    g = Grid(d)
    steps = col.deque([("IN", g.start, 0)])

    while True:
        nex = g.getNext()
        steps.append(nex)
        if (nex[0] == "OUT"):
            break
    
    seen = set()
    cur = steps.popleft()[1]
    for s in steps:
        s = s[1]
        minx = min(cur[0], s[0])
        maxx = max(cur[0], s[0])
        miny = min(cur[1], s[1])
        maxy = max(cur[1], s[1])
        for x in range(minx, maxx + 1):
            for y in range(miny, maxy + 1):
                seen.add((x, y))
        cur = s
        
    if part == 1:
        return len(seen)
    
    seen = list(seen)
    loops = 0
    for si in range(len(seen)):
        s = seen[si]
        if s == g.start:
            continue
        g2 = Grid(d)
        g2.obs.append(s)
        loops += g2.loop()
        print("Trying: " + str(si + 1) + "/" + str(len(seen)) + " - " + str(loops) + " Counted")

    return loops


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
    example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
    a1 = 41
    a2 = 6
    return validate_solution((s(example, 1), s(example, 2)), (a1, a2))


main()
