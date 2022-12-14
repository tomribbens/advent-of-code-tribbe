import numpy as np
from aocd.models import Puzzle
from itertools import pairwise

from aoc_tribbe.utils.parse import ints


def solve(data: str) -> tuple[str, str]:
    all_coords = ints(data)
    y_size = max(all_coords[1::2]) + 3
    x_size = max(all_coords[::2]) + y_size + 1
    grid = np.zeros((y_size, x_size), dtype=int)

    for line in data.splitlines():
        for origin, destination in pairwise(line.split(" -> ")):
            o_x, o_y = ints(origin)
            d_x, d_y = ints(destination)
            if o_x > d_x:
                o_x, d_x = d_x, o_x
            if o_y > d_y:
                o_y, d_y = d_y, o_y
            grid[o_y : d_y + 1, o_x : d_x + 1] = 1

    grid[y_size -1] = 1

    full = False
    sand = 0
    total_sand_a = 0
    total_sand_b = 0
    while not full:
        sand_settled = False
        new_sand = [500, 0]

        while not sand_settled:
            if not total_sand_a and new_sand[1] >= y_size - 3:
                total_sand_a = sand

            if grid[0, 500]:
                total_sand_b = sand
                sand_settled = True
                full = True

            if grid[new_sand[1] + 1, new_sand[0]] == 0:
                new_sand[1] += 1
                continue

            if grid[new_sand[1] + 1, new_sand[0] - 1] == 0:
                new_sand[0] -= 1
                new_sand[1] += 1
                continue

            if grid[new_sand[1] + 1, new_sand[0] + 1] == 0:
                new_sand[0] += 1
                new_sand[1] += 1
                continue

            grid[new_sand[1], new_sand[0]] = 2
            sand += 1
            sand_settled = True

    return str(total_sand_a), str(total_sand_b)


if __name__ == "__main__":
    p = Puzzle(year=2022, day=14)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
