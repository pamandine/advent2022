import os
path = os.path.dirname(os.path.abspath(__file__))
file = path+"/../inputs/in08.txt"

f = open(file, "r")

height = 0
IN = 0
forest = []
SCENIC = 0

for line in f.readlines():
    height = height + 1
    line = line.rstrip("\n")
    line = list(line)
    L = len(line)
    forest.append(line)
f.close()

# On ne fait pas la première ligne, puisqu'elle est à l'extérieur
# On ne fait pas la premier colonne et la dernière colonne
# On ne fait pas la dernière ligne
for i in range(1,len(forest)-1): # Parse lines
    for j in range(1,len(forest[i])-1): # Parse in the line (so column)
        # look for visibility on same line
        tree = int(forest[i][j])
        isTreeVisible = [True, True, True, True]
        SCORE = [0,0,0,0]

        for k in range(j-1,-1,-1): # left part
            SCORE[0] += 1
            if (int(forest[i][k]) >= tree):
                isTreeVisible[0] = False
                break

        for k in range(j+1,len(forest[i])): # right part
            SCORE[1] += 1
            if (int(forest[i][k])>= tree):
                isTreeVisible[1] = False
                break

        for k in range(i-1,-1,-1): # top part
            SCORE[2] += 1
            if (int(forest[k][j]) >= tree):
                isTreeVisible[2] = False
                break

        for k in range(i+1,len(forest)): # bottom
            SCORE[3] += 1
            if (int(forest[k][j]) >= tree):
                isTreeVisible[3] = False
                break
        
        if (True in isTreeVisible):
            IN = IN + 1

        SCENIC = max(SCENIC, SCORE[0]*SCORE[1]*SCORE[2]*SCORE[3])


# Hauteur * 2 
# Longueur * 2 mais sans compter les arbres déjà dans Hauteur
# Les arbres dedans (IN)
total_visible_trees = 2*height + (L-2)*2 + IN
print("########## Function 1 ##########")
print(f'total_visible_trees visible trees={total_visible_trees}')

print("########## Function 2 ##########")
print (f'MAX SCENIC={SCENIC}')


