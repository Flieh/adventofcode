from itertools import combinations
 
def tokenize():
    f = open('data.txt', 'r')
    inp = f.read().split('\n')
    inp.pop()
    for i, line in enumerate(inp):
        inp[i] = int(line)
    return inp


def main():
    data = tokenize()
    len_preamble = 25
    target = 731031916
    for i, line in enumerate(data):
        mini = line
        maxi = line
        j = i
        count = 0
        while count < target:
            count += data[j]
            if data[j] < mini:
                mini = data[j]
            if data[j] > maxi:
                maxi = data[j]
            if count == target:
                return sum([mini, maxi])
            j += 1

print(main())

