f = open("inputs/in14.txt", "r")
txt = f.readlines()
f.close()

##########################
# Build the stupid map
# 500,0 is the + (sand)
##########################

# Find the max of elements for X and Y 
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

# Now, build an "empty" map with all dots in it 
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

# Build an offset to 0, because 0 is not our first index, but the tab starts at 0
offsetToZero= -xMin

# Now, find the # positions 
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

        if (x==x1):
            for yy in range(0,yMax+1):
                if ((yy>=min(y,y1)) and (yy <= max(y,y1))):
                    map_[yy][x+offsetToZero] = "#"
        else: # y==y1
            for xx in range(min(x,x1),max(x,x1)+1):
                map_[y][xx+offsetToZero] = "#"

map_.append([])
map_.append([])
for xx in range(len(map_[0])):
    map_[-2].append(".")
    map_[-1].append("#")

def increaseMap(_map, _index):

    # Add double of elements at right and left
    # I think this is the easiest way to deal with "infinite line" on the bottom
    n = int(len(_map[0])*6)
    temp = []
    idx1 = []
    idx2 = []
    diez = []
    for i in range(n):
        temp.append(".")
        diez.append("#")
        idx1.append(xMin-i)
        idx2.append(xMax+i)

    idx1.reverse()
    _index = idx1+_index+idx2

    for yy in range(len(_map)):
        if (yy == len(_map)-1):
            _map[yy] = diez+_map[yy]+diez
        else:
            _map[yy] = temp+_map[yy]+temp
    return (_map, _index)

(map_, index) = increaseMap(map_,index)

# Look for 0 on the top, and add "+"
# Save the position
start = []
for i in range(len(map_[0])):
    if (index[i] == 0):
        map_[0][i] = "+"
        start = [0,i]

# Print all of it
print(index)
for k in range(len(map_)):
    mapTxt = "".join(map_[k])
    print(f'{k} {mapTxt}')

print("")

##########################
# The map is finally built.....
# Now, let the sand fall !
##########################

def goDown(_map, curY, curX):
    if (_map[curY+1][curX] != "."):
        return False
    else:
        return True

def goDownLeft(_map,curY,curX):
    if (_map[curY+1][curX-1] == "."):
        return True
    return False

def goDownRight(_map,curY,curX):
    if (_map[curY+1][curX+1] == "."):
        return True
    return False

# Get start point
goOn = True
x = start[1]
y = start[0]
units = 0
# Go on, find the sand positions 
while goOn:
    if goDown(map_,y,x):
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
        units += 1
        if (x == start[1] and y == start[0]): # Not moving anymore, this is the end
            goOn = False
        x = start[1]
        y = start[0]

        # Print all of it because it's cool 
        for k in range(len(map_)):
            mapTxt = "".join(map_[k])
            print('{:02d} {:s}'.format(k,mapTxt))

print (f"There are {units} of sand")

