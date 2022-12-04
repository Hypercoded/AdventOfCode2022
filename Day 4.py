def get_input(fileName):
    with open(f"./Input/{fileName}", "r") as f:
        return f.read()

def part1():
    lines = get_input("Day 4.txt").splitlines()
    pairs = []
    sum = 0
    for line in lines:
        pairs.append(line.split(","))
    for pair in pairs:
        elf1 = pair[0].split('-')
        elf2 = pair[1].split('-')
        elf1 = [int(x) for x in elf1]
        elf2 = [int(x) for x in elf2]
        
        print(elf1)
        print(elf2)
        
        if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
            sum+= 1
            print("case 1")
        elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
            sum+=1
            print("case 2")

        print(" -- ")

        
    print(sum)

def part2():
    lines = get_input("Day 4.txt").splitlines()
    pairs = []
    sum = 0
    for line in lines:
        pairs.append(line.split(","))
    for pair in pairs:
        elf1 = pair[0].split('-')
        elf2 = pair[1].split('-')
        elf1 = [int(x) for x in elf1]
        elf2 = [int(x) for x in elf2]
        
        print(elf1)
        print(elf2)
        
        if elf1[0] <= elf2[1] and elf1[1] >= elf2[1]:
            sum+= 1
            print("case 1")
        elif elf2[0] <= elf1[1] and elf2[1] >= elf1[1]:
            sum+=1
            print("case 2")

        print(" -- ")

        
    print(sum)

part1()
part2()