from aoc_tribbe.aoc2015 import d18

example_a = """\
.#.#.#
...##.
#....#
..#...
#.#..#
####.."""


def test_gif_a():
    parta, partb = d18.solve(example_a, 4)
    assert parta == "4"


def test_gif_b():
    parta, partb = d18.solve(example_a, 5)
    assert partb == "17"
