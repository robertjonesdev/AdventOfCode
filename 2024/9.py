from aocd.models import Puzzle


YEAR = 2024
DAY = 9

TEST_DATA = "2333133121414131402"


def parse(data: str):
    """Parse input."""
    data = [int(x) for x in list(data.strip())]
    files = data[::2]
    empty_spaces = data[1::2]
    if len(empty_spaces) < len(files):
        empty_spaces.append(0)

    file_list = []
    file_list2 = []

    for index, (file, space) in enumerate(zip(files, empty_spaces)):
        file_list.extend([index for x in range(file)])
        file_list2.append((index, file))
        if space:
            file_list.extend([-1 for x in range(space)])
            file_list2.append((-1, space))

    return file_list, file_list2


def checksum(lst):
    checksum = 0
    for index, value in enumerate(lst):
        if value > -1:
            checksum += index * value
    return checksum


def swap(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]


def part1(file_list):
    """Solve part 1."""

    left_idx = 1
    right_idx = len(file_list) - 1
    for index in range(right_idx, -1, -1):
        if index < left_idx:
            break
        value = file_list[index]
        if value != -1:
            for idx in range(left_idx, index):
                space = file_list[idx]
                if space == -1:
                    swap(file_list, index, idx)
                    left_idx = idx
                    break

    return checksum(file_list)


def part2(file_list: list):
    """Solve part 2."""
    left_idx = 1
    right_idx = len(file_list) - 1

    idx_offset = 0
    for index in range(right_idx, -1, -1):
        index += idx_offset
        file_id, file_size = file_list[index]
        if file_id != -1:
            for idx in range(left_idx, index):
                space_id, space_size = file_list[idx]
                if space_id == -1 and file_size <= space_size:
                    file_list.insert(idx, (file_id, file_size))
                    idx_offset += 1
                    file_list[idx + 1] = (-1, space_size - file_size)

                    if (index + 2 < len(file_list)) and file_list[index + 2][0] == -1:
                        _, next_space = file_list[index + 2]
                        file_list[index + 2] = (-1, next_space + file_size)
                        del file_list[index + 1]
                    else:
                        file_list[index + 1] = (-1, file_size)
                    break

    unpacked_list = []
    for file_id, size in file_list:
        for i in range(size):
            unpacked_list.append(file_id)

    return checksum(unpacked_list)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data1, data2 = parse(puzzle_input)
    solution1 = None  # part1(data1)
    solution2 = part2(data2)

    return solution1, solution2


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)

    # solution1, solution2 = solve(TEST_DATA)
    solution1, solution2 = solve(puzzle.input_data)

    print(f"Part 1 Solution: {solution1}")
    print(f"Part 2 Solution: {solution2}")
