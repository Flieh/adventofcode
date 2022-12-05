# f = open("sample.txt", "r")
f = open("input.txt", "r")
data = f.read().split("\n")
data.pop()  ## the previous line results in one record too many so pop it
richestElf = 0
thisElf = 0
for i in data:
    if i == "":
        if thisElf > richestElf:
            richestElf = thisElf
        thisElf = 0
    else:
        thisElf += int(i)
if thisElf > richestElf:
    richestElf = thisElf
print(richestElf)
