f = open('input1.txt','r')
xlist = f.read().split('\n')
xlist.pop()
newlist = [int(x) for x in xlist]
increases = 0
items = 0
prev = newlist.pop(0)
while len(newlist) > 0:
    items += 1
    if newlist[0] > prev:
        increases += 1
    prev = newlist.pop(0)
print 'items:     ',  items
print 'increases: ',  increases

