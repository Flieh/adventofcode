f = open('input.txt','r')
xlist = f.read().split('\n')
xlist.pop()
for x in xlist:
    for y in xlist:
        for z in xlist:
            if int(x) + int(y) + int(z) == 2020:
                print(int(x) * int(y) * int(z))
