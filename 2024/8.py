from aocd.models import Puzzle
from collections import defaultdict
import math
import itertools

YEAR = 2024
DAY = 8

TEST_DATA = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

TEST_DATA = """T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
.........."""

num_rows = 0
num_cols = 0


def print_grid(coordinates, grid_height, grid_width):
    for x in range(grid_height):
        for y in range(grid_width):
            if (x, y) in coordinates:
                print("#", end="")
            else:
                print(".", end="")
        print()


def parse(data: str):
    grid = defaultdict(set)

    global num_rows
    num_rows = len(data.splitlines())

    global num_cols
    num_cols = len(data.splitlines()[0])

    for row, line in enumerate(data.splitlines()):
        for col, item in enumerate(list(line)):
            if item != ".":
                grid[item].add((row, col))
    return grid


def in_bounds(point):
    row, col = point
    return 0 <= row < num_rows and 0 <= col < num_cols


def calculate_opposite_points(pointA, pointB):
    x1, y1 = pointA
    x2, y2 = pointB

    rise, run = y2 - y1, x2 - x1

    p1x, p1y = x1 - run, y1 - rise
    p2x, p2y = x2 + run, y2 + rise
    return (p1x, p1y), (p2x, p2y)


def part1(data):
    """Solve part 1."""
    unique_locations = set()

    for letter in data.values():
        for pointA, pointB in itertools.combinations(letter, 2):
            locationA, locationB = calculate_opposite_points(pointA, pointB)
            if locationA and in_bounds(locationA):
                unique_locations.add(locationA)
            if locationB and in_bounds(locationB):
                unique_locations.add(locationB)
    return len(unique_locations)


def part2(data):
    """Solve part 2."""
    unique_locations = set()

    for letter in data.values():
        for pointA, pointB in itertools.combinations(letter, 2):
            x1, y1 = pointA
            x2, y2 = pointB
            rise, run = y2 - y1, x2 - x1
            n = 1
            while True:
                p3 = (x2 + n * run, y2 + n * rise)
                p4 = (x1 - n * run, y1 - n * rise)

                if in_bounds(p3):
                    unique_locations.add(p3)
                if in_bounds(p4):
                    unique_locations.add(p4)

                unique_locations.add(pointA)
                unique_locations.add(pointB)

                if not in_bounds(p3) and not in_bounds(p4):
                    break

                n += 1

    return len(unique_locations)


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
