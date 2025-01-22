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

def find_triplets(connections):
    triplets = set()
    for c in connections:
        if c[:1] != "t":
            continue
        for c2 in connections[c]:
            for c3 in connections[c2]:
                if c3 in c or c not in connections[c3]:
                    continue
                c_sorted = sorted([c, c2, c3])
                triplets.add(tuple(c_sorted))
    return triplets


def longest_lan(a, b):
    if len(a) > len(b):
        return a
    return b


def find_lan(connections):
    all_connections_found = []
    for c in connections:
        all_connections_found.extend(connect([c], connections[c], connections))
       
    return functools.reduce(longest_lan, all_connections_found)


def connect(established, left, connections):
    all_connections = [established]
    for c in left:
        works = True
        for e in established:
            if e not in connections[c]:
                works = False
                break
        if works:
            new_left = left
            new_left.remove(c)
            all_connections.extend(connect(established + [c], new_left, connections))
    
    return all_connections



def s(d, part):
    connections = {}

    ll = lines(d)
    for line in ll:
        fr, to = line.split("-")
        if fr not in connections:
            connections[fr] = []
        if to not in connections:
            connections[to] = []
        connections[fr].append(to)
        connections[to].append(fr)

    if part == 1:
        return len(find_triplets(connections))

    lan = find_lan(connections)
    return ",".join(sorted(lan))


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
    example = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""
    a1 = 7
    a2 = "co,de,ka,ta"
    return validate_solution((s(example, 1), s(example, 2)), (a1, a2))


main()
