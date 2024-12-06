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


class Rule:
    def __init__(self, val):
        self.val = val
        self.bigger = []
        self.smaller = []

    def big(self, big):
        self.bigger.append(big)

    def small(self, small):
        self.smaller.append(small)
    
    def same(self, val):
        return val == self.val

    def knows(self, val):
        if val in self.bigger:
            return 1
        if val in self.smaller:
            return -1
        return 0

    def __str__(self):
        return str(self.smaller) + " <<< " + str(self.val) + " <<< " + str(self.bigger)

    def __repr__(self):
        return self.__str__()


def createRules(rules):
    newRules = {}
    for ll in lines(rules):
        l, r = ints(ll, "|")
        if l not in newRules:
            newRules[l] = Rule(l)
        newRules[l].big(r)
        if r not in newRules:
            newRules[r] = Rule(r)
        newRules[r].small(l)
    return newRules


def isInOrder(d, rules):
    for a in range(len(d)):
        for b in range(a, len(d)):
            if d[a] == d[b]:
                continue
            rel = rules[d[a]].knows(d[b])
            if rel < 0:
                return False

    return True


def order(d, rules):
    change = True
    while change:
        change = False
        for a in range(len(d)):
            for b in range(a, len(d)):
                if d[a] == d[b]:
                    continue
                rel = rules[d[a]].knows(d[b])
                if rel < 0:
                    d[a], d[b] = d[b], d[a]
                    change = True

    return d

def s(d, part):
    rules, data = d.split("\n\n")
    rules = createRules(rules)
    total = 0

    for ll in lines(data):
        nums = ints(ll, ",")
        if part == 1 and isInOrder(nums, rules):
            total += nums[len(nums) // 2]
        elif part == 2 and not isInOrder(nums, rules):
            nums = order(nums, rules)
            total += nums[len(nums) // 2]

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
    example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
    a1 = 143
    a2 = 123
    return validate_solution((s(example, 1), s(example, 2)), (a1, a2))


main()
