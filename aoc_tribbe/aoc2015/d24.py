from itertools import combinations
from math import prod

from aocd.models import Puzzle


def balance_storage(data, storage_spaces=3):
    packages = [int(p) for p in data.splitlines()]
    qe = None
    group1_packages = 0
    assert sum(packages) % storage_spaces == 0
    target_weight = sum(packages) // storage_spaces

    while qe is None:
        group1_packages += 1
        for group1 in combinations(packages, group1_packages):
            if not sum(group1) == target_weight:
                continue
            if qe is not None and prod(group1) > qe:
                continue
            remaining_packages = packages.copy()
            for p in group1:
                remaining_packages.remove(p)
            group2_packages = 1
            while group2_packages <= len(remaining_packages) // 2:
                for group2 in combinations(remaining_packages, group2_packages):
                    if not sum(group2) == target_weight:
                        continue
                    new_qe = prod(group1)
                    if qe is None or new_qe < qe:
                        qe = new_qe
                        break
                else:
                    group2_packages += 1
                    continue
                break
    return qe


def solve(data):
    parta = balance_storage(data)
    partb = balance_storage(data, storage_spaces=4)

    return str(parta), str(partb)



if __name__ == "__main__":
    p = Puzzle(year=2015, day=24)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
