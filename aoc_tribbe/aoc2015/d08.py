from aocd.models import Puzzle


def solve(input_data):
    lines = input_data.splitlines()
    literals = 0
    values = 0
    expanded = 0

    for line in lines:
        assert line[0] == '"'
        assert line[-1] == '"'

        line = line[1:-1]
        literals += 2
        expanded += 6

        previous = ""
        for char in line:
            literals += 1
            if previous == '\\':
                if char in ['\\', '"']:
                    values += 1
                    expanded += 2
                    previous = ""
                elif char == "x":
                    previous = '\\x'
                    expanded += 1
            elif previous.startswith('\\x'):
                if len(previous) == 3:
                    values += 1
                    previous = ""
                    expanded += 1
                else:
                    previous += char
                    expanded += 1
            elif char == '\\':
                previous = '\\'
                expanded += 2
            else:
                values += 1
                expanded += 1

    return str(literals - values), str(expanded - literals)


if __name__ == "__main__":
    p = Puzzle(year=2015, day=8)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
