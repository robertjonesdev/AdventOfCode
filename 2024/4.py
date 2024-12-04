from aocd.models import Puzzle
from functools import reduce
from collections import Counter

YEAR = 2024
DAY = 4
SEARCH_WORD = "XMAS"

TEST_DATA = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def parse(data: str):
    """Parse input."""
    # no parsing
    # return data
    return [list(line) for line in data.splitlines()]
    # String rows to list
    # return data.splitlines()
    # Integer rows to list
    # return [list(map(int, line.split())) for line in data.splitlines()]
    # Columns to Rows
    # return list(zip(*(map(int, line.split()) for line in data.splitlines())))


def part1(data):
    """Solve part 1."""

    word_count = 0
    y_max = len(data)
    for y, row in enumerate(data):
        x_max = len(row)
        for x, char in enumerate(row):
            if char == "X":
                # right
                if x < (x_max - 3):
                    word = f"{data[y][x]}{data[y][x+1]}{data[y][x+2]}{data[y][x+3]}"
                    if word == SEARCH_WORD:
                        word_count += 1
                    # diagonal up
                    if y >= 3:
                        word = f"{data[y][x]}{data[y-1][x+1]}{data[y-2][x+2]}{data[y-3][x+3]}"
                        if word == SEARCH_WORD:
                            word_count += 1
                    # diagonal down
                    if y < (y_max - 3):
                        word = f"{data[y][x]}{data[y+1][x+1]}{data[y+2][x+2]}{data[y+3][x+3]}"
                        if word == SEARCH_WORD:
                            word_count += 1

                # to the left, backwards
                if x >= 3:
                    word = f"{data[y][x]}{data[y][x-1]}{data[y][x-2]}{data[y][x-3]}"
                    if word == SEARCH_WORD:
                        word_count += 1
                    # diagonal up, backwards
                    if y >= 3:
                        word = f"{data[y][x]}{data[y-1][x-1]}{data[y-2][x-2]}{data[y-3][x-3]}"
                        if word == SEARCH_WORD:
                            word_count += 1
                    # diagonal down, backwards
                    if y < (y_max - 3):
                        word = f"{data[y][x]}{data[y+1][x-1]}{data[y+2][x-2]}{data[y+3][x-3]}"
                        if word == SEARCH_WORD:
                            word_count += 1
                # up
                if y >= 3:
                    word = f"{data[y][x]}{data[y-1][x]}{data[y-2][x]}{data[y-3][x]}"
                    if word == SEARCH_WORD:
                        word_count += 1

                # down
                if y < (y_max - 3):
                    word = f"{data[y][x]}{data[y+1][x]}{data[y+2][x]}{data[y+3][x]}"
                    if word == SEARCH_WORD:
                        word_count += 1

    return word_count


def part2(data):
    """Solve part 2."""
    word_count = 0
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[y]) - 1):
            if data[y][x] == "A":
                set1 = {data[y - 1][x - 1], data[y + 1][x + 1]}
                set2 = {data[y - 1][x + 1], data[y + 1][x - 1]}
                if set1 == {"S", "M"} and set2 == {"S", "M"}:
                    word_count += 1
    return word_count


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)

    # solution1, solution2 = solve(TEST_DATA)
    solution1, solution2 = solve(puzzle.input_data)

    print(f"Part 1 Solution: {solution1}")
    print(f"Part 2 Solution: {solution2}")
