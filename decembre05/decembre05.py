import os
path = os.path.dirname(os.path.abspath(__file__))
file1 = path+"/../inputs/in05.txt"
file2 = path+"/../inputs/in05.1.txt"

# Build table
f = open(file1, "r")
tab = {}
for line in f.readlines():
    line = line.rstrip("\n")
    if (line != ""):
        j = 1 # First column 
        for i in range(0,len(line),4): # For each column 
            if (j not in tab.keys()): # If column does not exist
                tab[j] = [] # create it 
            c = line[i:i+4] # Isolate key
            c = " ".join(c.split()) # Remove all " " to only one
            if (c != ""): # If not empty (no key)
                tab[j].insert(0,c) # Insert it at beginning of table/column
            j = j+1 # Next column
f.close()

# Copy each list of the dictionary 
tab2 = {}
for j in tab.keys():
    tab2[j] = tab[j].copy()

f = open(file2, "r")
for line in f.readlines():
    line = line.rstrip("\n")
    e = line.split()
    nbr = int(e[1])
    start = int(e[3])
    end = int(e[5])
    # Part1
    for i in range(nbr):
        m = tab[start].pop() # Remove last item of start list on the top
        tab[end].append(m) # Add it on the top of the new one
    # Part2
    if (nbr == 1):  
        m = tab2[start].pop() # Remove last item of start list on the top
        tab2[end].append(m) # Add it on the top of the new one
    else:
        slot = len(tab2[start])-nbr
        for i in range(nbr): # take several items
            m = tab2[start].pop(slot) # Remove items in order on the top of the column
            # Always take slot not i as index, because the size of the list will change each time we pop an element
            tab2[end].append(m) # Add it on the top of the new one
f.close()

def getEnds(tab):
    print("End of each column :")
    txt = ""
    result = ""
    for k in tab.keys():
        m = tab[k].pop()
        txt += m
        result += m.replace("[", "").replace("]", "")
    print(txt)
    print(result)

print("########## Table 1 ##########")
getEnds(tab)

print("########## Table 2 ##########")
getEnds(tab2)
