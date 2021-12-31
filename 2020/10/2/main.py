from itertools import combinations
from functools import lru_cache

def tokenize():
    f = open('sample2.txt', 'r')
    data = f.read().split('\n')
    data.pop()
    for i, line in enumerate(data):
        data[i] = int(line)
    return data

@lru_cache(maxsize=128)
def is_valid_comb(comb, start, end):
    if len(comb) < 2 or comb[0] != start or comb[-1] != end:
        return False
    for j, val in enumerate(comb[:-1]):
        if comb[j + 1] - val > 3:
            return False
    return True

@lru_cache(maxsize=128)
def count_valid_combs(data, start, end, length):
    count = 0
    if is_valid_comb(data, start, end):
        count += 1
        print(count)
        data = combinations(data, length - 1)
        for d in data:
            # print(d, is_valid_comb(d, start, end))
            count += count_valid_combs(tuple(d), start, end, len(d))
            print(count)
    return count



def main():

    data = tokenize()
    start = 0
    end = max(data) + 3
    data.insert(0, start)
    data.append(end)
    data.sort()
    valid_length = False
    count = 0
    for i in range(len(data), -1, -1):
        for comb in tuple(combinations(tuple(data), i)):
            if is_valid_comb(comb, start, end):
                count += 1
    return count


print(main())
