import functools


rules = {}


@functools.lru_cache(maxsize=128)
def is_targ_in_bag(targ, bag):
    for b in rules[bag]:
        if targ in b:
            return True
        else:
            for r in rules[bag]:
                if is_targ_in_bag(targ, r[1]):
                    return True
    return False


@functools.lru_cache(maxsize=128)
def how_many_bags(targ):
    count = 0
    for r in rules[targ]:
        count += r[0]
        for i in range(r[0]):
            count += how_many_bags(r[1])
    return count


def make_rules():
    f = open('data.txt', 'r')
    inp= f.read().split('\n')
    inp.pop()
    for r in inp:
        tokens = r.split()
        container = ''.join([tokens[0], tokens[1]])
        contained = []
        if tokens[4].isnumeric():
            offset = 4
            while offset + 4 <= len(tokens):
                contained.append((int(tokens[offset]), ''.join([tokens[offset + 1], tokens[offset + 2]])))
                offset += 4
        rules[container] = contained

    return rules

def main():
    rules = make_rules()
    target = 'shinygold'
    # count_containers = 0
    # for bag in rules:
    #     if is_targ_in_bag(target, bag):
    #         count_containers += 1
    # return count_containers
    return how_many_bags(target)

print(main())

