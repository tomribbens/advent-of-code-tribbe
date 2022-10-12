
from aocd.models import Puzzle


def combinations_generator(containers):
    if len(containers) == 1:
        yield containers
        yield []
    elif len(containers) > 1:
        for idx in range(len(containers)):
            for y in combinations_generator(containers[idx+1:]):
                yield [containers[idx]] + y
        yield []
    elif len(containers) == 0:
        yield []


def solve(data):
    containers = [int(x) for x in data.splitlines()]

    parta = len([filled for filled in combinations_generator(containers) if sum(filled) == 150])
    minimum_containers = min([len(filled) for filled in combinations_generator(containers) if sum(filled) == 150])
    partb = len([filled for filled in combinations_generator(containers)
                 if sum(filled) == 150 and len(filled) == minimum_containers])

    return str(parta), str(partb)


if __name__ == "__main__":
    p = Puzzle(year=2015, day=17)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
