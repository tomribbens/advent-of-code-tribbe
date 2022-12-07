from __future__ import annotations
from aocd.models import Puzzle
from dataclasses import dataclass


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    parent: Directory | None
    contents: list[File | Directory]

    @property
    def size(self) -> int:
        total_size = 0
        for entry in self.contents:
            total_size += entry.size
        return total_size

    def get_or_create_subdir(self, dirname: str):
        for entry in self.contents:
            if isinstance(entry, Directory) and entry.name == dirname:
                return entry
        new_dir = Directory(dirname, self, [])
        self.contents.append(new_dir)
        return new_dir

    def get_full_dir_tree(self) -> list[Directory]:
        dirlist = [self]
        for entry in self.contents:
            if isinstance(entry, Directory):
                dirlist.extend(entry.get_full_dir_tree())
        return dirlist


def solve(data: str) -> tuple[str, str]:
    root = Directory("", None, [])
    cwd = root

    for line in data.splitlines():
        if line[0] == "$":
            command = line[2:].split(" ")
            if command[0] == "cd":
                if command[1] == "/":
                    continue

                if command[1] == "..":
                    cwd = cwd.parent
                    continue

                cwd = cwd.get_or_create_subdir(command[1])

        elif line[0].isdigit():
            size, name = line.split(" ")
            cwd.contents.append(File(name, int(size)))

    part_a = sum(
        entry.size for entry in root.get_full_dir_tree() if entry.size <= 100000
    )
    minimum_size_to_free = 30_000_000 - (70_000_000 - root.size)
    part_b = min(
        entry.size
        for entry in root.get_full_dir_tree()
        if entry.size >= minimum_size_to_free
    )

    return str(part_a), str(part_b)


if __name__ == "__main__":
    p = Puzzle(year=2022, day=7)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
