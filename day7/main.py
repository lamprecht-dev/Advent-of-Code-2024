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


def canOperateOld(ans, nums, part):
    operators = ["+", "*"]
    if part == 2:
        operators.append("|")
    # dfs with early return if overshooting because + amd * only increase
    visited = []
    dfs = [("", nums[0])]
    while len(dfs) > 0:
        nex = dfs.pop()
        if len(nex[0]) == len(nums) - 1:
            if nex[1] == ans:
                print(nex, ans, nums)
                return True
            else:
                continue
        if nex[1] > ans:
            continue
        for o in operators:
            nextVal = nex[1]
            if o == "+":
                nextVal += nums[len(nex[0]) + 1]
            elif o == "*":
                nextVal *= nums[len(nex[0]) + 1]
            elif o == "|":
                nextVal = int(str(nextVal) + str(nums[len(nex[0]) + 1]))
            dfs.append((nex[0] + o, nextVal))

    return False


def canOperate(ans, nums, part):
    if len(nums) == 1: return ans == nums[0]
    if ans % nums[-1] == 0 and canOperate(ans // nums[-1], nums[:-1], part): return True
    if ans > nums[-1] and canOperate(ans - nums[-1], nums[:-1], part): return True
    sAns = str(ans)
    sNum = str(nums[-1])
    if part == 2 and len(sAns) > len(sNum) and sAns.endswith(sNum) and canOperate(int(sAns[:-len(sNum)]), nums[:-1], part): return True
    return False


def s(d, part):
    ll = lines(d)
    total = 0
    for line in ll:
        ans, nums = line.split(": ")
        nums = ints(nums, " ")
        ans = int(ans)
        if canOperate(ans, nums, part):
            total += ans

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
    example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    a1 = 3749
    a2 = 11387
    return validate_solution((s(example, 1), s(example, 2)), (a1, a2))


main()
