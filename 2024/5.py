from aocd.models import Puzzle
from functools import reduce
from collections import Counter

YEAR = 2024
DAY = 5


def parse(data: str):
    """Parse input."""
    first, second = data.split("\n\n")
    rules = first.splitlines()
    rule_map = {}
    for rule in rules:
        key, value = rule.split("|")
        key = int(key)
        value = int(value)
        if key in rule_map:
            rule_map[key].add(value)
        else:
            rule_map[key] = {value}

    updates = second.splitlines()
    update_list = [[int(v) for v in s.split(",")] for s in updates]

    return rule_map, update_list


def part1(data):
    """Solve part 1."""

    """ Part 2 reveals are more efficient solution to Part 1, but alas I moved on."""
    rule_map, update_list = data
    middle_total = 0
    for update in update_list:
        isValid = True
        for i in range(len(update)):
            current = update[i]
            remaining = update[i + 1 :]
            for val in remaining:
                if current in rule_map and val not in rule_map[current]:
                    isValid = False
                    break
                if val in rule_map and current in rule_map[val]:
                    isValid = False
                    break
            if not isValid:
                break
        if isValid:
            middle_total += update[len(update) // 2]
    return middle_total


def part2(data):
    """Solve part 2."""
    rule_map, update_list = data
    incorrect_updates = []
    for update in update_list:
        isValid = True
        for i in range(len(update)):
            current = update[i]
            remaining = update[i + 1 :]
            for val in remaining:
                if current in rule_map and val not in rule_map[current]:
                    isValid = False
                    break
                if val in rule_map and current in rule_map[val]:
                    isValid = False
                    break
            if not isValid:
                incorrect_updates.append(update)
                break

    middle_total = 0
    for update in incorrect_updates:
        this_set = set(update)
        midpoint = len(update) // 2
        for val in update:
            rule_count = len(this_set.intersection(rule_map.get(val, {})))
            if rule_count == midpoint:
                middle_total += val

    return middle_total


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
