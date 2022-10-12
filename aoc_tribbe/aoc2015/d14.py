import re
from collections import defaultdict

from aocd.models import Puzzle, User


def get_distance(speed, duration, rest, race_length):
    iterations, remainder = divmod(race_length, duration + rest)
    distance = iterations * speed * duration + min(duration, remainder) * speed
    return distance


def get_points(reindeers, race_length):
    points = defaultdict(int)
    for s in range(1, race_length + 1):
        standings = dict()

        for deer in reindeers:
            distance = get_distance(reindeers[deer]["speed"], reindeers[deer]["duration"], reindeers[deer]["rest"], s)
            if distance in standings:
                standings[distance].append(deer)
            else:
                standings[distance] = [deer]

        for deer in standings[max(standings)]:
            points[deer] += 1

    return points


def solve(data):
    lines = data.splitlines()
    reindeers = defaultdict(dict)

    for line in lines:
        match = re.search(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line)
        reindeer, speed, duration, rest = match.groups()
        reindeers[reindeer] = {
            "speed": int(speed),
            "duration": int(duration),
            "rest": int(rest),
        }

    parta = max(get_distance(deer["speed"], deer["duration"], deer["rest"], 2503) for deer in reindeers.values())
    partb = max(get_points(reindeers, 2503).values())

    return str(parta), str(partb)



if __name__ == "__main__":
    p = Puzzle(year=2015, day=14, user=User.from_id("gsuite"))
    #p = Puzzle(year=2015, day=14)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
