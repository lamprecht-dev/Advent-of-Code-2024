import sys
import collections
import datetime
import itertools as it
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
    kp1 = "789456123_0A"
    kp2 = "_^A<v>"
    total = 0

    return total


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
    example = """029A
980A
179A
456A
379A"""
    a1 = 126384
    a2 = None
    return validate_solution((s(example, 1), s(example, 2)), (a1, a2))


main()
