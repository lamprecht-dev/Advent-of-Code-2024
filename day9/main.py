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

def p1(d):
    blocks = []
    white = False
    curI = 0
    for c in d:
        for ci in range(int(c)):
            if white:
                blocks.append(None)
            else:
                blocks.append(curI)
        white = not white
        if white:
            curI += 1

    p1 = 0
    p2 = len(blocks) - 1
    while p1 < p2:
        if blocks[p2] == None:
            p2 -= 1
            continue
        if blocks[p1] == None:
            blocks[p1], blocks[p2] = blocks[p2], None
            p2 -= 1
        p1 += 1
        
    checkSum = 0
    for i in range(p2 + 1):
        checkSum += i * blocks[i]

    return checkSum

def cleanBlocks(p2, blocks):
    bindex = 0
    while bindex < len(blocks) - 1:
        b = blocks[bindex]
        b2 = blocks[bindex + 1]
        if b[0] == None and b2[0] == None:
            b[1] += b2[1]
            blocks.pop(bindex + 1)
            if bindex + 1 <= p2:
                p2 -= 1
            bindex -= 1
        bindex += 1
    return p2, blocks

def p2(d):
    blocks = []
    white = False
    curI = 0
    for c in d:
        if white:
            blocks.append([None, int(c)])
        else:
            blocks.append([curI, int(c)])
            curI += 1
        white = not white

    curBlock = curI - 1
    p1 = 0
    p2 = len(blocks) - 1
    while p2 >= 0:
        if blocks[p2][0] == None:
            p2 -= 1
            continue
        if p1 > p2:
            p1 = 0
            p2 -= 1
        if blocks[p1][0] == None:
            diff = blocks[p1][1] - blocks[p2][1]
            if diff == 0:
                blocks[p1], blocks[p2] = blocks[p2], blocks[p1]
            elif diff > 0:
                blocks[p1][1] = diff
                blocks.insert(p1, blocks[p2])
                p2 += 1
                blocks[p2] = [None, blocks[p2][1]]
            else:
                p1 += 1
                continue
            p2, blocks = cleanBlocks(p2, blocks)
            p1 = 0
            p2 -= 1
            continue
        p1 += 1
    
    i = 0
    checkSum = 0
    for b in blocks:
        if b[0] != None:
            avrg = (i + i + b[1] - 1) * b[1] // 2
            checkSum += avrg * b[0]
        i += b[1]


    return checkSum


def s(d, part):
    if part == 2:
        return p2(d)

    return p1(d)

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
    example = """2333133121414131402"""
    a1 = 1928
    a2 = 2858
    return validate_solution((s(example, 1), s(example, 2)), (a1, a2))


main()
