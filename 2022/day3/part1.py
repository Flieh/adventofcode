# f = open("sample.txt", "r")
f = open("input.txt", "r")
data = f.read().split("\n")
data.pop()  ## the previous line results in one record too many so pop it
sumPrio = 0
prioString = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in data:
    rs = [i[: len(i) // 2], i[len(i) // 2 :]]
    for j in rs[0]:
        if rs[1].find(j) >= 0:
            sumPrio += prioString.index(j) + 1
            break
print(sumPrio)
