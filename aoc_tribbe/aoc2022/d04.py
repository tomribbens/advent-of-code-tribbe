from aocd.models import Puzzle

from aoc_tribbe.utils.parse import ints


def solve(data: str) -> tuple[str, str]:
    totally_overlapping = 0
    partly_overlapping = 0

    for line in data.splitlines():
        a, b, c, d = ints(line, signed=False)
        if (a <= c and b >= d) or (c <= a and d >= b):
            totally_overlapping += 1

        if (
            (a <= c and b >= c)
            or (c <= a and d >= a)
            or (a <= d and b >= d)
            or (c <= b and d >= b)
        ):
            partly_overlapping += 1

    return str(totally_overlapping), str(partly_overlapping)


if __name__ == "__main__":
    p = Puzzle(year=2022, day=4)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
