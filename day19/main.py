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


def canMake(pattern, towels):
    if pattern == "":
        return True
    for t in towels:
        if pattern.endswith(t):
            if canMake(pattern[:-len(t)], towels):
                return True

    return False

@functools.cache
def countMake(pattern, towels):
    if pattern == "":
        return 1
    count = 0
    for t in towels:
        if pattern.endswith(t):
            count += countMake(pattern[:-len(t)], towels)

    return count



def s(d, part):
    towels, patterns = d.split("\n\n")
    towels = tuple(towels.split(", "))
    patterns = patterns.split("\n")
    
    count = 0
    for p in patterns:
        if canMake(p, towels) and part == 1:
            count += 1
        if part == 2:
            count += countMake(p, towels)

    return count


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
    example = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""
    a1 = 6
    a2 = 16
    return validate_solution((s(example, 1), s(example, 2)), (a1, a2))


main()
