from __future__ import annotations
from aocd.models import Puzzle

from aoc_tribbe.utils.parse import ints


def add_lines(lines: list[Line]) -> list[Line]:
    """Create a new list of lines minimizing the number of lines."""
    ranges = []
    for line in lines:
        if line is None:
            continue

        if len(ranges) == 0:
            ranges.append((line.start, line.end))
            continue

        for i, (start, end) in enumerate(ranges):
            if start <= line.start <= end < line.end:
                ranges[i] = (start, line.end)
                break
            if line.start <= start <= line.end <= end:
                ranges[i] = (line.start, end)
                break
            if start <= line.start <= line.end <= end:
                break
        else:
            ranges.append((line.start, line.end))
    ranges.sort()
    new_lines = [Line(start, end) for start, end in ranges]
    if len(new_lines) < len(lines):
        return add_lines(new_lines)
    return new_lines


class Line:
    start: int
    end: int

    def __init__(self, start, end):
        self.start = start
        self.end = end


class Sensor:
    position: tuple[int, int]
    beacon: tuple[int, int]
    distance: int

    def __init__(self, position: tuple[int, int], beacon: tuple[int, int]):
        self.position = position
        self.beacon = beacon
        self.distance = abs(position[0] - beacon[0]) + abs(position[1] - beacon[1])

    @classmethod
    def from_string(cls, string: str):
        positions = ints(string)
        return cls((positions[0], positions[1]), (positions[2], positions[3]))

    def blocks(self, positon: tuple[int, int]) -> bool:
        return (
            abs(positon[0] - self.position[0]) + abs(positon[1] - self.position[1])
            <= self.distance
        )

    def get_lines(self, row: int) -> Line:
        if not self.blocks((self.position[0], row)):
            return None
        start = self.position[0] - (self.distance - abs(row - self.position[1]))
        end = self.position[0] + (self.distance - abs(row - self.position[1]))
        return Line(start, end)


def solve(data: str, tested_row: int = 2_000_000) -> tuple[str, str]:
    sensors = [Sensor.from_string(line) for line in data.splitlines()]
    blocked_list = set()
    for sensor in sensors:
        blocked_left = sensor.position[0] - (
            sensor.distance - abs(sensor.position[1] - tested_row)
        )
        blocked_right = sensor.position[0] + (
            sensor.distance - abs(sensor.position[1] - tested_row)
        )
        blocked_list = blocked_list.union(set(range(blocked_left, blocked_right + 1)))

    beacons = set(s.beacon[0] for s in sensors if s.beacon[1] == tested_row)
    blocked_on_row = len(blocked_list) - len(beacons)

    for row in range(4_000_000):
        lines = [sensor.get_lines(row) for sensor in sensors]
        row_occupancy = add_lines(lines)
        if len(row_occupancy) == 1:
            continue

        if (
            len(row_occupancy) == 2
            and row_occupancy[0].end + 2 == row_occupancy[1].start
        ):
            frequency = (row_occupancy[0].end + 1) * 4_000_000 + row
            break

    return str(blocked_on_row), str(frequency)


if __name__ == "__main__":
    p = Puzzle(year=2022, day=15)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
