# f = open("sample.txt", "r")
f = open("input.txt", "r")
data = f.read().split("\n")
data.pop()  ## the previous line results in one record too many so pop it
partnerships = [[[int(k) for k in j.split("-")] for j in i.split(",")] for i in data]
hits = 0
for p in partnerships:
    if (p[0][0] <= p[1][0] and p[0][1] >= p[1][1]) or (
        p[1][0] <= p[0][0] and p[1][1] >= p[0][1]
    ):
        hits += 1
print(hits)
