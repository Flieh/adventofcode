# f = open("sample.txt", "r")
f = open("input.txt", "r")
data = f.read().split("\n")
data.pop()  ## the previous line results in one record too many so pop it
score = 0
for i in data:
    line = i.split(" ")
    if line[0] == "A" and line[1] == "X":  # A = rock     1
        score += 3  # B = paper    2
    if line[0] == "A" and line[1] == "Y":  # C = scissors 3
        score += 4  # X = lose     0 A->C B->A C->B
    if line[0] == "A" and line[1] == "Z":  # Y = tie      3 A->A B->B C->C
        score += 8  # Z = win      6 A->B B->C C->A
    if line[0] == "B" and line[1] == "X":
        score += 1
    if line[0] == "B" and line[1] == "Y":
        score += 5
    if line[0] == "B" and line[1] == "Z":
        score += 9
    if line[0] == "C" and line[1] == "X":
        score += 2
    if line[0] == "C" and line[1] == "Y":
        score += 6
    if line[0] == "C" and line[1] == "Z":
        score += 7
print(score)
