""" aoc_template.py """

import pathlib
import sys
# from more_itertools import flatten
# from pipe import select
import pudb

pudb.set_trace()


def parse(puzzle_input):
    """Parse input"""
    # without parse mod
    # result = tuple(
    #     puzzle_input.split('\n')
    #     | select(lambda x : list(x.split(' -> ')))
    #     | select(lambda x : (x[0].split(','), x[1].split(',')))
    #     | select(lambda x : ((int(x[0][0]), int(x[0][1])), (int(x[1][0]), int(x[1][1]))))
    #     )

    # with parse
    data = puzzle_input.split('\n')
    for line in data:
        result = parse('{} -> {}', line)
    return result


def part1(data):
    """Solve part 1"""
    # without parse mod
    # max_coord = max(flatten(flatten(data)))
    # vents = {}
    # for i in range(max_coord + 1):
    #     for j in range(max_coord + 1):
    #         vents[(i,j)] = 0
    # # result = (type(data), type(data[0]), type(data[0][0]), type(data[0][0][0]))
    # for line in data:
    #     if line[0] == line[1]: #single point
    #         line_type = 'point'
    #         line_length = 0
    #     elif line[0][0] == line[1][0]: #horizontal line
    #         line_type = 'horizontal'
    #         line_length = line[1][1] - line[0][1]
    #     elif line[0][1] == line[1][1]: #vertical line
    #         line_type = 'vertical'
    #         line_length = line[1][0] - line[0][0]
    #     else:
    #         continue
    #     print(line)
    #     if line_type == 'point':
    #         vents[line[0]] += 1
    #     if line_type == 'horizontal':
    #         for l in range(line_length + 1):
    #             vents[(line[0][0], line[0][1] + l)] += 1
    #     if line_type == 'vertical':
    #         for l in range(line_length + 1):
    #             vents[(line[0][0] + l, line[0][1])] += 1

    # result = vents

    result = 'part 1 unsolved'

    return result


def part2(data):
    """Solve part 2"""
    return 'part 2 unsolved'


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print('part 1:     ', solutions[0])
        print('part 2:     ', solutions[1])
