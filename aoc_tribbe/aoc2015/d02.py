from aocd.models import Puzzle


def solve(input_data):
    lines = input_data.splitlines()
    paper_required = 0
    ribbon_required = 0

    for line in lines:
        l, w, h = list(map(int, line.split("x")))
        sides = (l * w, w * h, h * l)
        paper_required += 2 * sum(sides) + min(sides)

        ribbon_required += 2 * sum((l, w, h)) - 2 * max(l, w, h) + l * w * h

    return str(paper_required), str(ribbon_required)


if __name__ == "__main__":
    p = Puzzle(year=2015, day=2)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
