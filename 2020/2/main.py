f = open('input.txt', 'r')
entries = f.read().split('\n')
entries.pop()
count = 0
# for entry in entries:
#     fields = entry.split()
#     min_max = fields[0].split('-')
#     minimum = int(min_max[0])
#     maximum = int(min_max[1])
#     valid_char = fields[1][0]
#     if minimum <= fields[2].count(valid_char) <= maximum:
#         count += 1

for entry in entries:
    fields = entry.split()
    positions = fields[0].split('-')
    pos_1 = int(positions[0])
    pos_2 = int(positions[1])
    valid_char = fields[1][0]
    if len(fields[2]) < pos_1 or len(fields[2]) < pos_2:
        continue
    if valid_char == fields[2][pos_1 - 1] or valid_char == fields[2][pos_2 - 1]:
        if valid_char == fields[2][pos_1 - 1] and valid_char == fields[2][pos_2 - 1]:
            continue
        count += 1
print(count)
