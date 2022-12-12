from aocd.models import Puzzle
import numpy as np
import networkx as nx


def solve(data: str) -> tuple[str, str]:
    heightmap = np.genfromtxt(data.splitlines(), dtype=str, delimiter=1)
    graph = nx.MultiDiGraph()
    start = list(zip(*np.where(heightmap == "S")))[0]
    heightmap[heightmap == "S"] = "a"
    end = list(zip(*np.where(heightmap == "E")))[0]
    heightmap[heightmap == "E"] = "z"

    it = np.nditer(heightmap, flags=["multi_index"])
    for node in it:
        col, row = it.multi_index
        candidates = []
        candidates.append((col, row + 1)) if row + 1 < heightmap.shape[1] else None
        candidates.append((col, row - 1)) if row - 1 >= 0 else None
        candidates.append((col + 1, row)) if col + 1 < heightmap.shape[0] else None
        candidates.append((col - 1, row)) if col - 1 >= 0 else None

        for candidate in candidates:
            if ord(str(node)) + 1 >= ord(heightmap[candidate]):
                graph.add_edge((col, row), candidate)

    possible_starting_locations = list(zip(*np.where(heightmap == "a")))
    distances = []
    for start_option in possible_starting_locations:
        try:
            distances.append(nx.shortest_path_length(graph, start_option, end))
        except nx.NetworkXNoPath:
            pass

    return str(nx.shortest_path_length(graph, start, end)), str(min(distances))


if __name__ == "__main__":
    p = Puzzle(year=2022, day=12)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
