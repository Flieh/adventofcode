""" aoc 2021 day10 """

openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']
values = [3, 57, 1197, 25137]


def fetch():
    """ get input data """
    # with open('testdata.txt') as file:
    with open('data.txt') as file:
        init_data = file.read().split('\n')
    init_data.pop()
    return init_data


def part_one():
    data = fetch()
    score = 0
    for item in data:
        line = item
        first_invalid = None
        pair_removed = True
        while pair_removed:
            pair_removed = False
            if line[0] in closers:
                first_invalid = line[0]
                break
            for i, val in enumerate(line[:-1]):
                if val in openers:
                    if line[i + 1] in openers:
                        continue
                    if openers.index(val) == closers.index(line[i + 1]):
                        new_line = line[:i]
                        if i + 2 <= len(line):
                            new_line += line[i + 2:]
                        line = new_line
                        print(line)
                        pair_removed = True
                        break
                    else:
                        first_invalid = line[i + 1]
                        break

        if first_invalid:
            score += values[closers.index(first_invalid)]

    return score


def part_two():
    data = fetch()
    scores = []
    for item in data:
        line = item
        invalid = False
        pair_removed = True
        while pair_removed:
            pair_removed = False
            if line[0] in closers:
                invalid = True
                break
            for i, val in enumerate(line[:-1]):
                if val in openers:
                    if line[i + 1] in openers:
                        continue
                    if openers.index(val) == closers.index(line[i + 1]):
                        new_line = line[:i]
                        if i + 2 <= len(line):
                            new_line += line[i + 2:]
                        line = new_line
                        pair_removed = True
                        break
                    invalid = True
                    break

            if invalid:
                break
        if not invalid:
            score = 0
            line = list(reversed(line))
            line = [closers[openers.index(x)] for x in line]
            for elem in line:
                score *= 5
                score += closers.index(elem) + 1
            scores.append(score)
    print(sorted(scores)[len(scores) // 2])
    return None


if __name__ == "__main__":
    # print(part_one())
    print(part_two())
