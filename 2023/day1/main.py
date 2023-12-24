""" aoc 2023 dayx """

def fetch():
    """ get input data """
    with open('data.txt') as file:
        # with open('data.txt') as file:
        init_data = file.read().split('\n')
    init_data.pop()
    return init_data


def part_one():
    data = fetch()
    retVal = 0
    for line in data:
        for char in line:
            if char.isdigit():
                retVal += int(char) * 10
                break
        for char in reversed(line):
            if char.isdigit():
                retVal += int(char)
                break
    print(retVal)

def part_two():
    data = fetch()
    symbols = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    retVal = 0
    for line in data:
        firstIndex = len(line) + 1
        firstVal   = None
        lastIndex  = -1
        lastVal    = None
        tempVal    = 0
        for symbol in symbols:
            tmpIndxFirst = line.find(symbol)
            if (tmpIndxFirst < firstIndex) and (tmpIndxFirst > -1):
                firstIndex = tmpIndxFirst
                firstVal = symbol
            tmpIndxLast = line.rfind(symbol)
            if (tmpIndxLast > lastIndex) and (tmpIndxLast > -1):
                lastIndex = tmpIndxLast
                lastVal = symbol
        tmpIndxSym = symbols.index(firstVal)
        if tmpIndxSym < 10:
            tempVal += tmpIndxSym * 10
        else:
            tempVal += (tmpIndxSym - 9) * 10
        tmpIndxSym = symbols.index(lastVal)
        if tmpIndxSym < 10:
            tempVal += tmpIndxSym
        else:
            tempVal += (tmpIndxSym - 9)
        retVal += tempVal
    print(retVal)

if __name__ == "__main__":
    part_one()
    part_two()
