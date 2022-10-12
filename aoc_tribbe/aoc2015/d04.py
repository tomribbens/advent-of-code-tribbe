import hashlib

from aocd.models import Puzzle


def solve(input_data):
    salt = 0

    candidate = input_data + str(salt)

    result = hashlib.md5(candidate.encode())

    while result.hexdigest()[0:5] != "00000":
        salt += 1
        candidate = input_data + str(salt)
        result = hashlib.md5(candidate.encode())

    parta = salt

    while result.hexdigest()[0:6] != "000000":
        salt += 1
        candidate = input_data + str(salt)
        result = hashlib.md5(candidate.encode())


    return str(parta), str(salt)



if __name__ == "__main__":
    p = Puzzle(year=2015, day=4)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
