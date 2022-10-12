from itertools import pairwise

from aocd.models import Puzzle


def is_nice_a(string):
    disallowed_strings = {'ab', 'cd', 'pq', 'xy'}
    vowels = {'a', 'e', 'i', 'o', 'u'}
    if any(disallowed in string for disallowed in disallowed_strings):
        return False

    if len([letter for letter in string if letter in vowels]) < 3:
        return False

    previous = ""
    for letter in string:
        if letter == previous:
            return True

        previous = letter

    return False

def is_nice_b(string):
    if not any([left == right for left, right in zip(string, string[2:])]):
        return False

    if not any([string.count(''.join(candidate)) >= 2 for candidate in pairwise(string)]):
        return False

    return True


def solve(input_data):
    lines = input_data.splitlines()

    nice_a = [is_nice_a(line) for line in lines].count(True)
    nice_b = [is_nice_b(line) for line in lines].count(True)


    return str(nice_a), str(nice_b)



if __name__ == "__main__":
    p = Puzzle(year=2015, day=5)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
