# f = open("sample.txt", "r")
f = open("input.txt", "r")
data = f.read().split("\n")
data.pop()  ## the previous line results in one record too many so pop it

richElves3 = []
thisElf = 0
lines = 0

for i in data:
    if len(richElves3) == 3:
        break
    if i == "":
        richElves3.append(thisElf)
        thisElf = 0
    else:
        thisElf += int(i)
    lines += 1

for i in data[lines:]:
    if i == "":
        if thisElf > min(richElves3):
            richElves3.remove(min(richElves3))
            richElves3.append(thisElf)
        thisElf = 0
    else:
        thisElf += int(i)

if thisElf > min(richElves3):
    richElves3.remove(min(richElves3))
    richElves3.append(thisElf)

print(sum(richElves3))
