 f = open("inputs/in10.txt", "r")

def manageCycle(curCycle,cycles,x,img):
    inLine = (curCycle%40)
    if (inLine==0):
        img +="\n"
    print(f'x={x}, inLine={inLine}')
    if ((x-1)<=inLine and (x+1)>=inLine):
        img += "#"
    else:
        img += "."
    
    curCycle += 1
    cycles[curCycle] = x
    return (curCycle,cycles,img)

x = 1
txt=""
cycles = {} # To save for debug
curCycle = 0 # Number of current cycle
for line in f.readlines():
    line = line.rstrip("\n")
    if (line[:4]=="noop"):
        (curCycle,cycles,txt) = manageCycle(curCycle,cycles,x,txt)
    else:
        (instruction,V) = line.split()
        (curCycle,cycles,txt) = manageCycle(curCycle,cycles,x,txt)
        (curCycle,cycles,txt) = manageCycle(curCycle,cycles,x,txt)
        x +=  int(V) # Result is computed at the end of the 2 cycles

f.close()
strength = {}
for e in cycles.keys():
    strength[e] = e*cycles[e]


sum = 0
for i in [20,60,100,140,180,220]:
    sum += strength[i]

print(f'sum of 20,60,100,140,180 and 220 is {sum}')
print(txt)
