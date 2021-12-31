""" aoc 2021 dayx """

# constants
STEPS = 1000


def fetch():
    """ get input data """
    # with open('smalldata.txt') as file:
    # with open('testdata.txt') as file:
    with open('data.txt') as file:
        init_data = file.read().split('\n')
    init_data.pop()
    init_data = [list(x) for x in init_data]
    wrk_data = []
    for item in init_data:
        wrk_data.append([int(x) for x in item])
    init_data = wrk_data
    return init_data


def augment_all(data):
    new_data = []
    for line in data:
        new_line = []
        for item in line:
            new_line.append(item + 1)
        new_data.append(new_line)
    return new_data


def augment_neighbors(data, coords):
    neighbors = [(coords[0] - 1, coords[1] - 1), (coords[0] - 1, coords[1]),
                 (coords[0] - 1, coords[1] + 1), (coords[0], coords[1] - 1),
                 (coords[0], coords[1] + 1), (coords[0] + 1, coords[1] - 1),
                 (coords[0] + 1, coords[1]), (coords[0] + 1, coords[1] + 1)]
    for nbr in neighbors:
        # print(nbr[0], nbr[1])
        if nbr[0] < 0:
            # print('first index too small')
            continue
        if nbr[1] < 0:
            # print('second index too small')
            continue
        if nbr[0] >= len(data):
            # print('first index too large')
            continue
        if nbr[1] >= len(data[0]):
            # print('second index too large')
            continue
        if data[nbr[0]][nbr[1]] is None:
            continue
        data[nbr[0]][nbr[1]] += 1
        if data[nbr[0]][nbr[1]] > 9:
            data[nbr[0]][nbr[1]] = None
            data = augment_neighbors(data, (nbr[0], nbr[1]))

    return data


def visualize(data):
    for line in data:
        output_string = ''
        for el in line:
            if el > 9:
                output_string += ' '
            else:
                output_string += str(el)
        print(output_string)
    print()


def part_one():
    data = fetch()
    flashes = 0

    for step in range(STEPS):
        visualize(data)
        # first increase each value by 1
        data = augment_all(data)

        # augment all neighbors of cells superior to 9
        for i, line in enumerate(data):
            for j, el in enumerate(line):
                if el is None:
                    continue
                if el > 9:
                    data[i][j] = None
                    data = augment_neighbors(data, (i, j))

        # reset fired cells to 0
        for i, line in enumerate(data):
            for j, el in enumerate(line):
                if el is None:
                    flashes += 1
                    data[i][j] = 0

    return flashes


def part_two():
    data = fetch()
    full_flash = False
    octopi = len(data) * len(data[0])

    for step in range(STEPS):
        # visualize(data)
        # first increase each value by 1
        data = augment_all(data)

        # augment all neighbors of cells superior to 9
        for i, line in enumerate(data):
            for j, el in enumerate(line):
                if el is None:
                    continue
                if el > 9:
                    data[i][j] = None
                    data = augment_neighbors(data, (i, j))

        # reset fired cells to 0
        current_flashes = 0
        for i, line in enumerate(data):
            for j, el in enumerate(line):
                if el is None:
                    current_flashes += 1
                    if current_flashes == octopi:
                        full_flash = True
                    data[i][j] = 0
        if full_flash:
            break

    return step + 1


if __name__ == "__main__":
    # print(part_one())
    print(part_two())
