f = open("decembre03.txt", "r")

def ASCIItoInt (letter):
    # Minuscule letters are from 1 to 26
    # Majuscule letters are from 27 to 52
    # a = 97
    # A = 65
    ret = 0
    if (letter.islower()):
        ret = (ord(letter)- 96)
    else:
        ret = (ord(letter)- 38)

    print(f'Letter={letter}, isLower={letter.islower()}, ord={ord(letter)}')
    return ret

sum = 0
group = 0
groups = []
for line in f.readlines():
    # Get the 3 lines per group
    line = line.rstrip("\n")
    elements = list(line)
    groups.append(elements)
    group = group + 1 # reached 3 lines
    if (group == 3):
        print(groups)
        group = 0
        letter = set(groups[0]).intersection(groups[1], groups[2])
        letter = list(letter)
        # There is one identical letter in both list, no more
        points = ASCIItoInt(letter[0])
        sum = sum + points
        groups = []
        print (f'List={line}, Common letter={letter[0]}, points={points}, sum={sum}')

f.close()
