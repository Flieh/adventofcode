""" aoc 2023 dayx """
import pdb


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
    symbols = []
    retVal = 0
    for lineNo, line in enumerate(data):
        for token in line.split("."):
            wtoken = token
            for char in token:
                if not char.isdigit() and len(wtoken) > 1:
                    wtoken = token.replace(char, "")
                    symbols.append((char, (lineNo, line.find(wtoken))))
            if len(wtoken) == 1 and not char.isdigit():
                symbols.append((wtoken, (lineNo, line.find(wtoken))))
            elif len(wtoken) > 0:
                numbers.append((wtoken, (lineNo, line.find(wtoken))))
    for number in numbers:
        for symbol in symbols:
            # pdb.set_trace()
            if (
                int(number[1][0]) - 2 < int(symbol[1][0])
                and int(symbol[1][0]) < int(number[1][0]) + 2
                and int(number[1][1]) - 2 < int(symbol[1][1])
                and int(symbol[1][1]) < int(number[1][1]) + len(number) + 2
            ):
                print(number[0])
                retVal += int(number[0])
                break

    print(retVal)
    # print(symbols)


def part_two():
    pass


if __name__ == "__main__":
    part_one()
    # part_two()
