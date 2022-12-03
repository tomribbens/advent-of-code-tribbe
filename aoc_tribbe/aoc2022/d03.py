from aocd.models import Puzzle


def get_priority(char: str) -> int:
    if not isinstance(char, str) or len(char) > 1 or len(char) == 0:
        raise ValueError

    if char.islower():
        priority = ord(char) - ord("a") + 1
    else:
        priority = ord(char) - ord("A") + 27

    return priority


def solve(data: str) -> tuple[str, str]:
    total_priority = 0
    group_priority = 0
    three_rucksacks: dict[int, set] = {}
    for i, line in enumerate(data.splitlines()):
        items = len(line)
        half = items // 2
        three_rucksacks[i % 3] = set(line)
        compartment_1 = set(line[0:half])
        compartment_2 = set(line[half:])
        common = compartment_1.intersection(compartment_2)
        char = common.pop()
        total_priority += get_priority(char)

        if (i % 3) == 2:
            common = (
                three_rucksacks[0]
                .intersection(three_rucksacks[1])
                .intersection(three_rucksacks[2])
            )
            group_priority += get_priority(common.pop())

    return str(total_priority), str(group_priority)


if __name__ == "__main__":
    p = Puzzle(year=2022, day=3)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
