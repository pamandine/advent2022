debug=True
if debug:
	f = open("inputs/in10Example.txt", "r")
else:
	 f = open("inputs/in10.txt", "r")

x = 1
img=""
cycles = {} # To save for debug
curCycle = 0 # Number of current cycle
for line in f.readlines():
    line = line.rstrip("\n")
    if (line[:4]=="noop"):
        curCycle += 1
        cycles[curCycle] = x        
    else:
        (instruction,V) = line.split()
        curCycle += 1
        cycles[curCycle] = x        
        curCycle += 1
        cycles[curCycle] = x        
        x +=  int(V) # Result is computed at the end of the 2 cycles

f.close()
strength = {}
for e in cycles.keys():
    strength[e] = e*cycles[e]


sum = 0
for i in [20,60,100,140,180,220]:
    sum += strength[i]

print(f'sum of 20,60,100,140,180 and 220 is {sum}')
