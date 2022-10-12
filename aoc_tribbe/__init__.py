import sys
import importlib as il

def plugin(year, day, data):
    mod_name = "aoc_tribbe.aoc{}.d{:02d}".format(year, day)

    aoc_solution = il.import_module(mod_name)
    parta, partb = aoc_solution.solve(data)

    return parta, partb
