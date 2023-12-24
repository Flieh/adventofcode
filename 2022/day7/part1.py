import sys

# f = open("s1.data", "r")
f = open("i1.data", "r")
data = f.read().split("\n")
data.pop()  ## the previous line results in one record too many so pop it
data = [line.split(" ") for line in data]


class Dir:
    objecttype = "directory"

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = {}

    def get_size(self):
        size = sum(self.files.values())
        for child in self.children:
            size += globals()[child].get_size()
        return size


globals()["/"] = Dir("/", None)
dirs = []
curDir = "/"
dirs.append("/")
for line in data:

    if line[0] == "dir" and not (line[1] in globals()):  # test dir declared
        # declare new dir with curDir as parent
        globals()[line[1]] = Dir(line[1], globals()[curDir].name)
        dirs.append(line[1])
        # attach dir to curDir as child
        globals()[curDir].children.append(line[1])

    if line[0] == "$" and line[1] == "cd":  # test for directory change
        if line[2] in globals():
            curDir = line[2]
        elif line[2] == ".." and curDir != "/":
            curDir = globals()[curDir].parent
        elif line[2] == "/":
            curDir = line[2]
        else:
            globals()[line[2]] = Dir(line[2], curDir)
            dirs.append(line[2])
            globals()[curDir].children.append(line[2])  # attach dir to curDir as child
            curDir = line[2]
        print(curDir)

    if line[0].isnumeric():
        globals()[curDir].files[line[1]] = int(line[0])

total = 0
for g in dirs:
    if globals()[g].get_size() <= 100000:
        total += globals()[g].get_size()
print(total)
