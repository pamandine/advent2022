import ast
import logging
import os

couples = []

debug=False
if debug:
	f = open("inputs/in13Example.txt", "r")
else:
	 f = open("inputs/in13.txt", "r")
if os.path.isfile("log13.log"):
    os.unlink("log13.log")
logging.basicConfig(filename="log13.log", level=logging.DEBUG)

tuples = []
for line in f.readlines():
    line = line.rstrip("\n")
    if (line == ""):
        couples.append(tuples)
        tuples = []
    else:
        tuples.append(line)
f.close()

if (tuples != []):
    couples.append(tuples)

SAME = 0
RIGHT = 1
LEFT = 2

def compare(c1,c2):
    ret = (SAME, "Same")
    m = max(len(c1), len(c2))
    logging.info(f'Max between {c1} and {c2} is {m}')
    for i in range(m):
        try:
        
            try:
                c1[i] = int(c1[i])
            except:
                pass
            try:
                c2[i] = int(c2[i])
            except:
                pass

            if isinstance(c1[i],list) and not isinstance(c2[i], list):
                # c2 is not list, but c1 is list : convert
                c2[i] = [c2[i]]
            if isinstance(c2[i],list) and not isinstance(c1[i], list):
                # c2 is not list, but c1 is list : convert
                c1[i] = [c1[i]]

            if isinstance(c2[i],int) and isinstance(c1[i], int):
                if (c1[i] > c2[i]):
                    ret = RIGHT
                    ret =(RIGHT, "Right side is smaller, so inputs are NOT in the right order")
                    break
                elif (c1[i] < c2[i]):
                    ret = (LEFT,"Left side is smaller, so inputs are in the right order")
                    break

            elif isinstance(c2[i],list) and isinstance(c1[i], list):
                ret = compare (c1[i], c2[i])
                if (ret[0] != SAME):
                    break
        except:
            if (i >= len(c1)):
                # Out of the list 
                ret = (LEFT,"Left side ran out of items, so inputs are in the right order")
                break
            if (i >= len(c2)):
                # Out of the list 
                ret = (RIGHT,"Right side ran out of items, so inputs are NOT in the right order")
                break

    return ret

result = []
pair = 1
for c in couples:
    logging.info("=== New couple ===")
    c1 = ast.literal_eval(c[0])
    c2 = ast.literal_eval(c[1])
    ret = compare(c1,c2)
    logging.info(f'c1={c1}, c2={c2}, ret={ret}\n\n')
    if (ret[0]==LEFT):
        result.append(pair)

    pair += 1

print(f'Sum of right ordered list is : {sum(result,0)}')
