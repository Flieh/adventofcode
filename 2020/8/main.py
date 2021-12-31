import functools
from copy import deepcopy


def tokenize():
    f = open('data.txt', 'r')
    inp = f.read().split('\n')
    inp.pop()
    data = []
    for token in inp:
        data.append([token.split()[0], token.split()[1][0], int(token.split()[1][1:]), False])
    for token in data:
        if token[1] == '-':
            token[2] = token[2] * -1
        del token[1]
    return data

def run_machine(data):
    pointer = 0
    acc = 0
    op_code = None
    while True:
        if pointer == len(data):
            op_code = 1
            break
        if data[pointer][2]:
            op_code = 0
            break

        data[pointer][2] = True
        if data[pointer][0] == 'acc':
            acc += data[pointer][1]
            pointer += 1
        elif data[pointer][0] == 'jmp':
            pointer += data[pointer][1]
        elif data[pointer][0] == 'nop':
            pointer += 1
            
    return (acc, op_code)


def mod_line(line, d):
    if d[line][0] == 'nop':
        d[line][0] = 'jmp'
    elif d[line][0] == 'jmp':
        d[line][0] = 'nop'
    return d

def main():
    data = tokenize()
    for i, line in enumerate(data):
        test_data = deepcopy(data)
        test_data = mod_line(i, test_data)
        result = run_machine(test_data)
        if result[1]:
            return result[0]
print(main())

