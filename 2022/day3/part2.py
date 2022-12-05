# f = open("sample.txt", "r")
f = open("input.txt", "r")
data = f.read().split("\n")
data.pop()  ## the previous line results in one record too many so pop it
sumPrio = 0
prioString = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sacks = []
sack = []
for i in data:
    if len(sack) == 3:
        sacks.append(sack)
        sack = []
    sack.append(i)
sacks.append(sack)

for group in sacks:
    for elem in group[0]:
        if group[1].find(elem) >= 0 and group[2].find(elem) >= 0:
            sumPrio += prioString.index(elem) + 1
            indFound = True
            break
# rs = [i[: len(i) // 2], i[len(i) // 2 :]]
# for j in rs[0]:
#     if rs[1].find(j) >= 0:
#         sumPrio += prioString.index(j) + 1
#         break
print(sumPrio)
