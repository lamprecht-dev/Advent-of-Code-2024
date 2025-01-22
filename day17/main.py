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


def combo(op, reg):
    assert(op < 7)
    if op <= 3:
        return op
    return reg[op - 4]

def dv(op, reg, i):
    num = reg[0]
    den = 2 ** combo(op, reg)
    reg[i] = math.trunc(num / den)
    return reg

def bxl(op, reg):
    reg[1] = reg[1] ^ op
    return reg

def bst(op, reg):
    reg[1] = combo(op, reg) % 8
    return reg

# NOT RETURNING REG!
def jnz(op, reg, ip):
    if reg[0] == 0:
        return ip + 2
    return op

def bxc(op, reg):
    reg[1] = reg[1] ^ reg[2]
    return reg

def out(op, reg):
    return combo(op, reg) % 8


def s(d, part):
    i = int(d.split("\n")[0].split(": ")[1])
    if part == 2:
        i = 0
    while True:
        registers = [i, 0, 0]
        ip = 0
        program = ints(d.split("\n\n")[1].split(": ")[1].split(","))
        outs = []
        innerLoop = True

        while ip < len(program) and innerLoop:
            opc, op = program[ip], program[ip + 1]

            if opc == 0:
                registers = dv(op, registers, 0)
                ip += 2
            elif opc == 1:
                registers = bxl(op, registers)
                ip += 2
            elif opc == 2:
                registers = bst(op, registers)
                ip += 2
            elif opc == 3:
                ip = jnz(op, registers, ip)
            elif opc == 4:
                registers = bxc(op, registers)
                ip += 2
            elif opc == 5:
                outs.append(out(op, registers))
                if part == 2 and outs[len(outs) - 1] != program[len(outs) - 1]:
                    innerLoop = False
                ip += 2
            else:
                registers = dv(op, registers, opc - 5)
                ip += 2

        if part == 1:
            return ",".join([str(x) for x in outs])

        if outs == program:
            return i
        else:
            i += 1

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
    example = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""
    example2 = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""
    a1 = "4,6,3,5,6,3,5,2,1,0"
    a2 = 117440
    return validate_solution((s(example, 1), s(example2, 2)), (a1, a2))


main()
