debug=True
if debug:
	f = open("inputs/in14Example.txt", "r")
else:
	 f = open("inputs/in14.txt", "r")
txt = f.readlines()
f.close()

# 500,0 is the + (sand)
xMax = 0
yMax = 0
xMin = 99999
yMin = 99999
for line in txt:
    line = line.rstrip("\n")
    n = line.split(" -> ")
    for i in range(len(n)):
        (x,y) = n[i].split(",")
        x = int(x)-500
        y = int(y)
        xMax = max(xMax,x)
        xMin = min(xMin,x)
        yMax = max(yMax,y)
        yMin = min(yMin,y)


index = []
map_ = []
i = 0
print(f'X max,min = {xMin},{xMax}')
print(f'Y max,min = {yMin},{yMax}')
if yMin >0:
    yMin = 0
for y in range(yMin,yMax+1):
    map_.append([])
    index = []
    for x in range(xMin,xMax+1):
        map_[i].append(".")
        index.append(x)

    i+=1

offsetToZero = 0
offsetToZero= -xMin

for line in txt:
    line = line.rstrip("\n")
    n = line.split(" -> ")
    for i in range(len(n)-1):
        (x,y) = n[i].split(",")
        x = int(x)-500
        y = int(y)

        (x1,y1) = n[i+1].split(",")
        x1 = int(x1)-500
        y1 = int(y1)
        print(f'x={x}, y={y}, x1={x1}, y1={y1}')

        if (x==x1):
            for yy in range(0,yMax+1):
                if ((yy>=min(y,y1)) and (yy <= max(y,y1))):
                    map_[yy][x+offsetToZero] = "#"
        else: # y==y1
            for xx in range(min(x,x1),max(x,x1)+1):
                print(xx)
                map_[y][xx+offsetToZero] = "#"

# Look for 0 on the top, and add "+"
start = []
for i in range(len(map_)):
    if (index[i] == 0):
        map_[0][i] = "+"
        start = [0,i]
# The map is finally built.....


print(index)
for k in range(len(map_)):
    mapTxt = "".join(map_[k])
    print(f'{k} {mapTxt}')

def goDown(_map, curY, curX):
    if (_map[curY+1][curX] != "."):
        return False
    else:
        return True

def goOut(_map, curY, curX):
    if ((curX-1) < 0):
        return True
    if ((curX+1) > len(_map[0])):
        return True
    if ((curY+1)>len(_map)):
        return True
    return False

def goDownLeft(_map,curY,curX):
    if (_map[curY+1][curX-1] == "."):
        return True
    return False

def goDownRight(_map,curY,curX):
    if (_map[curY+1][curX+1] == "."):
        return True
    return False


goOn = True
x = start[1]
y = start[0]
while goOn:
    if goOut(map_,y,x):
        goOn = False
    elif goDown(map_,y,x):
        x = x
        y = y + 1
    elif goDownLeft(map_,y,x):
        x = x - 1
        y = y + 1
    elif goDownRight(map_,y,x):
        x = x + 1
        y = y + 1
    else : # stay where you are, little sand
        map_[y][x] = "o"
        x = start[1]
        y = start[0]



print(index)
for k in range(len(map_)):
    mapTxt = "".join(map_[k])
    print(f'{k} {mapTxt}')


