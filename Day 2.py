
# get data
def part1():
    
    data = get_input("Day 2.txt")
    puzzle = data.splitlines()

    totalScore = 0

    definitions = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors"
    }

    rps = ["rock", "paper", "scissors"]

    

    for round in puzzle:
        info = round.split(" ")
        them = definitions[info[0]]
        me = definitions[info[1]]

        if (rps.index(them) + 1 ) % 3 == rps.index(me):
            totalScore+= 6
        elif rps.index(them) == rps.index(me):
            totalScore += 3

        totalScore+= (rps.index(me) + 1)
    print(totalScore)
            
        
        
            
def part2():
    
    data = get_input("Day 2.txt")
    puzzle = data.splitlines()

    totalScore = 0

    definitions = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
    }

    rps = ["rock", "paper", "scissors"]

    

    for round in puzzle:
        info = round.split(" ")
        them = definitions[info[0]]
        end = info[1]

        if end == "X": # lose
            totalScore+= 0
            me = (rps.index(them) - 1) % 3
        elif end == "Y": # draw
            totalScore += 3
            me = rps.index(them)
        else: #win
            totalScore += 6
            me = (rps.index(them) + 1) % 3
        totalScore += (me + 1)
        

        
    print(totalScore)
            
        



def get_input(fileName):
    with open(f"./Input/{fileName}", "r") as f:
        return f.read()

part2()