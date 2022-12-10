f = open("s1.data", "r")
# f = open("i1.data", "r")
data = f.read().split("\n")
data.pop()  ## the previous line results in one record too many so pop it
tokens = []
for line in data:
    tokens.append(line.split(' '))
print(tokens)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dogA = Dog('Fido',5)

print(dogA.name)



