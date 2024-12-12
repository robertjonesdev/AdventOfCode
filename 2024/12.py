from aocd.models import Puzzle
from collections import deque, defaultdict


YEAR = 2024
DAY = 12

TEST_DATA = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""


def parse(data: str):
    """Parse input."""
    return [list(line) for line in data.splitlines()]


def is_valid(rows, cols, r, c):
    return 0 <= r < rows and 0 <= c < cols


def bfs(grid, visited, r, c):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(r, c)])
    visited[r][c] = True
    char = grid[r][c]
    perimeter = 0
    area = 0

    while queue:
        x, y = queue.popleft()
        area += 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if not is_valid(rows, cols, nx, ny) or grid[nx][ny] != char:
                perimeter += 1
            elif not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return perimeter, area


def part1(data):
    """Solve part 1."""
    rows, cols = len(data), len(data[0])
    visited = [[False] * cols for _ in range(rows)]

    total = 0
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                perimeter, area = bfs(data, visited, r, c)
                total += perimeter * area
    return total


def count_sides(sides: dict):
    count = 0
    for key, value_set in sides.items():
        sorted_values = sorted(value_set)
        previous = None
        for current in sorted_values:
            if previous is None or current != previous + 1:
                count += 1
            previous = current
    return count


def bfs2(grid, visited, r, c):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(r, c)])
    visited[r][c] = True
    char = grid[r][c]
    edges = defaultdict(set)
    area = 0

    while queue:
        x, y = queue.popleft()
        area += 1

        for dir, dx, dy in [(0, -1, 0), (1, 1, 0), (2, 0, -1), (3, 0, 1)]:
            nx, ny = x + dx, y + dy

            if not is_valid(rows, cols, nx, ny) or grid[nx][ny] != char:
                if dir == 0 or dir == 1:
                    edges[(dir, nx)].add(ny)
                else:
                    edges[(dir, ny)].add(nx)
            elif not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

    sides = count_sides(edges)
    return sides, area


def part2(data):
    """Solve part 2."""
    rows, cols = len(data), len(data[0])
    visited = [[False] * cols for _ in range(rows)]

    total = 0
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                sides, area = bfs2(data, visited, r, c)
                total += sides * area
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
