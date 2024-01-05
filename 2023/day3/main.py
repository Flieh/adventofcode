""" aoc 2023 dayx """
import pdb
import re


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
    retVal = 0
    tempData = []
    for line in data:
        tempLine = ''
        for charIndex, char in enumerate(list(line)):
            if not char.isdigit():
                tempLine += ' '
            else:
                tempLine += char
        tempData.append(tempLine)
    # print(tempData)
    for lineNo, line in enumerate(tempData):
        for token in line.split(' '):
            if len(token) > 0:
                pat = '\b' + token + '\b'
                print(pat)
                print(line)
                print(re.search(line, pat))
                # numbers.append((token, (lineNo, re.search(pat, line).span()[0])))
        # print(numbers)
    tempData = data
    symbols = []
    for lineNo, line in enumerate(tempData):
        for charInd, char in enumerate(line):
            if (not char.isdigit()) and char != ".":
                symbols.append((char, (lineNo, charInd)))
    # print(symbols)
    validParts = []
    for number in numbers:
        for symbol in symbols:
            # breakpoint()
            if (  int(number[1][0]) - 2 < int(symbol[1][0])
              and int(symbol[1][0])     < int(number[1][0]) + 2
              and int(number[1][1]) - 2 < int(symbol[1][1])
              and int(symbol[1][1])     < int(number[1][1]) + len(number[0]) + 1):
                if int(number[0]) == 4:
                    print(symbol)
                    print(number)
                validParts.append(int(number[0]))
                break
    retVal = sum(validParts)
    print(sorted(validParts))
    print(retVal)
    # print(symbols)
    # print(numbers)


def part_two():
    pass


if __name__ == "__main__":
    part_one()
    # part_two()
