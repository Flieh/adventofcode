# f = open("sample.txt", "r")
f = open("input.txt", "r")
data = f.read().split("\n")
data.pop()  ## the previous line results in one record too many so pop it
instructions = [x for x in data if len(x) > 1 and x[0] == 'm']
data = [x for x in data if x not in instructions and len(x) > 1]
for line in data:
    if line.lstrip()[0] == '1':
        stackSize = int(line.rstrip()[-1])
        break
data.reverse()
stacks = []
for i in range(stackSize):
    stacks.append([])
for line in data:
    if len(line) < 1:
        continue
    if line.lstrip()[0] != '[':
        continue
    for pos, val in enumerate(line):
        if val == '[':
            stacks[pos // 4].append(line[pos + 1])
instNums = []
for line in instructions:
    lineArr = line.split(' ')
    lineArr = [int(x) for x in lineArr if x.isnumeric()]
    instNums.append(lineArr)
for line in instNums:
    tempStack = []
    for i in range(line[0]):
        tempStack.append(stacks[line[1] - 1].pop())
    for i in range(line[0]):
        stacks[line[2] - 1].append(tempStack.pop())
output = ''
for stack in stacks:
    output += stack.pop()
print(output)

