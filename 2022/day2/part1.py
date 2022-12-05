# f = open("sample.txt", "r")
f = open("input.txt", "r")
data = f.read().split("\n")
data.pop()  ## the previous line results in one record too many so pop it
score = 0
for i in data:
    line = i.split(" ")
    if line[0] == "A" and line[1] == "X":
        score += 4
    if line[0] == "A" and line[1] == "Y":
        score += 8
    if line[0] == "A" and line[1] == "Z":
        score += 3
    if line[0] == "B" and line[1] == "X":
        score += 1
    if line[0] == "B" and line[1] == "Y":
        score += 5
    if line[0] == "B" and line[1] == "Z":
        score += 9
    if line[0] == "C" and line[1] == "X":
        score += 7
    if line[0] == "C" and line[1] == "Y":
        score += 2
    if line[0] == "C" and line[1] == "Z":
        score += 6
print(score)
