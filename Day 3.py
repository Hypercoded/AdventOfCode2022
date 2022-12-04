
def getPriority(character):
    ascii = ord(character)
    if character.isupper():
        return ascii - 64 + 26
    else:
        return ascii - 96
        

def part1():
    sumPriorities = 0
    ruckSack = get_input("Day 3.txt").splitlines()
    for section in ruckSack:
        halfIndex = int(len(section)/2)
        comps = [section[0:halfIndex], section[halfIndex:]]
        for character in comps[0]:
            if character in comps[1]:
                sumPriorities+= getPriority(character)
                break
    print("Sum Priorities:",sumPriorities)

def checkElfGroup(elfGroup):
    for c1 in elfGroup[0]:
        for c2 in elfGroup[1]:
            for c3 in elfGroup[2]:
                if c1 == c2 and c2 == c3:
                    return getPriority(c1)
                
                        
def part2():
    input = get_input("Day 3.txt").splitlines()
    elveGroups = []
    
    i = 0
    while i < (len(input) - 2):
        
        elveGroups.append([input[i], input[i+1], input[i+2]])
        i+=3
    sum = 0


    for elfGroup in elveGroups:
        sum+= checkElfGroup(elfGroup)
                        
                    
    print(sum)
    
    
        
                    
def get_input(fileName):
    with open(f"./Input/{fileName}", "r") as f:
        return f.read()

part2()