from aocd.models import Puzzle
from collections import defaultdict
from copy import deepcopy

from aoc_tribbe.utils.parse import ints


def solve(data: str) -> tuple[str, str]:
    block_input = True
    towers_a = defaultdict(list)
    towers_b = None
    for line in data.splitlines():
        if block_input:
            if line[1] == "1":
                block_input = False
                towers_b = deepcopy(towers_a)
                continue

            for i, contents in enumerate(line[1::4], start=1):
                if contents.isalpha():
                    towers_a[i].insert(0, contents)
            continue

        if line == "":
            continue

        amount, start, finish = ints(line)
        towers_b[finish].extend(towers_b[start][-amount:])
        del towers_b[start][-amount:]

        while amount:
            towers_a[finish].append(towers_a[start].pop())
            amount -= 1

    message_a = []
    message_b = []
    for tower in range(1, len(towers_a) + 1):
        message_a.append(towers_a[tower][-1])
        message_b.append(towers_b[tower][-1])

    return str("".join(message_a)), str("".join(message_b))


if __name__ == "__main__":
    p = Puzzle(year=2022, day=5)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
