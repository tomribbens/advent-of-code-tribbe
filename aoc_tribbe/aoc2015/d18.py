import numpy as np

from aocd.models import Puzzle


def next_generation(lights, force_corners_on=False):
    w, h = lights.shape
    new_gen = np.zeros((w, h), dtype=bool)
    for x in range(w):
        for y in range(h):
            if lights[x, y] and lights[max(x-1,0):min(x+2,w), max(y-1,0):min(y+2,h)].sum() in [3, 4]:
                new_gen[x, y] = True
            elif not lights[x, y] and lights[max(x-1,0):min(x+2,w), max(y-1,0):min(y+2,h)].sum() == 3:
                new_gen[x, y] = True

    if force_corners_on:
        new_gen[0,0] = True
        new_gen[w-1,h-1] = True
        new_gen[0,h-1] = True
        new_gen[w-1,0] = True

    return new_gen


def solve(data, iterations=100):
    lines = data.splitlines()
    lights = np.zeros((len(lines), len(lines[0])), dtype=bool)
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == "#":
                lights[x,y] = True

    lights_a = lights
    lights_b = np.copy(lights)
    lights_b[0,0] = True
    lights_b[len(lines)-1, 0] = True
    lights_b[0, len(lines[0])-1] = True
    lights_b[len(lines)-1, len(lines[0])-1] = True
    for _ in range(iterations):
        lights_a = next_generation(lights_a)
        lights_b = next_generation(lights_b, force_corners_on=True)

    parta = lights_a.sum()
    partb = lights_b.sum()

    return str(parta), str(partb)


if __name__ == "__main__":
    p = Puzzle(year=2015, day=18)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
