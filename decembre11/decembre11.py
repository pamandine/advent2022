import math
import re

debug=False
if debug:
	f = open("inputs/in11Example.txt", "r")
else:
	 f = open("inputs/in11.txt", "r")

class monkey():
    def __init__(self):
        self.items = []
        self.operation = None
        self.test = None
        self.monkeyOnTrue = None
        self.monkeyOnFalse = None
        self.inspect = 0
    def setItem(self,item):
        self.items.append(item)
    def setOperation(self,operation):
        self.operation = operation # old*5, old+78, old*old
        print(f'Operation = {operation}')
    def setTest(self,test):
        self.test = test
        print(f'Test : {test}')
    def setOnTrue(self,onTrue):
        self.monkeyOnTrue = onTrue
        print(f'Monkey on true : {onTrue}')
    def setOnFalse(self,onFalse):
        self.monkeyOnFalse = onFalse
        print(f'Monkey on false : {onFalse}')
    def dealWithItems(self):
        tuples = []
        while self.items!=[]:
            self.inspect += 1
            i = self.items.pop(0)
            operation = self.operation
            operation = operation.replace("old", str(i))

            i = eval(operation) # execute operation
            i = math.floor(i/3)
            # Now, test divisble per x
            if ((i%self.test)!=0):
                # False condition
                tuples.append((self.monkeyOnFalse,i))
            else:
                # True condition
                tuples.append((self.monkeyOnTrue,i))
        return tuples

def getLine(f):
    line = f.readline()
    line = line.rstrip("\n")
    print(line)
    return line

monkeys = []

line = getLine(f)
while line:
    if (line[:6] == "Monkey"):
        m = monkey()
        line = getLine(f) # Starting items
        match = re.findall(r'starting items: ([\w\s,]+)', line, re.I)
        if (match != []): # There is at least one item
            items = match[0].split(",")
            for i in items:
                i = int(i)
                m.setItem(i)

        line = getLine(f) # Operation
        match = re.findall(r'operation: new = ([\w\d\s\*\+\-\/]+)', line, re.I)
        m.setOperation(match[0])

        line = getLine(f) # Test
        match = re.findall(r'test: divisible by (\d+)', line, re.I)
        i = int(match[0])
        m.setTest(i)

        line = getLine(f) # True monkey
        match = re.findall(r'if (\w+): throw to monkey (\d+)', line, re.I)
        if (match[0][0] == "true"):
            m.setOnTrue(int(match[0][1]))
        elif (match[0][0] == "false"):
            m.setOnFalse(int(match[0][1]))

        line = getLine(f) # False monkey
        match = re.findall(r'if (\w+): throw to monkey (\d+)', line, re.I)
        if (match[0][0] == "true"):
            m.setOnTrue(int(match[0][1]))
        elif (match[0][0] == "false"):
            m.setOnFalse(int(match[0][1]))
        
        monkeys.append(m)

    line = getLine(f) # Blank line
    line = getLine(f) # New Monkey

f.close()

print(f'There are {len(monkeys)} monkeys')

for i in range(20):
    print(f'Iteration {i}')
    for m in monkeys:
        print(f'Monkey items = {m.items}, operation = {m.operation}, test = {m.test}, onTrue = {m.monkeyOnTrue}, onFalse = {m.monkeyOnFalse}')
        tuples = m.dealWithItems()
        print(f'Operations result : {tuples}')
        for e in tuples:
            (goto,item) = e
            monkeys[goto].setItem(item)

inspected = []
for i in range(len(monkeys)):
    m = monkeys[i]
    print(f'Monkey {i} inspected items {m.inspect} times')
    inspected.append(m.inspect)

inspected.sort()
business = inspected[-1]*inspected[-2]
print(f'Business = {business}')



