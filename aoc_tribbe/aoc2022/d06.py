from aocd.models import Puzzle


def get_marker_end_index(line: str, marker_length: int) -> int:
    """Returns the  index of the last character of character marker with marker_length which contains
    all different characters"""
    for i in range(marker_length, len(line)):
        candidate_marker = set(line[i - marker_length : i])
        if len(candidate_marker) == marker_length:
            return i


def solve(data: str) -> tuple[str, str]:
    return str(get_marker_end_index(data, 4)), str(get_marker_end_index(data, 14))


if __name__ == "__main__":
    p = Puzzle(year=2022, day=6)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
