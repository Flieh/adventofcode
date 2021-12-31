def main():
    f = open('input.txt', 'r')
    xlist = f.read().split()
    current_position = 0 
    tree_count = 0
    tree_count_list = []
    
    for line in xlist:
        if line[current_position] == '#':
            tree_count += 1
        current_position = (current_position + 1) % len(line)
    tree_count_list.append(tree_count)
    tree_count = 0
    current_position = 0 
    
    for line in xlist:
        if line[current_position] == '#':
            tree_count += 1
        current_position = (current_position + 3) % len(line)
    tree_count_list.append(tree_count)
    tree_count = 0
    current_position = 0 
   
    for line in xlist:
        if line[current_position] == '#':
            tree_count += 1
        current_position = (current_position + 5) % len(line)
    tree_count_list.append(tree_count)
    tree_count = 0
    current_position = 0 
  
    for line in xlist:
        if line[current_position] == '#':
            tree_count += 1
        current_position = (current_position + 7) % len(line)
    tree_count_list.append(tree_count)
    tree_count = 0
    current_position = 0 
   
    skip = True
    for line in xlist[::2]:
        if line[current_position] == '#':
            tree_count += 1
        current_position = (current_position + 3) % len(line)
    tree_count_list.append(tree_count)
    tree_count = 0
    current_position = 0 

    product = 1
    for count in tree_count_list:
        product *= count

    return product


print(main())
