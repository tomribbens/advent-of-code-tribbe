from collections import defaultdict
from itertools import permutations
from aocd.models import Puzzle


def get_distance(travel, distances):
    distance = 0
    for start, end in zip(travel, travel[1:]):
        distance += distances[start][end]

    return distance


def solve(input_data):
    lines = input_data.splitlines()

    locations = set()
    distances = defaultdict(dict)

    for line in lines:
        locs, distance = line.split(' = ')
        start, end = locs.split(' to ')
        locations.add(start)
        locations.add(end)
        distances[start][end] = int(distance)
        distances[end][start] = int(distance)

    shortest = min([get_distance(path, distances) for path in permutations(locations)])
    longest = max([get_distance(path, distances) for path in permutations(locations)])

    return str(shortest), str(longest)


if __name__ == "__main__":
    p = Puzzle(year=2015, day=9)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
