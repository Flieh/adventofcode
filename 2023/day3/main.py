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
    breakpoint()
    data = fetch()
    numbers = []
    retVal = 0
    tempData = []
    for line in data:
        tempLine = line
        for char in line:
            if not char.isdigit():
                tempLine = tempLine.replace(char, ".")
        tempData.append(tempLine)
    for lineNo, line in enumerate(tempData):
        for token in line.split("."):
            if len(token) > 0:
                numbers.append((token, (lineNo, line.find(token))))
    tempData = data
    symbols = []
    for lineNo, line in enumerate(tempData):
        for token in line:
            if (token.isdigit() == False) and (len(token) == 1) and (token != "."):
                symbols.append((token, (lineNo, line.find(token))))
    # print(symbols)
    for number in numbers:
        for symbol in symbols:
            if (
                int(number[1][0]) - 2 < int(symbol[1][0])
                and int(symbol[1][0]) < int(number[1][0]) + 2
                and int(number[1][1]) - 2 < int(symbol[1][1])
                and int(symbol[1][1]) < int(number[1][1]) + len(number) + 2
            ):
                print(int(number[0]))
                retVal += int(number[0])
                break

    print(retVal)
    # print(symbols)
    # print(numbers)


def part_two():
    pass


if __name__ == "__main__":
    part_one()
    # part_two()
