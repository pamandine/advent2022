f = open("decembre02.txt", "r")

opponent = {
        "A" : "R", # Rock
        "B" : "P", # Paper
        "C" : "S" # Scissors
        }
myself = {
    "X" : "R", # Rock
    "Y" : "P", # Papier
    "Z" : "S" # Scissors
        }

ROCK = 1
PAPER = 2
SCISSORS = 3

WON = 6
DRAW = 3
LOSS = 0

def whoWin(adv,me):
    ret = DRAW # Null
    if (adv == me):
        ret = DRAW
    elif ((adv == "R" and me == "P")
          or (adv == "S" and me == "R")
          or (adv == "P" and me == "S")):
        ret = WON # me win
    else:
        ret = LOSS # me fail
    return ret

def shapePoints(figure):
    points = 0
    if (figure == "R"):
        points = ROCK
    elif (figure == "S"):
        points = SCISSORS
    else:
        points = PAPER
    return points

myPoints = 0
for line in f.readlines():
    line = line.rstrip("\n")
    step = line.split()
    adv = opponent[step[0]]
    me = myself[step[1]]
    winPoints = whoWin(adv, me)
    figurePoints = shapePoints(me)
    myPoints = myPoints + winPoints + figurePoints 
    print(f'adv={adv}, me={me}, winPts={winPoints}, shapePts={figurePoints}, sumPoints={myPoints}')

print(myPoints)

f.close()
