import os
path = os.path.dirname(os.path.abspath(__file__))
file = path+"/../inputs/in08.txt"

f = open(file, "r")

TOTAL = 0
H = 0
IN = 0
table = []

for line in f.readlines():
    H = H + 1
    line = line.rstrip("\n")
    line = list(line)
    L = len(line)
    table.append(line)

# On ne fait pas la première ligne, puisqu'elle est à l'extérieur
# On ne fait pas la premier colonne et la dernière colonne
# On ne fait pas la dernière ligne
for i in range(1,len(table)-1): # Parse lines
    h = table[i]
    for j in range(1,len(h)-1): # Parse in the line (so column)
        # look for visibility on same line
        cur = int(h[j])
        VISIBLE = 4

        for k in range(0,j): # left part
            if (int(h[k])>= cur):
                VISIBLE = VISIBLE - 1
                break

        for k in range(j+1,len(h)): # right part
            if (int(h[k])>= cur):
                VISIBLE = VISIBLE - 1
                break

        for k in range(0,i):
            if (int(table[k][j]) >= cur):
                VISIBLE = VISIBLE - 1
                break

        for k in range(i+1,len(table)):
            if (int(table[k][j]) >= cur):
                VISIBLE = VISIBLE - 1
                break
        
        if (VISIBLE != 0):
            IN = IN + 1

f.close()

# Hauteur * 2 
# Longueur * 2 mais sans compter les arbres déjà dans Hauteur
# Les arbres dedans (IN)
TOTAL = TOTAL + 2*H + (L-2)*2 + IN
print("########## Function 1 ##########")
print(f'TOTAL={TOTAL}')


