import re

s = '....123....'
t = '123....'
u = '....123'
pat = '\w[0-9]+\w'
a = re.search(pat, s).span()[0]
b = re.search(pat, t).span()[0]
c = re.search(pat, u).span()[0]
print(a)
print(b)
print(c)
