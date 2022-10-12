import re
from collections import defaultdict
from itertools import permutations

from aocd.models import Puzzle


def get_total_happiness(seating, happiness):
    total = 0
    for seat1, seat2 in zip(seating, seating[1:] + (seating[0],)):
        total += happiness[seat1][seat2] + happiness[seat2][seat1]

    return total

def solve(data):
    lines = data.splitlines()
    happiness = defaultdict(dict)

    for line in lines:
        match = re.search(r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).", line)
        actor, action, amount, subject = match.groups()
        happiness[actor][subject] = int(amount) * (-1 if action == "lose" else 1)

    parta = max([get_total_happiness(seating, happiness) for seating in permutations(happiness.keys())])

    for person in list(happiness.keys()):
        happiness[person]["me"] = 0
        happiness["me"][person] = 0
    partb = max([get_total_happiness(seating, happiness) for seating in permutations(happiness.keys())])

    return str(parta), str(partb)



if __name__ == "__main__":
    p = Puzzle(year=2015, day=13)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
