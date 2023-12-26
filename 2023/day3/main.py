""" aoc 2023 dayx """


def fetch():
    """get input data"""
    with open("data.txt") as file:
        # with open('data.txt') as file:
        init_data = file.read().split("\n")
    init_data.pop()
    return init_data


def part_one():
    data = fetch()
    numbers = []
    for line in data:
        for token in line.split("."):
            wtoken = token
            for char in token:
                if not char.isdigit():
                    wtoken = token.replace(char, "")
            if len(wtoken) > 0:
                numbers.append(wtoken)
    for number in numbers:
        field = []
        for lineNo, line in enumerate(data):
            if line.find(number) > -1:
                if lineNo > 0:
                    if line.find(number) > 0:
                        field.append(lineNo - 1, line.find(number) - 1)
                    field.append(lineNo -1,)

    print(coordSymbols)


def part_two():
    pass


if __name__ == "__main__":
    part_one()
    # part_two()
