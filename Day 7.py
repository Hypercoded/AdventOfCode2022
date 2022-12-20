
def get_input(fileName):
    with open(f"./Input/{fileName}", "r") as f:
        return f.read()

class node:
    value = ""
    children = []
    parent = ""
    fileType = ""
    name = ""
    def __init__(self, parent, fileType, name, value, children):
        self.parent = parent
        self.fileType = fileType
        self.name = name
        self.value = int(value)
        self.children = children



root = node(None, "root", "root", 0, [])
lines = get_input("Day 7.txt").splitlines()


cur = root
for line in lines:
    tokens = line.split(" ")
    if tokens[0] == "$" and tokens[1] == "cd":
        if tokens[2] == "..":
            cur = cur.parent
        else:
            if tokens[2] not in cur.children:
                new = node(cur, "dir", tokens[2], 0, [])
                cur.children.append(new)
            else:
                new = None
                for child in cur.children:
                    if child.name == tokens[2]:
                        new = child
            
            cur = new

        
    elif tokens[0].isdigit():
        new = node(cur, "file", tokens[1], tokens[0], [])
        cur.children.append(new)


        

def printDir(node, indentLevel):

    print("   " * indentLevel, "-", node.name)
    for child in node.children:
        if child.fileType == "dir":
            printDir(child, indentLevel+1)
        else:
            print("   " * (indentLevel+1), child.value, child.name)

#printDir(root, 0)

smallDirs = {}
allDirs = {}
def sumDirs(node):

    sum = 0
    for child in node.children:
        if child.fileType == "dir":
            n = sumDirs(child)
            sum+= n
            print(f"Sum of {child.name} = {n}")
        else:
            sum+= child.value
    if sum < 100000:
        smallDirs[node] = sum
    node.value = sum
    if node.fileType == "dir":
        allDirs[node] = sum

    return sum


#print(printDir(root, 0))
rootSize = sumDirs(root.children[0])
#print(len(smallDirs))
##p1
print(sum(smallDirs.values()))

lowest = root.children[0]
totalsize = root.children[0].value
for dir in allDirs:
    print(lowest.value)
    if dir.value < lowest.value:
        lowest = dir if (70000000 - totalsize + dir.value)>= 30000000 else lowest

print(lowest.name)


#printDir(root.children[0], 0)







