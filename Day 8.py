def get_input(fileName):
    with open(f"./Input/{fileName}", "r") as f:
        return f.read()



def day1():
    data = []
    raw = get_input("Day 8.txt").splitlines()

    for line in raw:
        data.append([0 for i in raw])
    
    
    for y in range(len(raw)):
        threshold = -1
        for x in range(len(raw[y])):
            if int(raw[y][x]) > threshold:
                data[y][x] = 1
                threshold = int(raw[y][x])
        threshold = -1
        for x in reversed(range(len(raw[y]))):
            if int(raw[y][x]) > threshold:
                data[y][x] = 1
                threshold = int(raw[y][x])
    
    for x in range(len(raw[0])):
        threshold = -1

        for y in range(len(raw)):
            if int(raw[y][x]) > threshold:
                data[y][x] = 1
                threshold = int(raw[y][x])
        threshold = -1
        for y in reversed(range(len(raw))):
            if int(raw[y][x]) > threshold:
                data[y][x] = 1
                threshold = int(raw[y][x])
    


    

    print(data)
    total = 0
    for i in data:
        for j in i:
            total += j
    print(total)

def day2():
    data = []
    raw = get_input("Day 8.txt").splitlines()

    for line in raw:
        data.append([1 for i in raw])
    
    
    for y in range(len(raw)):
        threshold = 0
        count = 0
        for x in range(len(raw[y])):

            if int(raw[y][x]) > threshold:
                count+=1
                data[y][x] *= count
                
            if int(raw[y][x]) <= threshold:
                count = 0
                threshold = int(raw[y][x])
                
            count+=1
        threshold = -1
        for x in reversed(range(len(raw[y]))):
            if int(raw[y][x]) > threshold:
                data[y][x] = 1
                threshold = int(raw[y][x])
    
    for x in range(len(raw[0])):
        threshold = -1

        for y in range(len(raw)):
            if int(raw[y][x]) > threshold:
                data[y][x] = 1
                threshold = int(raw[y][x])
        threshold = -1
        for y in reversed(range(len(raw))):
            if int(raw[y][x]) > threshold:
                data[y][x] = 1
                threshold = int(raw[y][x])
    


    

    print(data)
    total = 0
    for i in data:
        for j in i:
            total += j
    print(total)
day2()