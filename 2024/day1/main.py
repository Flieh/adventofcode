""" aoc 2024 day1 """

def fetch():
    """ get input data """
    with open('data.txt') as file:
        # with open('data.txt') as file:
        init_data = file.read().split('\n')
    init_data.pop()
    return init_data


def part_one():
    data = fetch()

    listright = []
    listleft = []
    cumuldiff = 0

    for line in data:
        listright.append(line.split()[0])
        listleft.append(line.split()[1])

    while len(listright) > 0:
        cumuldiff += abs(int(min(listright)) - int(min(listleft)))
        listright.remove(min(listright))
        listleft.remove(min(listleft))
        
    return cumuldiff

def part_two():
    data = fetch()

    listright = []
    listleft = []
    cumul = 0

    for line in data:
        listright.append(line.split()[0])
        listleft.append(line.split()[1])

    for elem in listright:
        cumul += listleft.count(elem) * int(elem)

    return cumul

if __name__ == "__main__":
    print(part_one())
    print(part_two())
