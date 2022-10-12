import json

from aocd.models import Puzzle


def solve(data):
    stack = [json.loads(data)]
    total = 0

    while stack:
        entry = stack.pop(0)
        if isinstance(entry, int):
            total += entry
        elif isinstance(entry, list):
            for subentry in entry:
                stack.append(subentry)
        elif isinstance(entry, dict):
            for subentry in entry.values():
                stack.append(subentry)

    parta = total
    stack = [json.loads(data)]
    total = 0

    while stack:
        entry = stack.pop(0)
        if isinstance(entry, int):
            total += entry
        elif isinstance(entry, list):
            for subentry in entry:
                stack.append(subentry)
        elif isinstance(entry, dict):
            if "red" in entry.values():
                continue

            for subentry in entry.values():
                stack.append(subentry)

    return str(parta), str(total)



if __name__ == "__main__":
    p = Puzzle(year=2015, day=12)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
