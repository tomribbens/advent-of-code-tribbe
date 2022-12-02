from collections import defaultdict

from aocd.models import Puzzle


def solve(data: str) -> tuple[str, str]:
    lines = data.splitlines()
    elves = defaultdict(int)
    index = 0

    for line in lines:
        if line == "":
            index += 1
            continue

        elves[index] += int(line)

    parta = max(elves.values())
    all_elves = sorted(elves.values(), reverse=True)
    partb = sum(all_elves[0:3])

    return str(parta), str(partb)


if __name__ == "__main__":
    p = Puzzle(year=2022, day=1)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
