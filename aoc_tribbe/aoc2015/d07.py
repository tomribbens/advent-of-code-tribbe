from aocd.models import Puzzle


def compute(input_data: str, overrides={}):
    lines = input_data.splitlines()
    solution = dict()
    commands = []

    for line in lines:
        data, output = line.split(' -> ')
        cmd = data.split(' ')
        if len(cmd) == 1:
            cmd = ["STORE", cmd[0]]
        elif len(cmd) == 3:
            cmd = [cmd[1], cmd[0], cmd[2]]

        commands.append((cmd, output))


    while commands:
        cmd, out = commands.pop(0)
        if out in overrides:
            solution[out] = overrides[out]
            continue

        if cmd[1] in solution.keys():
            cmd[1] = solution[cmd[1]]
        if len(cmd) == 3 and cmd[2] in solution.keys():
            cmd[2] = solution[cmd[2]]

        if (isinstance(cmd[1], int) or cmd[1].isnumeric()) and (len(cmd) < 3 or (isinstance(cmd[2], int) or cmd[2].isnumeric())):
            if cmd[0] == "STORE":
                solution[out] = int(cmd[1])
            elif cmd[0] == "NOT":
                solution[out] = ~ int(cmd[1]) & 0xFFFF
            elif cmd[0] == "OR":
                solution[out] = int(cmd[1]) | int(cmd[2])
            elif cmd[0] == "AND":
                solution[out] = int(cmd[1]) & int(cmd[2])
            elif cmd[0] == "LSHIFT":
                solution[out] = int(cmd[1]) << int(cmd[2])
            elif cmd[0] == "RSHIFT":
                solution[out] = int(cmd[1]) >> int(cmd[2])
        else:
            commands.append((cmd, out))

    return solution

def solve(input_data):
    solution_a = compute(input_data)['a']
    solution_b = compute(input_data, overrides={'b': solution_a})['a']
    return str(solution_a), str(solution_b)


if __name__ == "__main__":
    p = Puzzle(year=2015, day=7)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
