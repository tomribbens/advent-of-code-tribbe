import re


def mapt(fn, *args) -> tuple:
    """map(fn, *args) and return the result as a tuple."""
    return tuple(map(fn, *args))


def ints(line: str, signed: bool = True) -> tuple[int]:
    """takes a string, and returns all numbers from it as ints in a tuple"""
    if signed:
        return mapt(int, re.findall(r"-?[0-9]+", line))
    else:
        return mapt(int, re.findall(r"[0-9]+", line))