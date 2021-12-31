""" aoc 2021 dayx """
import os
from time import perf_counter as timer


def fetch():
    """ get input data """
    with open('test3data.txt') as file:
        init_data = file.read().split('\n')
    init_data.pop()
    connections = {}
    for line in init_data:
        work = line.split('-')
        if work[0] not in connections:
            connections[work[0]] = []
        if work[1] not in connections[work[0]]:
            connections[work[0]].append(work[1])
        if work[1] not in connections:
            connections[work[1]] = []
        if work[0] not in connections[work[1]]:
            connections[work[1]].append(work[0])
    return connections

    return init_data


def part_one():
    data = fetch()
    partials = [['start']]
    new_path_found = True
    while new_path_found:
        # print('first loop')
        new_path_found = False
        for partial in partials:
            if 'end' in partial:
                continue
            # print('second loop')
            working_path = list(partial)
            for node in data[partial[-1]]:
                # print('third loop')
                if node in working_path:
                    if node.islower():
                        continue
                working_path.append(node)
                if working_path in partials:
                    working_path.pop()
                    continue
                partials.append(working_path)
                print(working_path)
                new_path_found = True
                break
            if new_path_found:
                break

    complete = []
    for partial in partials:
        if 'end' in partial:
            complete.append(partial)
    print(len(complete))
    return 'solved'


def part_two():
    data = fetch()
    return 'unsolved'

# hello 
if __name__ == "__main__":
    start_time = timer()
    os.system('clear')
    print()
    print('part one')
    print('***************')
    print(part_one())
    print()
    print('part two')
    print('***************')
    print(part_two())
    print(timer() - start_time)
