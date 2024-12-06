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
    # Code of Hyper Neutrino...
    a = [list(map(int, line.split())) for line in d.splitlines()]
    b = list(map(list, zip(*a)))
   
    if part == 1:
        for k in b: k.sort()
        return sum(abs(x - y) for x, y in zip(*b))
    return sum(x * b[1].count(x) for x in b[0]) 

    # MY CODE... 
    num = ints(d)
    i = 0
    left = []
    right = []
    sim = {}
    mult = {}

    #Every other is left and rigth
    for n in nums:
        if(i % 2 == 0):
            left.append(n)
        else:
            right.append(n)
        i+=1

    dists = 0
    left.sort()
    right.sort()
    for i in range(len(left)):
        dists += abs(left[i] - right[i])
        if(left[i] in mult):
            mult[left[i]] += 1
        else:
            mult[left[i]] = 1
        if(right[i] in left):
            if(right[i] in sim):
                sim[right[i]] += 1
            else:
                sim[right[i]] = 1

    if part == 2:
        simscore = 0
        for s in sim:
            simscore += s * sim[s] * mult[s]
        return simscore
    return dists


def main():
    if test():
        file = inp(os.path.join(os.path.dirname(__file__), 'input.txt'))
        solutions = (s(file, 1), s(file, 2))
        for sol in solutions:
            print(sol)
    else:
        print("\n\n" + BColors.FAIL + "Not All Test Successful" + BColors.ENDC)


def test():
    example = """3   4
4   3
2   5
1   3
3   9
3   3"""
    a1 = 11
    a2 = 31
    return validate_solution((s(example, 1), s(example, 2)), (a1, a2))


main()
