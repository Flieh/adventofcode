f = open('inputsamp.txt','r')
f = open('input.txt','r')
data = f.read().split('\n')
data.pop() ## the previous line results in one record too many so pop it

draw_numbers = data.pop(0).split(',')
boards = []
while len(data):
    if data.pop(0) == '':
        board = []
        for i in range(5):
            board.append(data.pop(0).split())
        for i in range(5):
            line = []
            for j in range(5):
                line.append(board[j][i])
            board.append(line)
        line = []
        for i in range(5):
            line.append(board[i][i])
        board.append(line)
        line = []
        i = 4
        j = 0
        for x in range(5):
            line.append(board[i][j])
            i -= 1
            j += 1
        board.append(line)
    boards.append(board)

drawn = []
for i in range(4):
    drawn.append(draw_numbers.pop(0))
win = False
while not win:
    drawn.append(draw_numbers.pop(0))
    for board in boards:
        for line in board:
            count = 0
            for number in line:
                if number in drawn:
                    count += 1
            if count == 5:
                win = True
                winner = board
numbers = []
for i in range(5):
    for number in winner[i]:
        if number not in drawn:
            numbers.append(int(number))
print sum(numbers) * int(drawn.pop())



