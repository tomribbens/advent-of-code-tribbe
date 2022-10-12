import re
from collections import defaultdict

from aocd.models import Puzzle


def solve(data):
    lines = data.splitlines()
    sues = defaultdict(dict)
    pattern = re.compile(r'Sue (\d+): (.+)')
    looking_for = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    for line in lines:
        match = pattern.search(line)
        sue, characteristics = match.groups()
        characteristics = characteristics.split(', ')
        for char in characteristics:
            c, n = char.split(': ')
            sues[sue][c] = int(n)


    parta = ""
    for idx, sue in sues.items():
        this_sue_a = True
        for char, val in sue.items():
            if looking_for[char] != val:
                this_sue_a = False
        if this_sue_a:
            parta = idx

    partb = ""
    for idx, sue in sues.items():
        this_sue_b = True
        for char, val in sue.items():
            if char == "cats" or char == "trees":
                if not looking_for[char] < val:
                    this_sue_b = False
            elif char == "pomeranians" or char == "goldfish":
                if not looking_for[char] > val:
                    this_sue_b = False
            else:
                if looking_for[char] != val:
                    this_sue_b = False

        if this_sue_b:
            partb = idx

    return str(parta), str(partb)


if __name__ == "__main__":
    p = Puzzle(year=2015, day=16)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
