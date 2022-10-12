import re
import numpy as np

from aocd.models import Puzzle


def solve(input_data):
    lines = input_data.splitlines()

    lights_a = np.zeros((1000, 1000), dtype=bool)
    lights_b = np.zeros((1000, 1000), dtype=int)

    for line in lines:
        match = re.search(r'(.*) (\d+),(\d+) through (\d+),(\d+)', line)
        cmd, x1, y1, x2, y2 = match.groups()
        x1, y1, x2, y2 = int(x1), int(y1), int(x2) + 1, int(y2) + 1

        if cmd == "turn on":
            lights_a[x1:x2, y1:y2] = True
            lights_b[x1:x2, y1:y2] += 1
        elif cmd == "turn off":
            lights_a[x1:x2, y1:y2] = False
            lights_b[x1:x2, y1:y2] -= 1
            lights_b.clip(min=0, out=lights_b)
        elif cmd == "toggle":
            lights_a[x1:x2, y1:y2] = lights_a[x1:x2, y1:y2] ^ True
            lights_b[x1:x2, y1:y2] += 2

    return str(sum(sum(lights_a))), str(sum(sum(lights_b)))



if __name__ == "__main__":
    p = Puzzle(year=2015, day=6)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
