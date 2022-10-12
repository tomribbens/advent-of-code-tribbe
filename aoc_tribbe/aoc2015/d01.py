from aocd.models import Puzzle


def solve(data):
    floor = 0
    basement = None

    for number, instruction in enumerate(data, start=1):
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1
            if floor < 0 and basement is None:
                basement = number
        else:
            raise ValueError

    return str(floor), str(basement)


if __name__ == "__main__":
    p = Puzzle(year=2015, day=1)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
