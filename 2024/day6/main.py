""" aoc 2024 day1 """
# import re

def fetch():
    """ get input data """
    with open('data.txt') as file:
        # with open('data.txt') as file:
        init_data = file.read().split('\n')
    init_data.pop()
    return init_data

def part_one():
    data = fetch()

    # get dimensions of the grid (depth x width)
    depth = len(data)
    width = len(data[0])

    # create grid from data
    grid = []
    for line in data:
        gridLine = []
        for token in line:
            gridLine.append(token)
        grid.append(gridLine)


    # get heading and coords of sprite
    indFound = False
    for i,v in enumerate(data):
        for j,w in enumerate(v):
            if w in ('^', '>', 'v','<' ):
                sprite = w
                spritePos = [i,j]
                indFound = True
                break
        if indFound == True:
            break

    # move the sprite according to its heading, test for # (turn) and for movement off grid 
    onGrid = True

    while onGrid == True:
        if sprite == '^':
            grid[spritePos[0]][spritePos[1]] = 'X'
            if spritePos[0] - 1 in range(0,depth):
                nextPos = [spritePos[0] - 1, spritePos[1]]
                if data[nextPos[0]][nextPos[1]] == '#':
                    sprite = '>'
                    continue
                else:
                    spritePos = nextPos
            else:
                onGrid = False

        if sprite == '>':
            grid[spritePos[0]][spritePos[1]] = 'X'
            if spritePos[1] + 1 in range(0,width):
                nextPos = [spritePos[0], spritePos[1] + 1]
                if data[nextPos[0]][nextPos[1]] == '#':
                    sprite = 'v'
                    continue
                else:
                    spritePos = nextPos
            else:
                onGrid = False

        if sprite == 'v':
            grid[spritePos[0]][spritePos[1]] = 'X'
            if spritePos[0] + 1 in range(0,depth):
                nextPos = [spritePos[0] + 1, spritePos[1]]
                if data[nextPos[0]][nextPos[1]] == '#':
                    sprite = '<'
                    continue
                else:
                    spritePos = nextPos
            else:
                onGrid = False

        if sprite == '<':
            grid[spritePos[0]][spritePos[1]] = 'X'
            if spritePos[1] - 1 in range(0,width):
                nextPos = [spritePos[0], spritePos[1] - 1]
                if data[nextPos[0]][nextPos[1]] == '#':
                    sprite = '^'
                    continue
                else:
                    spritePos = nextPos
            else:
                onGrid = False

    # count the number of Xs on the grid from sprite movement 
    nbX = 0
    for line in grid:
        for token in line:
            if token == 'X':
                nbX += 1

    # return the number of Xs
    return nbX


def part_two():
    global data, depth, width, grid, initSprite, initSpritePos, debug
    data = fetch()

    # get dimensions of the grid (depth x width)
    depth = len(data)
    width = len(data[0])


    # get initial heading and coords of sprite
    indFound = False
    for i,v in enumerate(data):
        for j,w in enumerate(v):
            if w in ('^', '>', 'v','<' ):
                initSprite = w
                initSpritePos = [i,j]
                indFound = True
                break
        if indFound == True:
            break

    # create maps with one extra obstacle, then test if the map loops
    loopingMaps = 0
    for i, v in enumerate(data):
        debug = False
        for j, w in enumerate(v):
            if w != '#':
                grid = createGridWithObstacle(i,j)
                if (i,j) == (6,3):
                    debug = True
                if isGridLoop() == True:
                    loopingMaps += 1

    # return number of looping maps
    return loopingMaps

def isGridLoop():
    # move the sprite according to its heading, test for # (turn), for loop and for movement off grid (end of test) onGrid = True
    northBoundCoords = []
    westBoundCoords = []
    southBoundCoords = []
    eastBoundCoords = []
    sprite = initSprite
    spritePos = initSpritePos
    indLoop = False
    onGrid = True
    while onGrid == True:
        if debug:
            print()
            for line in grid:
                print(''.join(line))
        # test for loop, if i've already been here with the same heading
        if sprite == '^':
            if spritePos in northBoundCoords:
                # i'm in a loop
                indLoop = True
                break 
            else:
                northBoundCoords.append(spritePos)
            grid[spritePos[0]][spritePos[1]] = 'X'
            if spritePos[0] - 1 in range(0,depth):
                nextPos = [spritePos[0] - 1, spritePos[1]]
                if data[nextPos[0]][nextPos[1]] == '#':
                    sprite = '>'
                    continue
                else:
                    spritePos = nextPos
            else:
                onGrid = False

        if sprite == '>':
            if spritePos in eastBoundCoords:
                # i'm in a loop
                indLoop = True
                break 
            else:
                eastBoundCoords.append(spritePos)
            grid[spritePos[0]][spritePos[1]] = 'X'
            if spritePos[1] + 1 in range(0,width):
                nextPos = [spritePos[0], spritePos[1] + 1]
                if data[nextPos[0]][nextPos[1]] == '#':
                    sprite = 'v'
                    continue
                else:
                    spritePos = nextPos
            else:
                onGrid = False

        if sprite == 'v':
            if spritePos in southBoundCoords:
                # i'm in a loop
                indLoop = True
                break 
            else:
                southBoundCoords.append(spritePos)
            grid[spritePos[0]][spritePos[1]] = 'X'
            if spritePos[0] + 1 in range(0,depth):
                nextPos = [spritePos[0] + 1, spritePos[1]]
                if data[nextPos[0]][nextPos[1]] == '#':
                    sprite = '<'
                    continue
                else:
                    spritePos = nextPos
            else:
                onGrid = False

        if sprite == '<':
            if spritePos in westBoundCoords:
                # i'm in a loop
                indLoop = True
                break 
            else:
                westBoundCoords.append(spritePos)
            grid[spritePos[0]][spritePos[1]] = 'X'
            if spritePos[1] - 1 in range(0,width):
                nextPos = [spritePos[0], spritePos[1] - 1]
                if data[nextPos[0]][nextPos[1]] == '#':
                    sprite = '^'
                    continue
                else:
                    spritePos = nextPos
            else:
                onGrid = False

    return indLoop
    # end isGridLoop

# create grid from data
def createGridWithObstacle(i,j):
    grid = []
    for line in data:
        gridLine = []
        for token in line:
            gridLine.append(token)
        grid.append(gridLine)
    grid[i][j] = '#'
    # grids look OK
    return grid

if __name__ == "__main__":
    # print(part_one())
    print(part_two())
