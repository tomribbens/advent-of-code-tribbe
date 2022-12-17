import networkx as nx
from itertools import permutations, combinations
from aocd.models import Puzzle
from dataclasses import dataclass
from time import time

from aoc_tribbe.utils.parse import ints


@dataclass
class CaveSystem:
    minute: int
    position: str
    opened: set[str]
    total_release: int


@dataclass
class CaveSystemWithElephant:
    minute: int
    my_position: str
    my_reached_at: int
    elephant_position: str
    elephant_reached_at: int
    opened: set[str]
    total_release: int


def ideal_extra_release(
    minutes_remaining: int, unopened: set[str], valves: dict[str, int], elephant=False
) -> int:
    flow_rates = [valves[valve] for valve in unopened]
    flow_rates.sort(reverse=True)
    total = 0
    for i, rate in enumerate(flow_rates, start=1):
        total += rate * minutes_remaining
        minutes_remaining -= 2 if not elephant or i % 2 else 0
        if minutes_remaining <= 0:
            break

    return total


def solve(data: str) -> tuple[str, str]:
    valves: dict[str, int] = {}
    graph = nx.Graph()
    for line in data.splitlines():
        valve = line[6:8]
        flowrate = ints(line)[0]

        if line[-8:-3] == "valve":
            connections = [line[-2:]]
        else:
            connections = line.split("valves ")[1].split(", ")

        for connection in connections:
            graph.add_edge(valve, connection)

        if flowrate:
            valves[valve] = flowrate

    distances = {k: v for k, v in nx.shortest_path_length(graph)}

    max_release = part_a(distances, valves)
    max_release_b = part_b(distances, valves)

    return str(max_release), str(max_release_b)


def part_a(distances, valves):
    start = CaveSystem(1, "AA", set(), 0)
    stack = [start]
    max_release = 0
    while stack:
        current = stack.pop()
        unopened = set(valves.keys()) - current.opened

        max_potential = current.total_release + ideal_extra_release(
            30 - current.minute, unopened, valves
        )
        if max_potential <= max_release:
            continue

        modified_distances_to_unopened = get_list_of_targets(
            current.position, current.minute, distances, unopened, valves, 30
        )

        if not modified_distances_to_unopened:
            if current.total_release > max_release:
                max_release = current.total_release
            continue

        for _, distance, valve in modified_distances_to_unopened:
            stack.append(
                CaveSystem(
                    current.minute + distance + 1,
                    valve,
                    current.opened | {valve},
                    current.total_release
                    + valves[valve] * (30 - current.minute - distance),
                )
            )
    return max_release


def get_list_of_targets(
    current_position,
    current_time,
    distances: dict[str, dict[str, int]],
    unopened,
    valves,
    time_limit: int,
):
    modified_distances_to_unopened = []
    for valve in unopened:
        distance = distances[current_position][valve]
        if distance + current_time > time_limit:
            continue
        modified_distances_to_unopened.append(
            (valves[valve] - distance, distance, valve)
        )
    modified_distances_to_unopened.sort()
    return modified_distances_to_unopened


def part_b(distances, valves):
    start = CaveSystemWithElephant(1, "AA", 1, "AA", 1, set(), 0)
    stack = [start]
    max_release = 0

    while stack:
        current = stack.pop()
        unopened = set(valves.keys()) - current.opened

        max_potential = current.total_release + ideal_extra_release(
            26 - current.minute,
            unopened,
            valves,
            elephant=True if current.elephant_position is not None else False,
        )
        if max_potential <= max_release:
            continue

        if current.minute == current.my_reached_at == current.elephant_reached_at:
            something_added = False
            unopened_list = list(unopened)
            unopened_list.sort(key=lambda x: valves[x])
            f = (
                combinations
                if current.my_position == current.elephant_position
                else permutations
            )
            for my_next_destination, elephant_next_destination in f(unopened_list, 2):
                my_next_distance = distances[current.my_position][my_next_destination]
                elephant_next_distance = distances[current.elephant_position][
                    elephant_next_destination
                ]
                if (
                    current.minute + my_next_distance > 26
                    or current.minute + elephant_next_distance > 26
                ):
                    continue

                first_stop = min(my_next_distance, elephant_next_distance)
                stack.append(
                    CaveSystemWithElephant(
                        current.minute + first_stop + 1,
                        my_next_destination,
                        current.minute + my_next_distance + 1,
                        elephant_next_destination,
                        current.minute + elephant_next_distance + 1,
                        current.opened
                        | {my_next_destination, elephant_next_destination},
                        current.total_release
                        + valves[my_next_destination]
                        * (26 - current.minute - my_next_distance)
                        + valves[elephant_next_destination]
                        * (26 - current.minute - elephant_next_distance),
                    )
                )
                something_added = True

            for my_next_destination in unopened:
                my_next_distance = distances[current.my_position][my_next_destination]
                if current.minute + my_next_distance > 26:
                    continue

                stack.append(
                    CaveSystemWithElephant(
                        current.minute + my_next_distance + 1,
                        my_next_destination,
                        current.minute + my_next_distance + 1,
                        None,
                        -1,
                        current.opened | {my_next_destination},
                        current.total_release
                        + valves[my_next_destination]
                        * (26 - current.minute - my_next_distance),
                    )
                )
                something_added = True
            if not something_added and current.total_release > max_release:
                max_release = current.total_release
            continue

        if current.minute == current.my_reached_at:
            modified_distances_to_unopened = get_list_of_targets(
                current.my_position, current.minute, distances, unopened, valves, 26
            )
            if not modified_distances_to_unopened:
                if current.elephant_reached_at > current.minute:
                    stack.append(
                        CaveSystemWithElephant(
                            current.elephant_reached_at,
                            None,
                            -1,
                            current.elephant_position,
                            current.elephant_reached_at,
                            current.opened,
                            current.total_release,
                        )
                    )
                    continue
                elif max_release < current.total_release:
                    max_release = current.total_release
                    continue

            for (
                _,
                my_next_distance,
                my_next_destination,
            ) in modified_distances_to_unopened:
                stack.append(
                    CaveSystemWithElephant(
                        min(
                            current.elephant_reached_at
                            if current.elephant_reached_at > 0
                            else 3000,
                            current.minute + my_next_distance + 1,
                        ),
                        my_next_destination,
                        current.minute + my_next_distance + 1,
                        current.elephant_position,
                        current.elephant_reached_at,
                        current.opened | {my_next_destination},
                        current.total_release
                        + valves[my_next_destination]
                        * (26 - current.minute - my_next_distance),
                    )
                )

        if current.minute == current.elephant_reached_at:
            modified_distances_to_unopened = get_list_of_targets(
                current.elephant_position,
                current.minute,
                distances,
                unopened,
                valves,
                26,
            )
            if not modified_distances_to_unopened:
                if max_release < current.total_release:
                    max_release = current.total_release
                    continue

            for (
                _,
                elephant_next_distance,
                elephant_next_destination,
            ) in modified_distances_to_unopened:
                stack.append(
                    CaveSystemWithElephant(
                        min(
                            current.my_reached_at
                            if current.my_reached_at > 0
                            else 3000,
                            current.minute + elephant_next_distance + 1,
                        ),
                        current.my_position,
                        current.my_reached_at,
                        elephant_next_destination,
                        current.minute + elephant_next_distance + 1,
                        current.opened | {elephant_next_destination},
                        current.total_release
                        + valves[elephant_next_destination]
                        * (26 - current.minute - elephant_next_distance),
                    )
                )
    return max_release


if __name__ == "__main__":
    p = Puzzle(year=2022, day=16)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
