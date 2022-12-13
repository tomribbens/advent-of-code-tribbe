from aocd.models import Puzzle

from aoc_tribbe.utils.datatypes import Tristate


class Packet:
    def __init__(self, data: list):
        self.data = data

    def __repr__(self):
        return str(self.data)

    def __lt__(self, other):
        ordered = is_ordered(self.data, other.data)
        if ordered == True:
            return True
        elif ordered == False:
            return False

    def __gt__(self, other):
        ordered = is_ordered(other.data, self.data)
        if ordered == True:
            return False
        elif ordered == False:
            return True

    def __eq__(self, other):
        return self.data == other.data


def is_ordered(left: int | list[int | list], right: int | list[int | list]) -> Tristate:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return Tristate(True)
        elif left > right:
            return Tristate(False)
        else:
            return Tristate(None)

    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]

    for l, r in zip(left, right):
        if (ordered := is_ordered(l, r)) in (True, False):
            return ordered

    if len(left) < len(right):
        return Tristate(True)
    elif len(left) > len(right):
        return Tristate(False)
    else:
        return Tristate(None)


def solve(data: str) -> tuple[str, str]:
    pairs = data.split("\n\n")
    all_packets = [Packet([[2]]), Packet([[6]])]
    total = 0
    for idx, pair in enumerate(pairs):
        left = eval(pair.splitlines()[0])
        right = eval(pair.splitlines()[1])
        all_packets.append(Packet(left))
        all_packets.append(Packet(right))
        if is_ordered(left, right) == True:
            total += idx + 1

    all_packets.sort()
    first_packet = all_packets.index(Packet([[2]])) + 1
    last_packet = all_packets.index(Packet([[6]])) + 1

    return str(total), str(first_packet * last_packet)


if __name__ == "__main__":
    p = Puzzle(year=2022, day=13)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
