""" aoc 2021 dayx """
import os
from time import perf_counter as timer


def fetch():
    """get input data"""
    with open("data1.txt") as file:
        init_data = file.read().split("\n")
    init_data.pop()
    connections = {}
    for line in init_data:
        work = line.split("-")
        if work[0] not in connections:
            connections[work[0]] = []
        if work[1] not in connections[work[0]]:
            connections[work[0]].append(work[1])
        if work[1] not in connections:
            connections[work[1]] = []
        if work[0] not in connections[work[1]]:
            connections[work[1]].append(work[0])
    for cnx in connections:
        print(cnx.values())
    return connections


def solve(node):
    pass


def part_one():
    data = fetch()
    return data


def part_two():
    return "unsolved"


# hello
if __name__ == "__main__":
    start_time = timer()
    os.system("clear")
    print()
    print("part one")
    print("***************")
    part_one()
    print()
    print("part two")
    print("***************")
    print(part_two())
    print(timer() - start_time)
