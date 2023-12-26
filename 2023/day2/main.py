""" aoc 2023 dayx """


def fetch():
    """get input data"""
    with open("data.txt") as file:
        # with open('data.txt') as file:
        init_data = file.read().split("\n")
    init_data.pop()
    return init_data


def part_one():
    games = fetch()
    RED = 12
    GREEN = 13
    BLUE = 14
    retVal = 0
    games = [
        [game.split(":")[0].split()[1], game.split(":")[1].replace(";", ",")]
        for game in games
    ]
    for game in games:
        gameOK = True
        gameVal = int(game[0])
        for throw in game[1].split(","):
            if throw.split()[1] == "red" and int(throw.split()[0]) > RED:
                gameOK = False
                break
            if throw.split()[1] == "green" and int(throw.split()[0]) > GREEN:
                gameOK = False
                break
            if throw.split()[1] == "blue" and int(throw.split()[0]) > BLUE:
                gameOK = False
                break
        if gameOK:
            retVal += gameVal
    print(retVal)


def part_two():
    games = fetch()
    retVal = 0
    games = [
        [game.split(":")[0].split()[1], game.split(":")[1].replace(";", ",")]
        for game in games
    ]
    for game in games:
        maxRed = 0
        maxGreen = 0
        maxBlue = 0
        for throw in game[1].split(","):
            if throw.split()[1] == "red" and int(throw.split()[0]) > maxRed:
                maxRed = int(throw.split()[0])
            if throw.split()[1] == "green" and int(throw.split()[0]) > maxGreen:
                maxGreen = int(throw.split()[0])
            if throw.split()[1] == "blue" and int(throw.split()[0]) > maxBlue:
                maxBlue = int(throw.split()[0])
        retVal += maxRed * maxGreen * maxBlue
    print(retVal)


if __name__ == "__main__":
    # part_one()
    part_two()
