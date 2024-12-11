from aocd.models import Puzzle
from collections import defaultdict


YEAR = 2024
DAY = 11

TEST_DATA = """125 17"""


def parse(data: str):
    """Parse input."""
    hashmap = defaultdict(int)
    for x in data.split(" "):
        hashmap[x] += 1
    return hashmap


def split(num):
    mid = len(num) // 2
    left = str(int(num[:mid]))
    right = str(int(num[mid:]))
    return left, right


def work(d1: defaultdict, count):
    for _ in range(count):
        d2 = defaultdict(int)
        for key, value in d1.items():
            if key == "0":
                d2["1"] += value
            elif len(key) % 2 == 0:
                left, right = split(key)
                d2[left] += value
                d2[right] += value
            else:
                d2[str(int(key) * 2024)] += value

        d1 = d2.copy()
    return sum(d1.values())


def part1(data: list):
    """Solve part 1."""
    return work(data, 25)


def part2(data):
    """Solve part 2."""
    return work(data, 75)


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
