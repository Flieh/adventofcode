""" aoc 2023 dayx """


def fetch():
    """ get input data """
    with open('testdata.txt') as file:
        # with open('data.txt') as file:
        init_data = file.read().split('\n')
    init_data.pop()
    return init_data


def part_one():
    data = fetch()
    return data


def part_two():
    data = fetch()
    return data


if __name__ == "__main__":
    print(part_one())
    print(part_two())
