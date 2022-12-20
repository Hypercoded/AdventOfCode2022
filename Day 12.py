from math import sqrt
import os
import time
from colr import color

def get_input(fileName):
    with open(f"./Input/{fileName}", "r") as f:
        return f.read()

class Node:
    x = 0
    y = 0
    dist = None
    height = None
    checked = False
    pointingTo = None
    

    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height

class Heightmap:
    data = []
    
    root = None
    end = None
    
    startx, starty = None, None
    endx, endy = None, None

    width, height = None, None


    def __init__(self, map):
        lines = map.splitlines()
        
        for y in range(len(lines)):
            self.data.append([])
            for x in range(len(lines[y])):
                elevation = lines[y][x]
                if elevation == 'S':
                    elevation = 'a'
                    self.startx = x
                    self.starty = y
                if elevation == 'E':
                    elevation = 'z'
                    self.endx = x
                    self.endy = y
                self.data[y].append(Node(x, y, elevation))

        self.root = self.data[self.starty][self.startx]
        self.end = self.data[self.endy][self.endx]
        self.height = len(self.data)
        self.width = len(self.data[0])

    def canStep(self, node, deltax, deltay):
        nodex = node.x
        nodey = node.y
        sumx = nodex + deltax
        sumy = nodey+deltay
        if (sumx >= 0 and sumx < self.width) :
            if (sumy >= 0 and sumy < self.height):
                checked = self.data[sumy][sumx].checked
                canjump = ord(self.data[sumy][sumx].height) - ord(self.data[nodey][nodex].height) <= 1
                if checked == False and canjump:
                    return True

        return False

        
    



            

def main():
    data = get_input("Day 12.txt")
    world = Heightmap(data)
    world.root.dist = 0

    open = []
    open.append(world.root) 
    

    while len(open) != 0:
        grid = world.data
        cur = open[0]

        x = cur.x
        y = cur.y
        
        



        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if world.canStep(cur, dx, dy):
                temp = grid[y + dy][x + dx]
                temp.dist = cur.dist + 1
                temp.prev = cur
                add = True
                for i in open:
                    if i.x == x+dx and i.y == y+dy:
                        add = False 
                        break
                if add:
                    open.append(temp)
        #print("\n\n")
        #os.system('cls' if os.name == 'nt' else 'clear')

        #for iy in range(len(grid)):
        #    for ix in range(len(grid[y])):
        #        print(grid[iy][ix].height if (iy, ix) != (y, x) else "■", end="")
        #    print("")
        #    
        #time.sleep(0.1)
        
        
        grid[y][x].checked = True
        open.pop(0)

    
    
    t = world.end
    n = 0
    path = []
    while True:
        
        try:
            path.append(t)
            t = t.prev
        except:
            break
        n += 1

    RESET = '\033[0m'
    def get_color_escape(r, g, b, background=False):
        return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

    for iy in range(len(grid)):
            for ix in range(len(grid[y])):
                height = grid[iy][ix].height
                col = (ord(height) - 97) * 7 + 80
                if height == 'a':
                    colors = (0, 50, 230)
                else:
                    colors = (0, col, 70)
                if grid[iy][ix] in path:
                    colors = (150, 100, 100)
                print( color(height , fore=colors), end="")
                #time.sleep(0.1)
            print("")
    
    
    print(get_color_escape(255, 128, 0) 
      + get_color_escape(80, 30, 60, True)
      + 'Fancy colors!' 
      + RESET)
            

main()
