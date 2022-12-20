class monkey():
    items = []
    operation = ""
    divisible = ""
    ifTrue = ""
    ifFalse = ""
    inspections = 0

    def __init__(self, startingItems, operation, test, ifTrue, ifFalse):
        self.items = startingItems
        self.operation = operation.replace("new = ", "").replace("old", "item")
        self.divisible = test
        self.ifTrue = ifTrue
        self.ifFalse = ifFalse



# test
tm0 = monkey([79,98], "new = old * 19", 23, 2, 3)
tm1 = monkey([54, 65, 75, 74], "new = old + 6", 19, 2, 0)
tm2 = monkey([79, 60, 97], "new = old * old", 13, 1, 3)
tm3 = monkey([74], "new = old + 3", 17, 0, 1)

#puzzle
m0 = monkey([73,77], "new = old * 5", 11, 6, 5)
m1 = monkey([57, 88, 80], "new = old + 5", 19, 6, 0)
m2 = monkey([61, 81, 84, 69, 77, 88], "new = old * 19", 5, 3, 1)
m3 = monkey([78, 89, 71, 60, 81, 84, 87, 75], "new = old + 7", 3, 1, 0)
m4 = monkey([60, 76, 90, 63, 86, 87, 89], "new = old + 2", 13, 2, 7)
m5 = monkey([88], "new = old + 1", 17, 4, 7)
m6 = monkey([84, 98, 78, 85], "new = old * old", 7, 5, 4)
m7 = monkey([98, 89, 78, 73, 71], "new = old + 4", 2, 3, 2)

monkeys = [m0, m1, m2, m3, m4, m5, m6, m7]
#monkeys = [tm0, tm1, tm2, tm3]

n = 1
for m in monkeys:
    n *= m.divisible

print(n)


for i in range(10000):
    #print(i)
    for m in monkeys:
        for i in range(len(m.items)):
                item = m.items[0]
                item = int(eval(m.operation) % n)
                if item % m.divisible == 0:
                    monkeys[m.ifTrue].items.append(item)
                else:
                    monkeys[m.ifFalse].items.append(item) 

                
                m.items.pop(0)
                m.inspections+=1
inspections = []
for m in monkeys:
    inspections.append(m.inspections)
inspections.sort()
print(inspections)
print(inspections[-1] * inspections[-2])
