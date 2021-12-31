""" aoc 2021 day9 """


def fetch():
    """ get input data """
    # with open('testdata.txt') as file:
    with open('data.txt') as file:
        init_data = file.read().split('\n')
    init_data.pop()
    return init_data


def part_one():
    data = fetch()
    heights = {}
    for row, val in enumerate(data):
        for col, cval in enumerate(val):
            heights[(row, col)] = int(cval)
    danger_totals = 0
    for x in heights:
        neighbor_vals = []
        if (x[0] - 1, x[1]) in heights:
            neighbor_vals.append(heights[x[0] - 1, x[1]])
        if (x[0] + 1, x[1]) in heights:
            neighbor_vals.append(heights[x[0] + 1, x[1]])
        if (x[0], x[1] - 1) in heights:
            neighbor_vals.append(heights[x[0], x[1] - 1])
        if (x[0], x[1] + 1) in heights:
            neighbor_vals.append(heights[x[0], x[1] + 1])
        print(heights[x], neighbor_vals)
        if heights[x] < min(neighbor_vals):
            danger_totals += heights[x] + 1
            print('low spot')
    print('danger totals', danger_totals)


def get_low_spots(heights):
    low_spots = []
    for x in heights:
        neighbor_vals = []
        if (x[0] - 1, x[1]) in heights:
            neighbor_vals.append(heights[x[0] - 1, x[1]])
        if (x[0] + 1, x[1]) in heights:
            neighbor_vals.append(heights[x[0] + 1, x[1]])
        if (x[0], x[1] - 1) in heights:
            neighbor_vals.append(heights[x[0], x[1] - 1])
        if (x[0], x[1] + 1) in heights:
            neighbor_vals.append(heights[x[0], x[1] + 1])
        if heights[x] < min(neighbor_vals):
            low_spots.append(x)
    return low_spots


def get_heights(data):
    heights = {}
    for row, val in enumerate(data):
        for col, cval in enumerate(val):
            heights[(row, col)] = int(cval)
    return heights



def part_two():
    # prepare data structures
    heights = get_heights(fetch())

    # find low spots
    low_spots = get_low_spots(heights)

    # find bassins from low spots
    bassins = []
    for spot in low_spots:
        bassin = []
        bassin.append(spot)
        growing = True
        while growing:
            growing = False
            for bas in bassin:
                neighbors = [(bas[0] - 1, bas[1])
                             , (bas[0] + 1, bas[1])
                             , (bas[0], bas[1] - 1)
                             , (bas[0], bas[1] + 1)]
                for nbr in neighbors:
                    if nbr in bassin or nbr not in heights or heights[nbr] == 9:
                        pass
                    else:
                        bassin.append(nbr)
                        growing = True
        bassins.append(len(bassin))
    bassins = sorted(bassins)
    print(bassins[-1] * bassins[-2] * bassins[-3])


if __name__ == "__main__":
    # print(part_one())
    print(part_two())
