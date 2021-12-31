""" aoc 2021 day5 """

from parse import parse
from more_itertools import flatten


def fetch():
    """ get input data """
    # with open('testdata.txt') as file:
    with open('data.txt') as file:
        init_data = file.read().split('\n')
    init_data.pop()
    return init_data


def part_one():
    data = fetch()
    vents = []
    for line in data:
        vent = parse("{:d},{:d} -> {:d},{:d}", line)
        vents.append(((vent[0], vent[1]), (vent[2], vent[3])))
    vents = tuple(vents)
    coords = {}
    max_coords = max(list(flatten(flatten(vents))))
    for i in range(max_coords + 1):
        for j in range(max_coords + 1):
            coords[(j, i)] = 0

    for vent in vents:
        x1 = min(vent)[0]
        y1 = min(vent)[1]
        x2 = max(vent)[0]
        y2 = max(vent)[1]

        if x1 == x2 and y1 == y2:
            coords[(x1, y1)] += 1
        elif x1 == x2:
            for i in range(y1, y2 + 1):
                coords[(x1, i)] += 1
        elif y1 == y2:
            for i in range(x1, x2 + 1):
                coords[(i, y1)] += 1

    danger = 0
    for j in range(max_coords + 1):
        dsp_string = ''
        for i in range(max_coords + 1):
            if coords[(i, j)] == 0:
                dsp_string += '.'
            else:
                if coords[(i, j)] > 1:
                    danger += 1
                dsp_string += str(coords[(i, j)])

    return danger


def part_two():
    data = fetch()
    vents = []
    for line in data:
        vent = parse("{:d},{:d} -> {:d},{:d}", line)
        vents.append(((vent[0], vent[1]), (vent[2], vent[3])))
    vents = tuple(vents)
    coords = {}
    max_coords = max(list(flatten(flatten(vents))))
    for i in range(max_coords + 1):
        for j in range(max_coords + 1):
            coords[(j, i)] = 0

    for vent in vents:
        x1 = min(vent)[0]
        y1 = min(vent)[1]
        x2 = max(vent)[0]
        y2 = max(vent)[1]

        if x1 == x2 and y1 == y2:
            coords[(x1, y1)] += 1
        elif x1 == x2:
            for i in range(y1, y2 + 1):
                coords[(x1, i)] += 1
        elif y1 == y2:
            for i in range(x1, x2 + 1):
                coords[(i, y1)] += 1
        else:
            for i in range(abs(x1 - x2) + 1):
                if x1 < x2:
                    if y1 < y2:
                        coords[(x1 + i, y1 + i)] += 1
                    else:
                        coords[(x1 + i, y1 - i)] += 1
                else:
                    if y1 < y2:
                        coords[(x1 - i, y1 + i)] += 1
                    else:
                        coords[(x1 - i, y1 - i)] += 1

    danger = 0
    for j in range(max_coords + 1):
        dsp_string = ''
        for i in range(max_coords + 1):
            if coords[(i, j)] == 0:
                dsp_string += '.'
            else:
                if coords[(i, j)] > 1:
                    danger += 1
                dsp_string += str(coords[(i, j)])

    return danger


if __name__ == "__main__":
    print(part_one())
    print(part_two())
