f = open('inputsamp.txt','r')
f = open('input.txt','r')
data = f.read().split('\n')
data.pop() ## the previous line results in one record too many so pop it

new_list = list(data)
for i, val in enumerate(data[0]):
    wk_list = []
    count_1 = 0
    count_0 = 0
    for j in new_list:
        if j[i] == '1':
            count_1 += 1
        else:
            count_0 += 1
    if count_1 >= count_0:
        majority = '1'
    else:
        majority = '0'
    for j in new_list:
        if j[i] == majority:
            wk_list.append(j)
    new_list = list(wk_list)
    if len(new_list) == 1:
        break
oxygen_generator_rating = int(new_list[0], 2)

new_list = list(data)
for i, val in enumerate(data[0]):
    wk_list = []
    count_1 = 0
    count_0 = 0
    for j in new_list:
        if j[i] == '1':
            count_1 += 1
        else:
            count_0 += 1
    if count_1 >= count_0:
        minority = '0'
    else:
        minority = '1'
    for j in new_list:
        if j[i] == minority:
            wk_list.append(j)
    new_list = list(wk_list)
    if len(new_list) == 1:
        break
CO2_scrubber_rating = int(new_list[0], 2)
print oxygen_generator_rating * CO2_scrubber_rating
