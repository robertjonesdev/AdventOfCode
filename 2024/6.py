from aocd.models import Puzzle
from functools import reduce
from collections import Counter

YEAR = 2024
DAY = 6

TEST_DATA = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


def parse(data: str):
    """Parse input."""

    return [list(line) for line in data.splitlines()]


def find_start(data):
    for row_idx, row in enumerate(data):
        for col_idx, char in enumerate(row):
            if char == "^":
                return row_idx, col_idx


def part1(data):
    """Solve part 1."""
    right_bound = len(data[0]) - 1
    down_bound = len(data) - 1
    left_bound = 0
    up_bound = 0

    row_pos, col_pos = find_start(data)

    direction = "UP"
    continue_flag = True
    while continue_flag:
        data[row_pos][col_pos] = 1
        if direction == "UP":
            if row_pos > up_bound:
                row_pos -= 1
            else:
                continue_flag = False

            if data[row_pos][col_pos] == "#":
                direction = "RIGHT"
                row_pos += 1

        elif direction == "DOWN":
            if row_pos < down_bound:
                row_pos += 1
            else:
                continue_flag = False
            if data[row_pos][col_pos] == "#":
                direction = "LEFT"
                row_pos -= 1

        elif direction == "RIGHT":
            if col_pos < right_bound:
                col_pos += 1
            else:
                continue_flag = False
            if data[row_pos][col_pos] == "#":
                direction = "DOWN"
                col_pos -= 1

        elif direction == "LEFT":
            if col_pos > left_bound:
                col_pos -= 1
            else:
                continue_flag = False
            if data[row_pos][col_pos] == "#":
                direction = "UP"
                col_pos += 1

    return sum(visited for row in data for visited in row if isinstance(visited, int))


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
