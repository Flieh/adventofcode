""" aoc 2021 day5 """

from parse import parse
# from more_itertools import flatten


def fetch():
    """ get input data """
    # with open('testdata.txt') as file:
    with open('data.txt') as file:
        init_data = file.read().split('\n')
    init_data.pop()
    init_data = [int(x) for x in init_data[0].split(',')]
    return init_data


def part_one():
    lampfish = fetch()
    gen_count = 80
    for i in range(gen_count):
        generation = []
        newfish = 0
        for fish in lampfish:
            if fish == 0:
                newfish += 1
                generation.append(6)
            else:
                generation.append(fish - 1)
        for fish in range(newfish):
            generation.append(8)
        lampfish = list(generation)

    return len(lampfish)


def part_two():
    lampfish = fetch()
    this_generation = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in lampfish:
        this_generation[fish] += 1
    gen_count = 256
    for j in range(gen_count):
        next_generation = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(8, 0, -1):
            next_generation[i - 1] = this_generation[i]
        next_generation[8] = this_generation[0]
        next_generation[6] += this_generation[0]
        this_generation = list(next_generation)
    return sum(this_generation)


if __name__ == "__main__":
    # print(part_one())
    print(part_two())
