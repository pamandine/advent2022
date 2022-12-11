debug = False
PART2 = True
ch = 4
if (PART2):
    ch = 14
if debug:
    f = open("decembre06Example.txt", "r")
else:   
    f = open("decembre06.txt", "r")

for line in f.readlines():
    line = line.rstrip("\n")
    print(line)
    # Isolate every for char until find on without duplicated letter
    for j in range(len(line)):
        c = line[j:j+ch]
        found = False
        for character in c:
            if c.count(character) > 1:
                found = True 
                break
        if (not found):
            # Did not found a single double 
            print (f'Start word = {c}')
            index = line.find(c)
            print(index+ch)
            break
    print("\n")

f.close()
