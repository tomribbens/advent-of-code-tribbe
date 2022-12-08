import numpy as np

from aocd.models import Puzzle


def solve(data: str) -> tuple[str, str]:
    forest = np.genfromtxt(data.splitlines(), dtype=int, delimiter=1)
    total_visible = 0
    scenic_view_scores = []

    for row in range(forest.shape[0]):
        for column in range(forest.shape[1]):
            total_visible += any(
                [
                    all(forest[i][column] < forest[row][column] for i in range(row - 1, -1, -1)),
                    all(
                        forest[i][column] < forest[row][column]
                        for i in range(row + 1, forest.shape[0])
                    ),
                    all(forest[row][i] < forest[row][column] for i in range(column - 1, -1, -1)),
                    all(
                        forest[row][i] < forest[row][column]
                        for i in range(column + 1, forest.shape[1])
                    ),
                ]
            )

            left, right, up, down = 0, 0, 0, 0
            blocked = False
            offset = 1
            while not blocked and row - offset >= 0:
                left += 1
                if forest[row - offset][column] >= forest[row][column]:
                    blocked = True
                offset += 1

            blocked = False
            offset = 1
            while not blocked and row + offset < forest.shape[0]:
                right += 1
                if forest[row + offset][column] >= forest[row][column]:
                    blocked = True
                offset += 1

            blocked = False
            offset = 1
            while not blocked and column - offset >= 0:
                up += 1
                if forest[row][column - offset] >= forest[row][column]:
                    blocked = True
                offset += 1

            blocked = False
            offset = 1
            while not blocked and column + offset < forest.shape[1]:
                down += 1
                if forest[row][column + offset] >= forest[row][column]:
                    blocked = True
                offset += 1

            scenic_view_scores.append(up * down * left * right)

    return str(total_visible), str(max(scenic_view_scores))


if __name__ == "__main__":
    p = Puzzle(year=2022, day=8)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
