# aoc_template.py

import pathlib
import sys
import pudb

pudb.set_trace()
from pipe import select, where


def parse(puzzle_input):
    """Parse input"""
    data = puzzle_input.split('\n')
    numbers = list(data.pop(0).split(',') | select(lambda x: int(x)))
    boards = []
    board = []
    for line in data:
        if line == '':
            if board:
                boards.append(board)
            board = []
        else:
            line = list(line.split() | select(lambda x: int(x)))
            board.append(line)
    boards.append(board)

    return (numbers, boards)


def part1(data):
    """Solve part 1"""
    numbers = data[0]
    boards = data[1]

    for board in boards:  # create columns
        columns = []
        for i in range(5):
            column = []
            for j in range(5):
                column.append(board[j][i])
            board.append(column)

    drawn = []
    for i in range(
            4):  #draw first 4 numbers before starting to check for winners
        drawn.append(numbers.pop(0))

    win = False
    while not win:
        last_draw = numbers.pop(0)
        drawn.append(last_draw)
        for board in boards:

            # check for completed lines
            for line in board:
                count = 0
                for number in line:
                    if number in drawn:
                        count += 1
                if count == 5:
                    win = True
                    winner = boards.index(board)
                    break

    #score winning board
    remaining = []
    for line in boards[winner][:5]:
        for number in line:
            if number not in drawn:
                remaining.append(number)

    return_val = sum(remaining) * last_draw

    return return_val


def part2(data):
    """Solve part 1"""
    numbers = data[0]
    boards = data[1]

    for board in boards:  # create columns
        columns = []
        for i in range(5):
            column = []
            for j in range(5):
                column.append(board[j][i])
            board.append(column)

    drawn = []
    for i in range(
            4):  #draw first 4 numbers before starting to check for winners
        drawn.append(numbers.pop(0))

    winners = []
    win = False
    while len(winners) < len(boards):
        last_draw = numbers.pop(0)
        drawn.append(last_draw)
        for board in boards:
            if boards.index(board) in winners:
                continue
            win = False

            # check for completed lines
            for line in board:
                count = 0
                for number in line:
                    if number in drawn:
                        count += 1
                if count == 5:
                    win = True
                    winners.append(boards.index(board))
                    break
    print(winners)

    #score last winning board
    remaining = []
    for line in boards[winners[-1]][:5]:
        for number in line:
            if number not in drawn:
                remaining.append(number)

    return_val = sum(remaining) * last_draw

    return return_val


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    data = parse(puzzle_input)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
