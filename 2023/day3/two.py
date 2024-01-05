import re

masterlist = []
array = []
symbols = []

pattern = r'(=|\/|-|\+|\*|%|\$|#|@|&)'

filename = "data.txt"

with open(filename, 'r') as f:
    for line in f.readlines():
        array.append(line.strip().split(' '))

def combine_numbers(numbers):
    combined_number = int(''.join(map(str, numbers)))
    
    return combined_number

def findsymbols(symbolindex, line):
    for count, ele in enumerate(array[line][0]):
        symbol = re.findall(pattern, ele)
        if symbol:
            symbol = str(symbol[0])
            symbols.append(symbol)
            symbolindex.append(count)
            
    return symbolindex
     
def findleftright(line):
    
    symbolindex = []
    symbolindex = findsymbols(symbolindex, line)
    
    defrange = len(array[line][0]) - 1

    for index in symbolindex:
        
        lnum = []
        rnum = []
         
        increm = 1
        while increm < 4:
            if index - increm >= 0:
                if array[line][0][index - increm].isdigit():
                    print("left number at", str(index - increm))
                    lnum.append(int(array[line][0][index - increm]))
                    increm += 1
                else:
                    break
            else:
                break
        lnum = list(reversed(lnum))
        if lnum:
            lnum = combine_numbers(lnum)
            masterlist.append(lnum)
            print(lnum)
            
        increm = 1
        while increm < 4:
            if index + increm <= defrange:
                if array[line][0][index + increm].isdigit():
                    print("right number at", str(index + increm))
                    rnum.append(int(array[line][0][index + increm]))
                    increm += 1
                else:
                    break
            else:
                break
        if rnum:
            rnum = combine_numbers(rnum)
            masterlist.append(rnum)
            print(rnum)
        increm = 1

def findup(line):
    
    symbolindex = []
    symbolindex = findsymbols(symbolindex, line)
    
    defrange = len(array[line][0]) - 1

    for index in symbolindex:
        
        upleftnum = []
        uprightnum = []
         
        #initial check up
        increm = 1
        if array[line - 1][0][index].isdigit():
            print("up number at", str(index))
            temp = int(array[line - 1][0][index])
            #checks left
            increm = 1
            while increm < 4:
                if index - increm >= 0:
                    if array[line - 1][0][index - increm].isdigit():
                        print("left number at", str(index - increm))
                        upleftnum.insert(0, int(array[line - 1][0][index - increm]))
                        increm += 1
                    else:
                        break
                else:
                    break

            #checks right
            increm = 1
            while increm < 4:
                if index + increm <= defrange:
                    if array[line - 1][0][index + increm].isdigit():
                        print("right number at", str(index + increm))
                        uprightnum.append(int(array[line - 1][0][index + increm]))
                        increm += 1
                    else:
                        break
                else:
                    break
                
            if upleftnum and uprightnum:
                upleftnum.append(uprightnum[0])
                upleftnum.insert(1, temp)
                upleftnum = combine_numbers(upleftnum)
                masterlist.append(upleftnum)
                print(upleftnum)
                
            elif upleftnum:
                upleftnum.append(temp)
                upleftnum = combine_numbers(upleftnum)
                masterlist.append(upleftnum)
                print(upleftnum)
                
            elif uprightnum:
                uprightnum.insert(0, temp)
                uprightnum = combine_numbers(uprightnum)
                masterlist.append(uprightnum)
                print(uprightnum)
                
            elif temp:
                masterlist.append(temp)
                print(temp)
                
        else:
            #checks left
            increm = 1
            while increm < 4:
                if index - increm >= 0:
                    if array[line - 1][0][index - increm].isdigit():
                        print("upleft number at", str(index - increm))
                        upleftnum.insert(0, int(array[line - 1][0][index - increm]))
                        increm += 1
                    else:
                        break
                else:
                    break
                
            if upleftnum:
                upleftnum = combine_numbers(upleftnum)
                masterlist.append(upleftnum)
                print(upleftnum)

            #checks right
            increm = 1
            while increm < 4:
                if index + increm <= defrange:
                    if array[line - 1][0][index + increm].isdigit():
                        print("upright number at", str(index + increm))
                        uprightnum.append(int(array[line - 1][0][index + increm]))
                        increm += 1
                    else:
                        break
                else:
                    break
                  
            if uprightnum:
                uprightnum = combine_numbers(uprightnum)
                masterlist.append(uprightnum)
                print(uprightnum)

def finddown(line):
    
    symbolindex = []
    symbolindex = findsymbols(symbolindex, line)
    
    defrange = len(array[line][0]) - 1

    for index in symbolindex:
        
        downleftnum = []
        downrightnum = []
         
        #initial check down
        increm = 1
        if array[line + 1][0][index].isdigit():
            print("down number at", str(index))
            temp = int(array[line + 1][0][index])
            
            #checks left
            while increm < 4:
                if index - increm >= 0:
                    if array[line + 1][0][index - increm].isdigit():
                        print("left number at", str(index - increm))
                        downleftnum.insert(0, int(array[line + 1][0][index - increm]))
                        increm += 1
                    else:
                        break
                else:
                    break
                
            #checks right
            increm = 1
            while increm < 4:
                if index + increm <= defrange:
                    if array[line + 1][0][index + increm].isdigit():
                        print("right number at", str(index + increm))
                        downrightnum.append(int(array[line + 1][0][index + increm]))
                        increm += 1
                    else:
                        break
                else:
                    break
                
            if downleftnum and downrightnum:
                downleftnum.append(downrightnum[0])
                downleftnum.insert(1, temp)
                downleftnum = combine_numbers(downleftnum)
                masterlist.append(downleftnum)
                print(downleftnum)
                
            elif downleftnum:
                downleftnum.append(temp)
                downleftnum = combine_numbers(downleftnum)
                masterlist.append(downleftnum)
                print(downleftnum)
                
            elif downrightnum:
                downrightnum.insert(0, temp)
                downrightnum = combine_numbers(downrightnum)
                masterlist.append(downrightnum)
                print(downrightnum)
            
            elif temp:
                masterlist.append(temp)
                print(temp)
               
        else:
            #checks left
            increm = 1
            while increm < 4:
                if index - increm >= 0:
                    if array[line + 1][0][index - increm].isdigit():
                        print("downleft number at", str(index - increm))
                        downleftnum.insert(0, int(array[line + 1][0][index - increm]))
                        increm += 1
                    else:
                        break
                else:
                    break
                
            if downleftnum:
                downleftnum = combine_numbers(downleftnum)
                masterlist.append(downleftnum)
                print(downleftnum)
            
            #checks right
            increm = 1
            while increm < 4:
                if index + increm <= defrange:
                    if array[line + 1][0][index + increm].isdigit():
                        print("downright number at", str(index + increm))
                        downrightnum.append(int(array[line + 1][0][index + increm]))
                        increm += 1
                    else:
                        break
                else:
                    break
                
            if downrightnum:
                downrightnum = combine_numbers(downrightnum)
                masterlist.append(downrightnum)
                print(downrightnum)

with open(filename, 'r') as f:
    line = 0
    range = 140
    while line < range:
        if line - 1 < 0:
            findleftright(line)
            finddown(line)
            line += 1
        if line + 1 < range:
            findleftright(line)
            findup(line)
            finddown(line)
            line += 1
        else:
            findleftright(line)
            findup(line)
            line += 1

# print(array[line - 1][0])
# print(array[line][0])
# print(array[line + 1][0])

# print(symbols)
# print(symbolindex)

print(sorted(masterlist))
print(len(masterlist))
print(sum(masterlist))
