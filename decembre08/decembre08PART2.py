import os
path = os.path.dirname(os.path.abspath(__file__))
file = path+"/../inputs/in08.txt"

debug = False
if debug:
    f = open("in08Example.txt", "r")
else:
    f = open(file, "r")

table = []
SCENIC = []

for line in f.readlines():
    line = line.rstrip("\n")
    line = list(line)
    table.append(line)

for i in range(0, len(table)): # Parse lines
    h = table[i]
    for j in range(0,len(h)): # Parse in the line (so column)
        cur = int(h[j])
        print(f'Current={cur}')
        N = 1
        NEIB = 1
        for k in range(j-1,-1,-1): # left part
            print(f'Left = {h[k]}')
            if ((int(h[k])>= cur) or (k == 0)):
                break
            NEIB = NEIB + 1
        
        print(f'NEIB={NEIB}')
        N = N * NEIB
        NEIB = 1

        for k in range(j+1,len(h)): # right part
            print(f'Right = {h[k]}')
            if ((int(h[k])>= cur) or (k >= len(h)-1)):
                break
            NEIB = NEIB + 1

        print(f'NEIB={NEIB}')
        N = N * NEIB
        NEIB = 1

        for k in range(0,i):
            print(f'Top = {table[k][j]}')
            if ((int(table[k][j]) >= cur) or (k == 0)):
                break
            NEIB = NEIB + 1

        print(f'NEIB={NEIB}')
        N = N * NEIB
        NEIB = 1

        for k in range(i+1,len(table)):
            print(f'Bottom = {table[k][j]}')
            if ((int(table[k][j]) >= cur) or (k >= len(table)-1)):
                break
            NEIB = NEIB + 1

        print(f'NEIB={NEIB}')
        N = N * NEIB
        
        print(f'N = {N}\n')
        SCENIC.append(N)

f.close()
SCENIC.sort()
print(SCENIC)
sum = 0
for e in SCENIC:
    sum = sum + e
print(sum)

