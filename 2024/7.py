from aocd.models import Puzzle
import copy

YEAR = 2024
DAY = 7


def parse(data: str):
    """Parse input."""
    lines = data.strip().splitlines()
    parsed_data = []
    for line in lines:
        splits = line.split(":")
        total = int(splits[0].strip())
        values = [int(val) for val in splits[1].strip().split()]
        parsed_data.append([total, values])
    return parsed_data


def recursive_fn(total, values):
    last_value = values.pop()
    if not values:  # base case
        if total == last_value:
            return True
        return False

    if total % last_value == 0:
        return recursive_fn(total / last_value, list(values)) or recursive_fn(
            total - last_value, list(values)
        )
    else:
        return recursive_fn(total - last_value, list(values))


def combine(x, y):
    return int(str(x) + str(y))


def endswith(num, suffix):
    return num != suffix and str(num).endswith(str(suffix))


def remove_suffix(num, suffix):
    try:
        num_str = str(int(num))
        suffix_str = str(int(suffix))
        return int(num_str[: -len(suffix_str)])
    except:
        return int(num)


def recursive_fn2(total, values):
    if not (
        isinstance(total, int) or (isinstance(total, float) and total.is_integer())
    ):
        return False
    if total < 0:
        return False

    total = int(total)
    last_value = values.pop()
    if not values:
        if total == last_value:
            return True
        return False

    if endswith(total, last_value):
        return (
            recursive_fn2(total / last_value, list(values))
            or recursive_fn2(total - last_value, list(values))
            or recursive_fn2(remove_suffix(total, last_value), list(values))
        )

    else:
        return recursive_fn2(total / last_value, list(values)) or recursive_fn2(
            total - last_value, list(values)
        )


def part1(data):
    """Solve part 1."""
    total_result = 0
    for problem in data:
        total, values = problem
        if recursive_fn(total, values):
            total_result += total
    return total_result


def part2(data):
    """Solve part 2."""
    total_result = 0
    for problem in data:
        total, values = problem
        if recursive_fn2(total, values):
            total_result += total
    return total_result


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(copy.deepcopy(data))
    solution2 = part2(copy.deepcopy(data))

    return solution1, solution2


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)

    solution1, solution2 = solve(puzzle.input_data)

    print(f"Part 1 Solution: {solution1}")
    print(f"Part 2 Solution: {solution2}")
