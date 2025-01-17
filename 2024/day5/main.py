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
    rules = []
    editions = []
    validEditions = []
    sumMiddlePages = 0
    for line in data:
        if len(line) > 0 and line[2] != '|':
            editions.append(line.split(','))
    for ed in editions:
        isEdValid = True
        for rule in rules:
            if rule[0] in ed and rule[1] in ed:
                if ed.index(rule[0]) > ed.index(rule[1]):
                    isEdValid = False
                    break
        if isEdValid:
            validEditions.append(ed)

    for ed in validEditions:
        midIdx = (len(ed) // 2)
        sumMiddlePages += int(ed[midIdx])
    return sumMiddlePages

def part_two():
    data = fetch()
    rules = []
    editions = []
    invalidEditions = []
    correctedEditions = []
    sumMiddlePages = 0
    newRules = []
    orderedRules = []

    # separate data lines into list of rules and list of editions
    for line in data:
        if len(line) > 0 and line[2] == '|':
            rules.append(line.split('|'))
        if len(line) > 0 and line[2] != '|':
            editions.append(line.split(','))

    # determine invalide editions (pages in wrong order according to rules)which will later be validated for ed in editions: for rule in rules:
    for ed in editions:
        for rule in rules:
            if rule[0] in ed and rule[1] in ed:
                if ed.index(rule[0]) > ed.index(rule[1]):
                    invalidEditions.append(ed)
                    break
    # dress list of beforeRules (first item in each rule) and afterRules (second item in each rule)
    print(rules)
    print(invalidEditions)
    for ed in invalidEditions:
        indSort = False
        while indSort == False:
            indSort = True
            for ru in rules:
                if ru[0] in ed and ru[1] in ed:
                    i = ed.index(ru[0])
                    j = ed.index(ru[1])
                    if i > j:
                        indSort = False
                        ed[i], ed[j] = ed[j], ed[i]
    print(invalidEditions)


    # create list of rules in order (orderedRules) FLAWED 
    # while len(beforeRules) > 0:

    #     # if its the remaining rule then these are the last two page orders
    #     if len(rules) == 1:
    #         orderedRules.append(rules[0][0])
    #         orderedRules.append(rules[0][1])
    #         break

    #     for br in beforeRules:
    #         if br not in afterRules:
    #             print(found)
    #             foundRule = br
    #             orderedRules.append(br)
    #             for rule in rules:
    #                 if rule[0] != br:
    #                     newRules.append(rule)

    #     beforeRules.remove(foundRule)
    #     rules = newRules[:]
    #     newRules = []
    #     beforeRules = list(set([x[0] for x in rules]))
    #     afterRules =  list(set([x[1] for x in rules]))

    # # based on ordered rules, correct the order of the invalid editions

    for ed in invalidEditions:
        midIdx = (len(ed) // 2)
        sumMiddlePages += int(ed[midIdx])
    return sumMiddlePages

if __name__ == "__main__":
    # print(part_one())
    print(part_two())
