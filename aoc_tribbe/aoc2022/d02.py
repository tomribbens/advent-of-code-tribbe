from collections import defaultdict

from aocd.models import Puzzle


def solve(data: str) -> tuple[str, str]:
    scores_a = {
        "A": {
            "X": 4,
            "Y": 8,
            "Z": 3,
        },
        "B": {
            "X": 1,
            "Y": 5,
            "Z": 9,
        },
        "C": {
            "X": 7,
            "Y": 2,
            "Z": 6,
        },
    }
    scores_b = {
        "A": {
            "X": 3,
            "Y": 4,
            "Z": 8,
        },
        "B": {
            "X": 1,
            "Y": 5,
            "Z": 9,
        },
        "C": {
            "X": 2,
            "Y": 6,
            "Z": 7,
        },
    }

    total_score_a = 0
    total_score_b = 0

    for line in data.splitlines():
        opp, me = line.split()
        total_score_a += scores_a[opp][me]
        total_score_b += scores_b[opp][me]

    return str(total_score_a), str(total_score_b)


if __name__ == "__main__":
    p = Puzzle(year=2022, day=2)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
