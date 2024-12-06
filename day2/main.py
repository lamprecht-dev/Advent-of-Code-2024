import sys
import functools
sys.path.append('../')
from utils import *


def is_good(levels):
    diffs = [b - a for a, b in zip(levels, levels[1:])]
    dmin, dmax = min(diffs), max(diffs)
    small_step = 4 > abs(dmin) > 0 and 4 > abs(dmax) > 0
    same_sign = (dmin > 0) == (dmax > 0)
    return small_step and same_sign

def s(d, part):
    # My attempt in working a bit more functional
    # I feel like using the divided variable down there creates a lot of extra data that is not needed and can just be straight calculated like in my first version
    data = list(map(ints, lines(d)))
    if part == 1:
        return [is_good(levels) for levels in data].count(True)
    
    divided = ([[levels[0:i] + levels[i + 1:] for i in range(len(levels))]
                for levels in data])
    return [any([is_good(levels[i]) for levels in zip(data, *divided)]) 
           for i in range(len(data))].count(True)


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
    example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    a1 = 2
    a2 = 4
    return validate_solution((s(example, 1), s(example, 2)), (a1, a2))


main()
