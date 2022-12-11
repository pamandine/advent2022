# Build table
f = open("decembre05Table.txt", "r")
tab = {}
for line in f.readlines():
    line = line.rstrip("\n")
    print(f'Line={line}')
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
    
print(tab)
f.close()


f = open("decembre05Moves.txt", "r")
for line in f.readlines():
    line = line.rstrip("\n")
    e = line.split()
    nbr = int(e[1])
    start = int(e[3])
    end = int(e[5])
    print(e)
    print(nbr)
    print(start)
    print(end)
    for i in range(nbr):
        m = tab[start].pop() # Remove last item of start list on the top
        tab[end].append(m) # Add it on the top of the new one

print("Table :")
for k in tab.keys():
    print(f'{k} = {tab[k]}')

print("End of each column :")
txt = ""
result = ""
for k in tab.keys():
    m = tab[k].pop()
    txt += m
    result += m.replace("[", "").replace("]", "")
print(txt)
print(result)

f.close()

