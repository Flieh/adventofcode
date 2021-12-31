from itertools import combinations


def tokenize():
    f = open('sample.txt', 'r')
    data = f.read().split('\n')
    data.pop()
    for i, line in enumerate(data):
        data[i] = int(line)
    return data


def main():
    data = tokenize()
    start = 0
    end = max(data) + 3
    data.sort()
    # count_diff_1 = 0
    # count_diff_3 = 0
    # for k, v in enumerate(data):
    #     if k > len(data) - 2:
    #         break
    #     if data[k + 1] - v == 1:
    #         count_diff_1 += 1
    #     if data[k + 1] - v == 3::wqw
    #         count_diff_3 += 1
    # return (count_diff_1 * count_diff_3)
    # combs = list(combinations(data, len(data)))
    return combs




print(main())

