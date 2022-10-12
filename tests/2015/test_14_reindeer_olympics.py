from aoc_tribbe.aoc2015.d14 import get_distance


def test_distance_race():
    assert get_distance(14, 10, 127, 1000) == 1120
    assert get_distance(16, 11, 162, 1000) == 1056

