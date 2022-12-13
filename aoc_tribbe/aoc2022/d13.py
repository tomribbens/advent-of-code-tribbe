from aocd.models import Puzzle
from functools import cmp_to_key


def is_ordered(left: int | list[int | list], right: int | list[int | list]) -> int:
    if isinstance(left, int) and isinstance(right, int):
        return left - right

    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]

    for l, r in zip(left, right):
        if ordered := is_ordered(l, r):
            return ordered

    return len(left) - len(right)


def solve(data: str) -> tuple[str, str]:
    pairs = data.split("\n\n")
    all_packets = [[[2]], [[6]]]
    total = 0
    for idx, pair in enumerate(pairs, start=1):
        left = eval(pair.splitlines()[0])
        right = eval(pair.splitlines()[1])
        all_packets.append(left)
        all_packets.append(right)
        if is_ordered(left, right) < 0:
            total += idx

    all_packets.sort(key=cmp_to_key(is_ordered))
    first_packet = all_packets.index([[2]]) + 1
    last_packet = all_packets.index([[6]]) + 1

    return str(total), str(first_packet * last_packet)


if __name__ == "__main__":
    p = Puzzle(year=2022, day=13)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
