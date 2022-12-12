import os
path = os.path.dirname(os.path.abspath(__file__))
file = path+"/../inputs/in02.txt"

ROCK = 1
PAPER = 2
SCISSORS = 3

WON = 6
DRAW = 3
LOSS = 0

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
predict = {
    "X" : LOSS, 
    "Y" : DRAW,
    "Z" : WON
        }
expected = { # What should I have to lose, win or draw
    DRAW : {
        "P" : "P",
        "S" : "S",
        "R" : "R",
        },
    LOSS : {
        "P" : "R",
        "S" : "P", 
        "R" : "S",
        },
    WON : {
        "P" : "S", 
        "R" : "P", 
        "S" : "R",
        },
     }

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

def whatShape(adv,result):
    return expected[result][adv]

def shapePoints(figure):
    points = 0
    if (figure == "R"):
        points = ROCK
    elif (figure == "S"):
        points = SCISSORS
    else:
        points = PAPER
    return points

def func1(lines):
    myPoints = 0
    for line in lines:
        line = line.rstrip("\n")
        step = line.split()
        adv = opponent[step[0]]
        me = myself[step[1]]
        winPoints = whoWin(adv, me)
        figurePoints = shapePoints(me)
        myPoints = myPoints + winPoints + figurePoints 
        #print(f'adv={adv}, me={me}, winPts={winPoints}, shapePts={figurePoints}, sumPoints={myPoints}')

    print(myPoints)

def func2(lines):
    myPoints = 0
    for line in lines:
        line = line.rstrip("\n")
        step = line.split()
        adv = opponent[step[0]] # Opponent shape
        winPoints = predict[step[1]] # What I should do (DRAW, WIN, LOSS). These are directly the points
        me = whatShape(adv,winPoints)
        figurePoints = shapePoints(me)
        myPoints = myPoints + winPoints + figurePoints 
        #print(f'adv={adv}, me={me}, winPts={winPoints}, shapePts={figurePoints}, sumPoints={myPoints}')

    print(myPoints)

f = open(file, "r")
lines = f.readlines()
print('Call function 1')
func1(lines)
print('Call function 2')
func2(lines)
f.close()
