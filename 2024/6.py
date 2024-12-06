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

# Globals
right_bound = 0
down_bound = 0
game_board = None
start_pos = (-1, -1)


def parse(data: str):
    """Parse input."""
    global game_board
    game_board = [list(line) for line in data.splitlines()]

    global right_bound
    right_bound = len(game_board[0])

    global down_bound
    down_bound = len(game_board)

    global start_pos
    start_pos = find_start(game_board)
    return


def find_start(data):
    for row_idx, row in enumerate(data):
        for col_idx, char in enumerate(row):
            if char == "^":
                return row_idx, col_idx


# Up-0, Right-1, Down-2, Left-3
directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}


def turn_right(direction):
    return (direction + 1) % 4


def inbounds(x, y):
    return 0 <= x < down_bound and 0 <= y < right_bound


def traverse_map(obstacle=None):

    row_pos, col_pos = start_pos
    direction = 0
    visited = set()
    visited_direction = set()

    while inbounds(row_pos, col_pos):
        visited.add((row_pos, col_pos))

        d_row, d_col = directions[direction]
        n_row, n_col = row_pos + d_row, col_pos + d_col

        if inbounds(n_row, n_col) and (
            game_board[n_row][n_col] == "#" or (obstacle and (n_row, n_col) == obstacle)
        ):
            direction = turn_right(direction)
        else:
            row_pos, col_pos = n_row, n_col

        visited_with_direction = (row_pos, col_pos, direction)
        if visited_with_direction in visited_direction:
            return True, visited
        visited_direction.add(visited_with_direction)

    return False, visited


def part1():
    """Solve part 1."""
    return traverse_map()[1]


def part2(visited):
    """Solve part 2."""
    obstacle_count = 0
    obstacles = visited - {start_pos}
    for obstacle in obstacles:
        if traverse_map(obstacle)[0]:
            obstacle_count += 1
    return obstacle_count


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    parse(puzzle_input)
    visited = part1()
    solution1 = len(visited)
    solution2 = part2(visited)

    return solution1, solution2


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)

    solution1, solution2 = solve(puzzle.input_data)

    print(f"Part 1 Solution: {solution1}")
    print(f"Part 2 Solution: {solution2}")
