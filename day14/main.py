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
import time

sys.path.append('../')
from utils import *


def getQuadrant(robot, dim, time):
    x, y = getPos(robot, dim, time)
    left = x < dim[0] // 2
    top = y < dim[1] // 2
    right = not left and x != dim[0] // 2
    bottom = not top and y != dim[1] // 2

    if left and top:
        return "tl"
    if left and bottom:
        return "bl"
    if right and top:
        return "tr"
    if right and bottom:
        return "br"

    return "none"


def getPos(robot, dim, time):
    p = robot["p"]
    v = robot["v"]

    return ((p[0] + v[0] * time) % dim[0], (p[1] + v[1] * time) % dim[1])


def s(d, part, test = False):
    dim = (101, 103)
    if test:
        dim = (11, 7)

    ll = lines(d)
    amount = (part - 1) * dim[0] * dim[1] + 1
    for t in range(amount):
        quadrants = {"tl": 0, "tr": 0, "bl": 0, "br": 0, "none": 0}
        positions = set()
        for line in ll:
            p, v = line.split(" ")
            p = ints(p.split("=")[1].split(","))
            v = ints(v.split("=")[1].split(","))
            
            if part == 1:
                quadrants[getQuadrant({"p": p, "v": v}, dim, 100)] += 1
            else:
                positions.add(getPos({"p": p, "v": v}, dim, t))
       
        if part == 1 or test:
            return quadrants["tl"] * quadrants["tr"] * quadrants["bl"] * quadrants["br"]
    
        for p in positions:
            foundOption = True
            for dd in dirs:
                dx, dy = p[0] + dirs[dd][0], p[1] + dirs[dd][1]
                if (dx, dy) not in positions:
                    foundOption = False
                    break

            if foundOption:
                for y in range(dim[1]):
                    row = ""
                    for x in range(dim[0]):
                        if (x, y) in positions:
                            row += "#"
                        else:
                            row += " "
                    print(row)
                print(t, "/", amount)
                break
        

    return quadrants["tl"] * quadrants["tr"] * quadrants["bl"] * quadrants["br"]


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
    example = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
    a1 = 12
    a2 = None
    return validate_solution((s(example, 1, True), s(example, 2, True)), (a1, a2))


main()
