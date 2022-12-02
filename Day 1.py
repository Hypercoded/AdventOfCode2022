
# get data
def main():
    
    data = get_input("Day 1.txt")
    lines = data.splitlines()
    
    
    currentElf = []
    elves = []
    for line in lines:
        if line != '':
            currentElf.append(int(line))
        else:
            elves.append(sum(currentElf))
            currentElf = []
    elves.sort()

    print("Part 1:", elves[-1])
    print("Part 2:", sum(elves[-3:]))
    

def get_input(fileName):
    with open(f"./Input/{fileName}", "r") as f:
        return f.read()

main()