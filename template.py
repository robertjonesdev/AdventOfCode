from aocd.models import Puzzle
from functools import reduce
from collections import Counter

YEAR = 2024
DAY = 1


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
    pass


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
