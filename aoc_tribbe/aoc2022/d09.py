from aocd.models import Puzzle
from collections import namedtuple

Position = namedtuple("Position", ["x", "y"])


def get_next_knot_position(head: Position, tail: Position) -> Position:
    """Returns the position of the tail after attempting to move one closer to the head"""
    if head == tail:
        return tail

    # if tail is adjacent to head, return tail
    if abs(head.x - tail.x) + abs(head.y - tail.y) == 1:
        return tail

    # if tail is diagonally adjacent to head, return tail
    if abs(head.x - tail.x) == 1 and abs(head.y - tail.y) == 1:
        return tail

    # if tail is not adjacent to head, move one closer to head
    # if tail is in the same column as head, move vertically
    if head.x == tail.x:
        if head.y > tail.y:
            return Position(tail.x, tail.y + 1)
        else:
            return Position(tail.x, tail.y - 1)
    # if tail is in the same row as head, move horizontally
    elif head.y == tail.y:
        if head.x > tail.x:
            return Position(tail.x + 1, tail.y)
        else:
            return Position(tail.x - 1, tail.y)
    # if tail is not in the same row or column as head, move diagonally
    else:
        if head.x > tail.x:
            x = tail.x + 1
        else:
            x = tail.x - 1
        if head.y > tail.y:
            y = tail.y + 1
        else:
            y = tail.y - 1
        return Position(x, y)


def solve(data: str) -> tuple[str, str]:
    head = tail = Position(0, 0)
    knots = [Position(0, 0)] * 9
    tail_positions_a = set()
    tail_positions_b = set()

    for line in data.splitlines():
        direction, distance = line.split(" ")
        distance = int(distance)
        for _ in range(distance):
            if direction == "U":
                head = Position(head.x, head.y + 1)
            elif direction == "D":
                head = Position(head.x, head.y - 1)
            elif direction == "R":
                head = Position(head.x + 1, head.y)
            elif direction == "L":
                head = Position(head.x - 1, head.y)

            tail = get_next_knot_position(head, tail)
            tail_positions_a.add(tail)

            # move each knot one closer to the previous knot, with the first one moving towards the head
            knots[0] = get_next_knot_position(head, knots[0])
            for i in range(1, 9):
                knots[i] = get_next_knot_position(knots[i - 1], knots[i])

            tail_positions_b.add(knots[-1])

    return str(len(tail_positions_a)), str(len(tail_positions_b))


if __name__ == "__main__":
    p = Puzzle(year=2022, day=9)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
