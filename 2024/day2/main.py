""" aoc 2024 day1 """
def fetch():
    """ get input data """
    with open('data.txt') as file:
        # with open('data.txt') as file:
        init_data = file.read().split('\n')
    init_data.pop()
    return init_data


def part_one():
    data = fetch()
    nbSafeReports = 0
    lines = 0
    for line in data:
        report = [int(x) for x in line.split()]
        safe = isReportSafe(report)
        if not safe:
            continue
        nbSafeReports += 1
    return nbSafeReports

def part_two():
    pass
    data = fetch()
    nbSafeReports = 0
    lines = 0
    for line in data:
        report = [int(x) for x in line.split()]
        safe = isReportSafe(report)
        if not safe:
            for i, v in enumerate(report):
                w_report = report[:]
                del w_report[i]
                if isReportSafe(w_report):
                    safe = True
        if safe:
            nbSafeReports += 1
    return nbSafeReports

def isReportSafe(report):
    if report[0] < report[1]:
        sort = 'asc'
    else:
        sort = 'desc'
    for i, v in enumerate(report[:-1]):
        if          sort == 'asc' \
                and report[i+1] - v not in (1 ,2 ,3 ) \
                or \
                    sort == 'desc' \
                and report[i+1] - v not in (-1,-2,-3):
            return False
    return True

if __name__ == "__main__":
    # print(part_one())
    print(part_two())
