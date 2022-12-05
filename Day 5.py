

def main(part):
    instr = ""
    if part is None:
        instr = "part1"
    else:
        instr = part
    lines = get_input("Day 5.txt").splitlines()
    stacks = {}
    stackInput = []
    instructions = []
    for line in lines:
        parse = "stacks"
        if "[" not in line:
            parse = "instructions"
        if parse == "stacks":
            stackInput.append(line)
        else:
            
            instructions.append(line)
    instructions = instructions[2:]


    for line in stackInput:
        i = 0
        row = []
        while i < len(line)-2:
            
            row.append(line[i:i+4])

            i+=4
        for i in range(len(row)):
            row[i] = row[i].replace(" ","").replace("[","").replace("]","")
            if not i in stacks:
                stacks[i] = []
                
            
            stacks[i] = stacks[i] + [{row[i]}] if row[i] != '' else stacks[i]
    

    if instr == "part1":
        for instruction in instructions:
            values = instruction.replace("move ", "").replace("from ", "").replace("to ", "")
            values = values.split(" ")
            values = [int(x) for x in values]

            for i in range(values[0]):
                stacks[values[2]-1].insert(0, stacks[values[1] -1 ].pop(0))
    else:
        for instruction in instructions:
            values = instruction.replace("move ", "").replace("from ", "").replace("to ", "")
            values = values.split(" ")
            values = [int(x) for x in values]


            amnt = values[0]
            origin = values[1] - 1
            dest = values[2] - 1

            
            stacks[dest] = stacks[origin][0:amnt] + stacks[dest]
            stacks[origin] = stacks[origin][amnt:]
    
   
    for k, v in stacks.items():
        try:
            print(str(v[0]).strip("{}''"), end="")
        except:
            pass
    print()


def get_input(fileName):
    with open(f"./Input/{fileName}", "r") as f:
        return f.read()



print("Part 1")
main(None)
print("Part 2")
main("part2")