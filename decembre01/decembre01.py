resume = {}
sum = 0
max = 0
current = 0

f = open("decembre01.txt", "r")
for line in f.readlines():
    line = line.rstrip("\n")
    if (line == ""): # New one
        resume[current] = sum
        if (sum > max):
            max = sum

        sum = 0
        current = current+1
    else:    
        sum = sum + int(line);

# Sort by value in increasing order
sorted = {k: v for k, v in sorted(resume.items(), key=lambda item: item[1])}

# Get the 3 big, and add them
sorted_keys = list(sorted)
print(sorted_keys)

size = len(sorted_keys)-1
sum = 0
for i in range(size,size-3,-1):
    print(sorted_keys[i])
    print(sorted[sorted_keys[i]])
    sum = sum + sorted[sorted_keys[i]]

print (f'Sum of 3 bigger = {sum}')
f.close()
