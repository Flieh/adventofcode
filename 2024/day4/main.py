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
    data = fetch()
    length = len(data)
    width = len(data[0])
    xmas = 0
    headings = ( (0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1) )
    for h in headings:
        for i,v in enumerate(data):
            for j,w in enumerate(v):
                if i + (h[0] * 3) in range(0,length) and j + (h[1] * 3) in range(0,width):
                    sample =  data[i             ][j             ] \
                            + data[i + (h[0]    )][j + (h[1]    )] \
                            + data[i + (h[0] * 2)][j + (h[1] * 2)] \
                            + data[i + (h[0] * 3)][j + (h[1] * 3)]

                    if sample == 'XMAS':
                        xmas += 1
    return xmas

def part_two():
    data = fetch()
    length = len(data)
    width = len(data[0])
    xmas = 0
    for i,v in enumerate(data):
        if i in range(1,length-1):
            for j,w in enumerate(v):
                if j in range(1,width-1):
                    if      w == 'A' \
                        and ( data[i-1][j-1] + data[i-1][j+1] + data[i+1][j+1] + data[i+1][j-1] ) \
                            in ('MMSS', 'SMMS', 'SSMM', 'MSSM'):
                        xmas += 1
    return xmas

if __name__ == "__main__":
    print(part_one())
    print(part_two())
