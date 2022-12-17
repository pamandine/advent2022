import math
import re
import sys

sys.set_int_max_str_digits(9999999)
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
    def setTest(self,test):
        self.test = test
    def setOnTrue(self,onTrue):
        self.monkeyOnTrue = onTrue
    def setOnFalse(self,onFalse):
        self.monkeyOnFalse = onFalse
    def dealWithItems(self, part):
        tuples = []
        while self.items!=[]:
            self.inspect += 1
            i = self.items.pop(0)
            operation = self.operation
            operation = operation.replace("old", str(i))

            i = eval(operation) # execute operation
            if (part == 1):
                i = math.floor(i/3)
            # Now, test divisble per x
            if ((i%self.test)!=0):
                # False condition
                tuples.append((self.monkeyOnFalse,i))
            else:
                # True condition
                tuples.append((self.monkeyOnTrue,i))
        return tuples
    def getAndClearInspect(self):
        temp = self.inspect
        self.inspect = 0
        return temp

def getLine(f):
    line = f.readline()
    line = line.rstrip("\n")
    return line
        
def func(part, max):
    debug=True
    if debug:
        f = open("inputs/in11Example.txt", "r")
    else:
         f = open("inputs/in11.txt", "r")


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

    monkeyInspection = {}
    for i in range(len(monkeys)):
        monkeyInspection[i] = []

    for i in range(max):
        for m in monkeys:
            tuples = m.dealWithItems(part)
            print(tuples)
            for e in tuples:
                (goto,item) = e
                monkeys[goto].setItem(item)

        if i in [0,19,29,39,49,59,69,79,89,99,999, 1999,2999,3999,4999,5999,6999,7999,8999,9999]:
            print(f'== After round {i+1} ==')
            for m in range(len(monkeys)):
                print(f'Monkey {m} inspected items {monkeys[m].inspect}')
                monkeyInspection[m].append(monkeys[m].getAndClearInspect())

    inspected = []
    for i in range(len(monkeys)):
        sumInspect = sum(monkeyInspection[i],0)
        print(f'Monkey {i} inspected items {sumInspect} times')
        inspected.append(sumInspect)

    inspected.sort()
    business = inspected[-1]*inspected[-2]
    print(f'Business = {business}')


print("Call function 1")
func(1,20)

print("Call function 2")
# TODO 
#func(2,10000)

