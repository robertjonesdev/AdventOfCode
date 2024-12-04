from aocd.models import Puzzle
from functools import reduce
from collections import Counter
import re

YEAR = 2024
DAY = 3

TEST_DATA = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


def parse(data: str):
    """Parse input."""
    # no parsing
    return data
    # String rows to list
    # return data.splitlines()
    # Integer rows to list
    # return [list(map(int, line.split())) for line in data.splitlines()]
    # Columns to Rows
    # return list(zip(*(map(int, line.split()) for line in data.splitlines())))


def part1(data):
    """Solve part 1."""
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    return sum(map(lambda x: int(x[0]) * int(x[1]), re.findall(pattern, data)))


def part2(data):
    """Solve part 2."""
    pass


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)

    solution1, solution2 = solve(puzzle.input_data)

    print(f"Part 1 Solution: {solution1}")
    print(f"Part 2 Solution: {solution2}")
