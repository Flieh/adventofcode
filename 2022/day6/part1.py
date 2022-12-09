# f = open("s1.data", "r")
# f = open("s2.data", "r")
# f = open("s3.data", "r")
# f = open("s4.data", "r")
# f = open("s5.data", "r")
f = open("i1.data", "r")
data = f.read().split("\n")
data.pop()  ## the previous line results in one record too many so pop it
chars = data[0]
print(chars)
counter = 0
segLen = 14
for i,v in enumerate(chars[segLen-1:]):
    slice = []
    for j in range(segLen):
        slice.append(chars[i+j])
    if len(set(slice)) == segLen:
        print(i + segLen)
        break
