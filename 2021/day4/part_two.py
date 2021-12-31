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
    boards.append(board)

drawn = []
winners = []
for i in range(4):
    drawn.append(draw_numbers.pop(0))
while len(winners) < len(boards): 
    win = False
    while not win:
        drawn.append(draw_numbers.pop(0))
        for board in boards:
            if boards.index(board) in winners:
                continue
            for line in board: count = 0
                for number in line:
                    if number in drawn:
                        count += 1
                if count == 5:
                    win = True
                    winners.append(boards.index(board))
numbers = []
loser = boards[winners[-1]]
for i in range(5):
    for number in loser[i]:
        if number not in drawn:
            numbers.append(int(number))
print(boards.index(loser))
print(drawn[-1])
print(sum(numbers) * int(drawn[-1]))
