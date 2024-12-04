import os
from aocd.models import Puzzle
from functools import reduce
from collections import Counter

YEAR = 2024
DAY = 1


def parse(data: str):
    """Parse input."""
    return list(zip(*(map(int, line.split()) for line in data.splitlines())))


def part1(data):
    """Solve part 1."""
    left_col, right_col = data
    left_col = sorted(left_col)
    right_col = sorted(right_col)
    return reduce(lambda acc, x: acc + abs(x[0] - x[1]), zip(left_col, right_col), 0)


def part2(data):
    """Solve part 2."""
    left_col, right_col = data
    counter = Counter(right_col)
    return reduce(lambda acc, x: acc + (x * counter[x]), left_col, 0)


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
