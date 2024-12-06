import sys

sys.path.append('../')
from utils import *


def count(ll, r, c, h, w, start, dirs, target, rangeA, rangeB):
    if ll[r][c] != start:
        return 0

    allWords = {}

    for d in dirs:
        allWords[d] = ""
        for dist in range(rangeA, rangeB):
            dx, dy = dirs[d][0] * dist, dirs[d][1] * dist
            if (w <= dx + c or dx + c < 0 or h <= dy + r or dy + r < 0):
                continue
            allWords[d] += ll[dy + r][dx + c]

    count = 0

    for key, val in allWords.items():
        if val == target:
            count += 1

    return count

def s(d, part):
    ll = lines(d)
    rows = len(ll)
    cols = len(ll[0])

    total = 0
    for r in range(rows):
        for c in range(cols):
            if part == 1:
                dirs = {'r': (1, 0), 'd': (0, 1), 'l': (-1, 0), 'u': (0, -1), 'ur': (1, -1), 'dr': (1, 1), 'dl': (-1, 1), 'ul': (-1, -1)}
                total += count(ll, r, c, rows, cols, "X", dirs, "XMAS", 0, 4)
            else:
                dirs = {'ur': (1, -1), 'dr': (1, 1), 'dl': (-1, 1), 'ul': (-1, -1)}
                total += count(ll, r, c, rows, cols, "A", dirs, "MAS", -1, 2) == 2

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
    example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    a1 = 18
    a2 = 9
    return validate_solution((s(example, 1), s(example, 2)), (a1, a2))


main()
