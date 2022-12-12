import os
path = os.path.dirname(os.path.abspath(__file__))
file = path+"/../inputs/in01.txt"

resume = {}
sum = 0
current = 0

f = open(file, "r")
for line in f.readlines():
    line = line.rstrip("\n")
    if (line == ""): # New one
        resume[current] = sum

        sum = 0
        current = current+1
    else:    
        sum = sum + int(line);
f.close()

# Sort by value in increasing order
sorted = {k: v for k, v in sorted(resume.items(), key=lambda item: item[1])}

# Get the 3 big, and add them
sorted_keys = list(sorted)
sum = 0
for i in [-1,-2,-3]:
    sum = sum + sorted[sorted_keys[i]]

biggerOfAll = sorted[sorted_keys[-1]]
print (f'[PART1] Sum of 1 bigger = {biggerOfAll}')
print (f'[PART2] Sum of 3 bigger = {sum}')
