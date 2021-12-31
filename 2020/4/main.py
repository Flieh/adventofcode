req_fields = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']
def main():
    f = open('input.txt', 'r')
    # f = open('input_sample.txt', 'r')
    # f = open('valid.txt', 'r')
    # f = open('invalid.txt', 'r')
    records = f.read().split('\n\n')
    if records[-1][-1] == '\n':
        records[-1] = records[-1][:-1] # remove trailing newline
    # valid_recs = 0
    # for rec in records:
    #     validate = 0
    #     fields = rec.split(' ')
    #     for field in req_fields:
    #         if field in rec:
    #             validate += 1
    #     if validate == 7:
    #         valid_recs += 1
    valid_recs = 0
    for record in records:
        print('*********')
        print(record)
        print('*********')
        valid = 0
        fields = record.split()
        for field in fields:
            key = field.split(':')[0]
            value = field.split(':')[1]
            if key == 'byr':
                if len(value) == 4:
                    if value.isnumeric():
                        if 1920 <= int(value) <= 2020:
                            print(key, 'valid')
                            valid += 1
                        else:
                            print(key, '** rejected **')
            elif key == 'iyr':
                if len(value) == 4:
                    if value.isnumeric():
                        if 2010 <= int(value) <= 2020:
                            print(key, 'valid')
                            valid += 1
                        else:
                            print(key, '** rejected **')
            elif key == 'eyr':
                if len(value) == 4:
                    if value.isnumeric():
                        if 2020 <= int(value) <= 2030:
                            print(key, 'valid')
                            valid += 1
                        else:
                            print(key, '** rejected **')
            elif key == 'hgt':
                unit = value[-2:]
                if unit == 'cm':
                    if 150 <= int(value[:-2]) <= 193:
                        print(key, 'valid')
                        valid += 1
                    else:
                        print(key, '** rejected **')
                elif unit == 'in':
                    if 59 <= int(value[:-2]) <= 76:
                        print(key, 'valid')
                        valid += 1
                    else:
                        print(key, '** rejected **')
                else:
                    print(key, '** rejected **')
            elif key == 'hcl':
                if value[0] == "#":
                    value = value[1:]
                    if len(value) == 6:
                        ok = True
                        for letter in value:
                            if letter not in 'abcdef0123456789':
                                ok = False
                        if ok:
                            print(key, 'valid')
                            valid += 1
                        else:
                            print(key, '** rejected **')
            elif key == 'ecl':
                if value in ['amb','blu','brn','gry','grn','hzl','oth']:
                    print(key, 'valid')
                    valid += 1
                else:
                    print(key, '** rejected **')
            elif key == 'pid':
                if len(value) == 9:
                    if value.isnumeric():
                        print(key, 'valid')
                        valid += 1
                    else:
                        print(key, '** rejected **')
                else:
                    print(key, '** rejected **')
            elif key == 'cid':
                continue
            else:
                print('** unknown key **')
        if valid == 7:
            valid_recs += 1
            print('Record Accepted :)')
        else:
            print('** record rejected **')
        print()
        print()
    return valid_recs


print(main())
