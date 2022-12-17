def manageCycle(cycle,x,res,img):
    inLine = (cycle%40)
    if (inLine==0):
        img +="\n"
    if ((x-1)<=inLine and (x+1)>=inLine):
        img += "#"
    else:
        img += "."
    
    cycle += 1
    if cycle in [20,60,100,140,180,220]:
        res += (cycle*x)
    return (cycle,res,img)

x = 1
txt=""
cycle = 0 # Number of current cycle
res = 0
f = open("inputs/in10.txt", "r")
for line in f.readlines():
    line = line.rstrip("\n")
    if (line[:4]=="noop"):
        (cycle,res,txt) = manageCycle(cycle,x,res,txt)
    else:
        (instruction,V) = line.split()
        (cycle,res,txt) = manageCycle(cycle,x,res,txt)
        (cycle,res,txt) = manageCycle(cycle,x,res,txt)
        x +=  int(V) # Result is computed at the end of the 2 cycles

f.close()

print(f'sum of 20,60,100,140,180 and 220 is {res}')
print(txt)
