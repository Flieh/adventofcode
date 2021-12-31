# f = open('input1samp.txt','r')
f = open('input1.txt','r')
xlist = f.read().split('\n')
xlist.pop()
int_list = [int(x) for x in xlist]
wk_list = []
for i,val in enumerate(int_list[:-2]):
    wk_list.append(int_list[i] + int_list[i+1] + int_list[i+2])

increases = 0
items = 1
prev = wk_list.pop(0)
while len(wk_list) > 0:
    items += 1
    if wk_list[0] > prev:
        increases += 1
    prev = wk_list.pop(0)
print 'items:     ',  items
print 'increases: ',  increases

