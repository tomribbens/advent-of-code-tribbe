from aocd.models import Puzzle


def solve(input_data):
    location_a = [0, 0]
    location_b1 = [0, 0]
    location_b2 = [0, 0]
    visited_a = set()
    visited_b = set()
    visited_a.add(tuple(location_a))
    visited_b.add(tuple(location_b1))

    for number, direction in enumerate(input_data):
        if direction == '>':
            location_a[0] += 1
            if number % 2:
                location_b1[0] += 1
            else:
                location_b2[0] += 1
        elif direction == '<':
            location_a[0] -= 1
            if number % 2:
                location_b1[0] -= 1
            else:
                location_b2[0] -= 1
        elif direction == 'v':
            location_a[1] -= 1
            if number % 2:
                location_b1[1] -= 1
            else:
                location_b2[1] -= 1
        elif direction == '^':
            location_a[1] += 1
            if number % 2:
                location_b1[1] += 1
            else:
                location_b2[1] += 1

        visited_a.add(tuple(location_a))
        visited_b.add(tuple(location_b1))
        visited_b.add(tuple(location_b2))

    return str(len(visited_a)), str(len(visited_b))


if __name__ == "__main__":
    p = Puzzle(year=2015, day=3)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
