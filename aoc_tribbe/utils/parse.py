import re


def mapt(fn, *args) -> tuple:
    """map(fn, *args) and return the result as a tuple."""
    return tuple(map(fn, *args))


def ints(line: str, signed: bool = True) -> tuple[int, ...]:
    """takes a string, and returns all numbers from it as ints in a tuple"""
    if signed:
        return mapt(int, re.findall(r"-?[0-9]+", line))
    else:
        return mapt(int, re.findall(r"[0-9]+", line))


def atoms(line: str) -> tuple[str, ...]:
    """takes a string, and returns all atoms from it as strings in a tuple"""
    return mapt(str, re.findall(r"[a-zA-Z]+", line))


def floats(line: str) -> tuple[float, ...]:
    """takes a string, and returns all numbers from it as floats in a tuple"""
    return mapt(float, re.findall(r"-?[0-9]+\.[0-9]+", line))


def intify(line: str) -> int | str:
    """Converts a string to an int if possible, otherwise returns the string."""
    try:
        return int(line)
    except ValueError:
        return line


def atoms_or_ints(line: str) -> tuple[str | int, ...]:
    """takes a string, and returns all atoms and numbers from it as strings or ints in a tuple"""
    return mapt(intify, re.findall(r"[a-zA-Z]+|-?[0-9]+", line))


def str_ordinal_to_int(ordinal: str) -> int:
    """Converts an ordinal number to an int. first -> 1, second -> 2, etc."""
    translation_dict = {
        "first": 1,
        "second": 2,
        "third": 3,
        "fourth": 4,
        "fifth": 5,
        "sixth": 6,
        "seventh": 7,
        "eighth": 8,
        "ninth": 9,
        "tenth": 10,
    }
    return translation_dict[ordinal]
