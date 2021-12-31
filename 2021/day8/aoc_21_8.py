""" aoc 2021 dayx """


def fetch():
    """ get input data """
    # with open('testdata.txt') as file:
    with open('data.txt') as file:
        init_data = file.read().split('\n')
    init_data.pop()
    return init_data


def part_one():
    data = fetch()
    count = 0
    for line in data:
        results = [
            len(x) for x in line.split('|')[1].split()
            if len(x) in [2, 3, 4, 7]
        ]
        count += len(results)
    return count


def part_two():
    data = fetch()
    result = 0
    for line in data:
        numerals = [None for x in range(10)]
        codes = line.split('|')
        input_codes = codes[0].split(' ')
        input_codes = [''.join(sorted(x)) for x in input_codes]
        input_codes.pop()
        output_codes = codes[1].split(' ')
        output_codes = [''.join(sorted(x)) for x in output_codes]
        output_codes.pop(0)
        for element in input_codes:
            if len(element) == 2:
                numerals[1] = element
            if len(element) == 3:
                numerals[7] = element
            if len(element) == 4:
                numerals[4] = element
            if len(element) == 7:
                numerals[8] = element
        for element in input_codes:
            if len(element) == 5 and all(x in element for x in numerals[1]):
                numerals[3] = element
                break
        for element in input_codes:
            if len(element) == 6 and all(x in element for x in numerals[3]):
                numerals[9] = element
                break
        for element in input_codes:
            if len(element) == 6 and all(x in element for x in numerals[7]):
                if element in numerals:
                    continue
                numerals[0] = element
                break
        for element in input_codes:
            if len(element) == 6:
                if element in numerals:
                    continue
                numerals[6] = element
        for element in input_codes:
            if len(element) == 5:
                if element in numerals:
                    continue
                if all(x in numerals[9] for x in element):
                    numerals[5] = element
        for element in input_codes:
            if element in numerals:
                continue
            numerals[2] = element

        output_string = ''
        for element in output_codes:
            output_string += str(numerals.index(element))
        result += int(output_string)

    return result


if __name__ == "__main__":
    # print('Part One:')
    # print('-----------------')
    # print(part_one())
    # print()
    print('Part Two:')
    print('-----------------')
    print(part_two())
