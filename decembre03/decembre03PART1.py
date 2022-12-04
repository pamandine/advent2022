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
for line in f.readlines():
    # We have to split the line per 2 with exact same size
    line = line.rstrip("\n")
    elements = list(line)
    middle = int(len(elements)/2)
    first = elements[:middle]
    second = elements[middle:]
    letter = set(first).intersection(second)
    letter = list(letter)
    # There is one identical letter in both list, no more
    points = ASCIItoInt(letter[0])
    sum = sum + points
    print (f'List={line}, Common letter={letter[0]}, points={points}, sum={sum}')

f.close()
