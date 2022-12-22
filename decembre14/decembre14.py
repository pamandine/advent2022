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


print(index)
for k in range(len(map_)):
    print(f'{k} {map_[k]}')

