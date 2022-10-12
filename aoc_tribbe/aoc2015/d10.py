from aocd.models import Puzzle


def look_and_say(input_data, n=1):
    for _ in range(n):
        prev = input_data[0]
        count = 1
        new_input = ""
        for char in input_data[1:]:
            if char == prev:
                count += 1
            else:
                new_input += str(count) + prev
                prev = char
                count = 1

        new_input += str(count) + prev

        input_data = new_input

    return input_data


def solve(input_data):
    return str(len(look_and_say(input_data, n=40))), str(len(look_and_say(input_data, n=50)))


if __name__ == "__main__":
    p = Puzzle(year=2015, day=10)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
