from itertools import product

from aocd.models import Puzzle


def computer(instructions, registera = 0, registerb = 0):
    pointer = 0
    registers = {
        "a": registera,
        "b": registerb,
    }

    while pointer < len(instructions):
        current_instruction = instructions[pointer][0:3]
        match current_instruction:
            case "hlf":
                register = instructions[pointer][4]
                registers[register] = registers[register] // 2
                pointer += 1
            case "tpl":
                register = instructions[pointer][4]
                registers[register] = registers[register] * 3
                pointer += 1
            case "inc":
                register = instructions[pointer][4]
                registers[register] = registers[register] + 1
                pointer += 1
            case "jmp":
                offset = int(instructions[pointer][4:])
                pointer += offset
            case "jie":
                register = instructions[pointer][4]
                offset = int(instructions[pointer][7:])
                if registers[register] % 2 == 0:
                    pointer += offset
                else:
                    pointer += 1
            case "jio":
                register = instructions[pointer][4]
                offset = int(instructions[pointer][7:])
                if registers[register] == 1:
                    pointer += offset
                else:
                    pointer += 1

    return registers

def solve(data):
    instructions = data.splitlines()

    registers = computer(instructions)
    parta = registers["b"]
    registers = computer(instructions, registera=1)
    partb = registers["b"]
    return str(parta), str(partb)



if __name__ == "__main__":
    p = Puzzle(year=2015, day=23)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
