import re

from aocd.models import Puzzle, User


def reduce(target, substitutions):
    stack = {target: 0}
    invalid_solution = set()
    solution = None

    while stack:
        step = min(stack, key=len)
        count = stack.pop(step)

        if solution and solution < count + 1:
            continue

        has_valid_next_step = False
        for dst, src in substitutions:
            for m in re.finditer(src, step):
                new_step = step[:m.start()] + dst + step[m.end():]
                if new_step in invalid_solution:
                    continue

                has_valid_next_step = True
                if new_step == "e":
                    return count + 1
                elif new_step.count('e') < 1:
                    if new_step not in stack or stack[new_step] > count + 1:
                        stack[new_step] = count + 1
                else:
                    invalid_solution.add(step)

        if not has_valid_next_step:
            invalid_solution.add(step)

def solve_wim(element, tri):
    replacements = 0
    while element != "e":
        pos = {}
        for k, v in tri.items():
            delta = len(k) - len(v)
            if k in element:
                if v != "e" or len(element) - delta == 1:
                    pos[k] = (element.rfind(k) + len(k), delta)
        k = max(pos, key=pos.get)
        v = tri[k]
        # replace from right
        element = element[::-1].replace(k[::-1], v[::-1], 1)[::-1]
        replacements += 1

    return replacements


def solve(data):
    lines = data.splitlines()
    target = lines.pop()
    lines.pop()
    substitutions = list()
    generated_molecules = set()

    for line in lines:
        src, dst = line.split(" => ")
        substitutions.append((src, dst))

    for src, dst in substitutions:
        for match in re.finditer(src, target):
            generated_molecules.add(target[:match.start()] + dst + target[match.end():])

    tri = {}
    for dst, src in substitutions:
        tri[src] = dst

    parta = len(generated_molecules)
    #partb = reduce(target, substitutions)
    partb = solve_wim(target, tri)

    return str(parta), str(partb)


if __name__ == "__main__":
    p = Puzzle(year=2015, day=19)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
