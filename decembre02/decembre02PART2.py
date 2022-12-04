f = open("decembre02.txt", "r")

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


myPoints = 0
for line in f.readlines():
    line = line.rstrip("\n")
    step = line.split()
    adv = opponent[step[0]] # Opponent shape
    winPoints = predict[step[1]] # What I should do (DRAW, WIN, LOSS). These are directly the points
    me = whatShape(adv,winPoints)
    figurePoints = shapePoints(me)
    myPoints = myPoints + winPoints + figurePoints 
    print(f'adv={adv}, me={me}, winPts={winPoints}, shapePts={figurePoints}, sumPoints={myPoints}')

print(myPoints)

f.close()
