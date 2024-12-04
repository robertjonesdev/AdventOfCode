from aocd.models import Puzzle
from functools import reduce
from collections import Counter

YEAR = 2024
DAY = 2


def parse(data: str):
    """Parse input."""
    return [list(map(int, line.split())) for line in data.splitlines()]


def is_linear(line):
    return all(l < r for l, r in zip(line, line[1:])) or all(
        l > r for l, r in zip(line, line[1:])
    )


def is_safe(line):
    return all(1 <= abs(l - r) <= 3 for l, r in zip(line, line[1:]))


def part1(data):
    """Solve part 1."""
    total_safe = 0
    for line in data:
        if is_linear(line) and is_safe(line):
            total_safe += 1
    return total_safe


def part2(data):
    """Solve part 2."""
    total_safe = 0
    for line in data:
        if is_linear(line) and is_safe(line):
            total_safe += 1
        else:
            for i in range(len(line)):
                sublist = line[:i] + line[i + 1 :]
                if is_linear(sublist) and is_safe(sublist):
                    total_safe += 1
                    break
    return total_safe


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
