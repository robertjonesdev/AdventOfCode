from aocd.models import Puzzle

YEAR = 2024
DAY = 10

TEST_DATA = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def parse(data: str):
    """Parse input."""
    grid = dict()
    for row_idx, row in enumerate(data.splitlines()):
        for col_idx, col in enumerate(list(row)):
            grid[(int(row_idx), int(col_idx))] = int(col)
    return grid


def part_1_dfs(grid, row, col, search_val, visited: set):
    key = (row, col)
    if key not in grid:
        return 0
    if grid[key] != search_val:
        return 0

    if search_val == 9 and grid[key] == 9:
        if key not in visited:
            visited.add(key)
            return 1
        return 0

    return (
        part_1_dfs(grid, row + 1, col, search_val + 1, visited)
        + part_1_dfs(grid, row, col + 1, search_val + 1, visited)
        + part_1_dfs(grid, row - 1, col, search_val + 1, visited)
        + part_1_dfs(grid, row, col - 1, search_val + 1, visited)
    )


def part_2_dfs(grid, row, col, search_val):
    key = (row, col)
    if key not in grid:
        return 0
    if grid[key] != search_val:
        return 0
    if search_val == 9 and grid[key] == 9:
        return 1

    return (
        part_2_dfs(grid, row + 1, col, search_val + 1)
        + part_2_dfs(grid, row, col + 1, search_val + 1)
        + part_2_dfs(grid, row - 1, col, search_val + 1)
        + part_2_dfs(grid, row, col - 1, search_val + 1)
    )


def part1(data: dict):
    """Solve part 1."""
    total = 0
    for (row, col), val in data.items():
        if val == 0:
            visited = set()
            total += part_1_dfs(data, row, col, val, visited)

    return total


def part2(data):
    """Solve part 2."""
    total = 0
    for (row, col), val in data.items():
        if val == 0:
            total += part_2_dfs(data, row, col, val)
    return total


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
