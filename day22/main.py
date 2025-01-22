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


def mix_n_prune(before, after):
    return before ^ after % 16777216


@functools.cache
def get_secret(secret):
    secret = mix_n_prune(secret, secret * 64)
    secret = mix_n_prune(secret, secret // 32)
    secret = mix_n_prune(secret, secret * 2048)
    
    return secret

def most_nanas(price_history):
    most_nanas = 0
    best_sequence = []
    change_history = []
    possible_changes = set()

    for j, ph in enumerate(price_history):
        changes = []
        for i in range(1, len(ph)):
            changes.append(ph[i] - ph[i - 1])
            if i >= 4:
                possible_changes.add(tuple(changes[i - 4: i]))
        change_history.append(changes)
        # print(j)
        # print(ph)
        # print(changes)

    for pc in possible_changes:
        nanas = 0
        print(pc)
        for j, ch in enumerate(change_history):
            for i in range(3, len(ch)):
                if pc[0] == ch[i - 3] and pc[1] == ch[i - 2] and pc[2] == ch[i - 1] and pc[3] == ch[i]:
                    # if pc == (-9, 9, -1, 0):
                    #     print(price_history[j][i + 1], i)
                    #     print(pc, i, j)
                    #     print(ch)
                    #     print(price_history[j])
                    nanas += price_history[j][i + 1]
                    break # only once per sequence

        if most_nanas < nanas:
            most_nanas = nanas
            best_sequence = pc

    print(most_nanas, best_sequence)
    return most_nanas

def s(d, part):
    total = 0
    price_history = []
    ll = lines(d)
    for line in ll:
        buyer = []
        secret = int(line)
        for i in range(2000):
            secret = get_secret(secret)
            buyer.append(secret % 10)
        total += secret
        price_history.append(buyer)

    if part == 2:
        return most_nanas(price_history)

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
    example = """1
10
100
2024"""
    example2 = """1
2
3
2024"""
    a1 = 37327623
    a2 = 23
    return validate_solution((s(example, 1), s(example2, 2)), (a1, a2))


main()
