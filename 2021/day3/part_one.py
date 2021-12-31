f = open('inputsamp.txt','r')
f = open('input.txt','r')
data = f.read().split('\n')
data.pop() ## the previous line results in one record too many so pop it

bit_counts = []
for i in data[0]:
    bit_counts.append(0)

for d in data:
    for i, bit in enumerate(d): 
       bit_counts[i] += int(bit) 

gamma = ''
epsilon = ''
for count in bit_counts:
    if count > len(data) / 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
print int(gamma, 2) * int(epsilon, 2)

