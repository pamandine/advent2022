import os
path = os.path.dirname(os.path.abspath(__file__))
file = path+"/../inputs/in04.txt"

def checkInclude(s1,s2,func):
    e1 = s1.split("-")
    e2 = s2.split("-")
    b1min = int(e1[0])
    b1max = int(e1[1])
    b2min = int(e2[0])
    b2max = int(e2[1])

    if (func==2):
        if (b1min >= b2min and b1min <= b2max):
            return True
        
        if (b1max >= b2min and b1max <= b2max):
            return True

        #e2 in e1?
        if (b2min >= b1min and b2min <= b1max):
            return True

        if (b2max >= b1min and b2max <= b1max):
            return True
    else:

        #e1 in e2?
        if (b1min >= b2min and b1max <= b2max):
            return True
        
        #e2 in e1?
        if (b2min >= b1min and b2max <= b1max):
            return True

def func(lines,part):
    pairs = 0
    for line in lines:
        # Build the complete string. If we have 1-3, transform to 123
        line = line.rstrip("\n")
        elements = line.split(",")
       
        if (checkInclude(elements[0], elements[1], part)):
            pairs = pairs + 1

    print(pairs)



f = open(file, "r")
lines = f.readlines()
print('Call function 1')
func(lines,1)
print('Call function 2')
func(lines,2)
f.close()
