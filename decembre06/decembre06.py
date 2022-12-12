import os
path = os.path.dirname(os.path.abspath(__file__))
file = path+"/../inputs/in06.txt"

def func(lines, nbr_char):
    for line in lines:
        line = line.rstrip("\n")
        # Isolate every for char until find on without duplicated letter
        for j in range(len(line)):
            c = line[j:j+nbr_char]
            found = False
            for character in c:
                if c.count(character) > 1:
                    found = True 
                    break
            if (not found):
                # Did not found a single double 
                print (f'Start word = {c}')
                index = line.find(c)
                print(index+nbr_char)
                break


f = open(file, "r")
lines = f.readlines()
print("Call function 1")
func(lines,4)
print("Call function 2")
func(lines,14)
f.close()
