def main():
    f = open('data.txt','r')
    # f = open('sample.txt','r')
    data = f.read()
    records = data.split('\n\n')
    # new_records = []
    # for rec in records:
    #     new_records.append(''.join(rec.split()))
    # total = 0
    # for rec in new_records:
    #     total += len(set(rec))
    # return total
 
    total = 0
    for rec in records:
        number = len(rec.split())
        answers = ''.join(rec.split())
        for a in set(answers):
            if answers.count(a) == number:
                total += 1
    return total


        



print(main())
