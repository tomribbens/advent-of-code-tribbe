import re

from aocd.models import Puzzle


def calculate_nth_number(n):
    number = 20151125
    n -= 1
    while n:
        number = (number * 252533) % 33554393
        n -= 1

    return number


def calculate_n_from_table_pos(row, col):
    n = 0
    adding = 1
    for _ in range(col):
        n += adding
        adding += 1

    adding = col

    for _ in range(row - 1):
        n += adding
        adding += 1

    return n


def solve(data):
    match = re.search(r"To continue, please consult the code grid in the manual.  Enter the code at row (\d+), column (\d+).", data)
    row, col = match.groups()
    row, col = int(row), int(col)
    n = calculate_n_from_table_pos(row, col)
    parta = calculate_nth_number(n)

    return str(parta), None



if __name__ == "__main__":
    p = Puzzle(year=2015, day=25)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
