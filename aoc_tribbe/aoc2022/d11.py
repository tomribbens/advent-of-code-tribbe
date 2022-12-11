from aocd.models import Puzzle
from typing import Callable

from aoc_tribbe.utils.parse import ints


class Monkey:
    items: list[int]
    operation: Callable
    division_test: int
    division_action: dict[bool, int]
    inspected_items: int

    def __init__(self, description: list[str]):
        self.items = list(ints(description[0]))
        self.operation = eval(f"lambda old : {description[1].split(' = ')[1]}")
        self.division_test = ints(description[2])[0]
        self.division_action = {
            True: ints(description[3])[0],
            False: ints(description[4])[0],
        }
        self.inspected_items = 0

    def throw_items(self, divide=True) -> tuple[int, int]:
        while self.items:
            item = self.items.pop(0)
            item = self.operation(item)
            if divide:
                item = item // 3
            self.inspected_items += 1
            yield item, self.division_action[item % self.division_test == 0]


def solve(data: str) -> tuple[str, str]:
    monkey_descriptions = data.split("\n\n")
    monkeys = [
        Monkey(description.splitlines()[1:]) for description in monkey_descriptions
    ]

    for _ in range(20):
        for monkey in monkeys:
            for item, receiving_monkey in monkey.throw_items():
                monkeys[receiving_monkey].items.append(item)

    monkey_activity_a = sorted(
        [monkey.inspected_items for monkey in monkeys], reverse=True
    )

    monkeys = [
        Monkey(description.splitlines()[1:]) for description in monkey_descriptions
    ]
    max_worry = 1
    for factor in (monkey.division_test for monkey in monkeys):
        max_worry = max_worry * factor

    for _ in range(10000):
        for monkey in monkeys:
            for item, receiving_monkey in monkey.throw_items(divide=False):
                monkeys[receiving_monkey].items.append(item % max_worry)

    monkey_activity_b = sorted(
        [monkey.inspected_items for monkey in monkeys], reverse=True
    )

    return str(monkey_activity_a[0] * monkey_activity_a[1]), str(
        monkey_activity_b[0] * monkey_activity_b[1]
    )


if __name__ == "__main__":
    p = Puzzle(year=2022, day=11)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
