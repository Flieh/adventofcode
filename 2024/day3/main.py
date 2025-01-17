""" aoc 2024 day1 """
import re

def fetch():
    """ get input data """
    with open('data.txt') as file:
        # with open('data.txt') as file:
        init_data = file.read().split('\n')
    init_data.pop()
    return init_data


def part_one():
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    data = fetch()
    string = ''.join(data)
    result = 0
    matches = re.findall(pattern,string)
    for match in matches:
        result += evalMult(match)
    return result

def part_two():
    pattern = r'mul\(\d{1,3},\d{1,3}\)|(?:do|don\'t)\(\)'
    data = fetch()
    string = ''.join(data)
    result = 0
    matches = re.findall(pattern,string)
    calc = True
    for match in matches:
        if match == 'do()':
            print('do()')
            calc = True
            continue
        if match == 'don\'t()':
            print('don\'t()')
            calc = False
            continue
        if calc == True:
            result += evalMult(match)
    return result 

def evalMult(string):
    pattern = r'\d{1,3}'
    operands = re.findall(pattern, string)
    return int(operands[0]) * int(operands[1])

if __name__ == "__main__":
    # print(part_one())
    print(part_two())
