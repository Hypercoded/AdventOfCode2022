def get_input(fileName):
    with open(f"./Input/{fileName}", "r") as f:
        return f.read()




headx, heady = 0, 0
tailx, taily = 0, 0

arr = []

for line in get_input('Day 9.txt').splitlines():
    instruction = line.split(' ')
    direction = instruction[0]
    steps = int(instruction[1])

    for i in range(steps):
        if direction == 'L':
            headx -= 1
        if direction == 'R':
            headx += 1
        if direction == 'D':
            heady -= 1
        if direction == 'U':
            heady += 1
        

        if abs(headx - tailx) >= 2 and heady == taily:
            sign = (headx - tailx) / abs(headx - tailx)
            print(headx, heady)
            print(tailx, taily)
            print(sign)
            tailx+= sign
        if abs(heady - taily) >= 2 and headx == tailx:
            
            sign = (heady - taily) / abs(heady - taily)
            taily+= sign 
        if headx != tailx and heady!= taily:
            sign1 = (headx - tailx) / abs(headx - tailx)
            sign2 = (heady - taily) / abs(heady - taily)
            
            tailx+= sign
            taily+= sign
        arr.append((tailx, taily))
print(len(set(arr)))