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


known_values = {}
operators = {}

def find(target):
    print(operators, target)
    a, op, b = operators[target]
    if a not in known_values:
        a = find(a)
    else:
        a = known_values[a]

    if b not in known_values:
        b = find(b)
    else:
        b = known_values[b]

    if op == "OR":
        c = a | b
    elif op == "AND":
        c = a & b
    elif op == "XOR":
        c = a ^ b

    known_values[target] = c
    return c


def s(d, part):
    global known_values, operators
    if part == 2:
        return 0

    known_values = {}
    operators = {}

    z_list = []

    init_vals, instructions = d.split("\n\n")
    for iv in lines(init_vals):
        n, v = iv.split(": ")
        known_values[n] = int(v)
        if n.startswith("z"):
            z_list,append(n)
    
    for i in lines(instructions):
        origin, target = i.split(" -> ")
        a, ins, b = origin.split(" ")
        print(target, origin)
        pp.pp(operators)
        assert target not in operators
        operators[target] = [a, ins, b]
        if target.startswith("z"):
            z_list.append(target)
    
    z_list = sorted(z_list)
    # pp.pp(known_values)
    # pp.pp(operators)
    # pp.pp(z_list)

    z_vals = {}
    for z in z_list:
        zv = find(z)
        z_vals[z] = zv

    binary = ""
    for i in range(len(z_vals)):
        j = len(z_vals) - i - 1
        if (j) < 10:
            ii = "0" + str(j)
        else:
            ii = str(j)
        binary += str(z_vals["z" + ii])
    print(binary, len(binary))
    return int(binary, 2)

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
    example = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""
    a1 = 2024
    a2 = None
    return validate_solution((s(example, 1), s(example, 2)), (a1, a2))


main()
