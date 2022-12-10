from aocd.models import Puzzle
from dataclasses import dataclass

from aoc_tribbe.utils.parse import atoms_or_ints
from aoc_tribbe.utils.ocr import perform_ocr


@dataclass
class CommsDevice:
    clock: int = 0
    register: int = 1
    total: int = 0
    screen: str = ""

    def clock_tick(self):
        if abs(self.register - self.clock % 40) <= 1:
            self.screen += "#"
        else:
            self.screen += "."

        if self.clock % 40 == 39:
            self.screen += "\n"

        self.clock += 1
        if self.clock % 40 == 20:
            self.total += self.register * self.clock


def solve(data: str) -> tuple[str, str]:
    device = CommsDevice(0, 1, 0, "")

    for line in data.splitlines():
        line_tuple = atoms_or_ints(line)
        if line_tuple[0] == "noop":
            device.clock_tick()
            continue
        if line_tuple[0] == "addx":
            device.clock_tick()
            device.clock_tick()
            device.register += line_tuple[1]
            continue

    return str(device.total), perform_ocr(device.screen).upper()


if __name__ == "__main__":
    p = Puzzle(year=2022, day=10)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
