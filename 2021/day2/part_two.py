f = open('inputsamp.txt','r')
f = open('input.txt','r')
xlist = f.read().split('\n')
xlist.pop()
lines = len(xlist)
xlist = [x.split(' ') for x in xlist]
newlist = []
for item in xlist:
    newlist.append((item[0], int(item[1])))
aim = 0
horizontal = 0
depth = 0
for item in newlist:
    if item[0] == 'forward':
        horizontal += item[1]
        depth += aim * item[1]
    if item[0] == 'down':
        aim += item[1]
    if item[0] == 'up':
        aim -= item[1]
print 'lines:       ', lines
print 'horizontal:  ', horizontal
print 'depth:       ', depth
print 'answer:      ', horizontal * depth

