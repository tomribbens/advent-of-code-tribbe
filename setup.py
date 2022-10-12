from setuptools import setup

setup(
    entry_points={"adventofcode.user": ["tribbe = aoc_tribbe:plugin"]},
)