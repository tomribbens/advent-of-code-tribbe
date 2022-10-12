import numpy as np

from aocd.models import Puzzle, User

def solve(data):
    target = int(data)
    MAX_HOUSES = 2000000
    houses_a = np.zeros(MAX_HOUSES)
    houses_b = np.zeros(MAX_HOUSES)

    for elf in range(1, MAX_HOUSES):
        houses_a[elf::elf] += 10 * elf
        houses_b[elf:(elf+1)*50:elf] += 11 * elf

    return str(np.nonzero(houses_a >= target)[0][0]), str(np.nonzero(houses_b >= target)[0][0])


if __name__ == "__main__":
    p = Puzzle(year=2015, day=20)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
