f = open("decembre04.txt", "r")

def checkInclude(s1,s2):
    e1 = s1.split("-")
    e2 = s2.split("-")
    b1min = int(e1[0])
    b1max = int(e1[1])
    b2min = int(e2[0])
    b2max = int(e2[1])
    #e1 in e2?

    print(f'bornes 1 = {b1min}-{b1max}, bornes 2 = {b2min}-{b2max}')

    if (b1min >= b2min and b1max <= b2max):
        return True
    
    #e2 in e1?
    if (b2min >= b1min and b2max <= b1max):
        return True



pairs = 0
for line in f.readlines():
    # Build the complete string. If we have 1-3, transform to 123
    line = line.rstrip("\n")
    elements = line.split(",")
   
    if (checkInclude(elements[0], elements[1])):
        pairs = pairs + 1

print(pairs)
f.close()
