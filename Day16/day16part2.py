
import copy
import sys

history = set()
def move(row, col, heading):
    # pos = (row, col, heading)
    # up = 0
    # right = 1
    # down = 2
    # left = 3
    pos = (row, col, heading)
    if pos in history:
        return
    else:
        history.add(pos)  # the coords and heading describe a singular path

    if debug:
        print(pos)
        visMap()

    match heading:
        case 1:
            nextCoord = (row, col + 1)
        case 3:
            nextCoord = (row, col - 1)
        case 0:
            nextCoord = (row - 1, col)
        case 2:
            nextCoord = (row + 1, col)
        case _:
            assert False

    nextRow, nextCol = nextCoord

    if nextRow < 0 or nextRow >= len(data[0]):
        return
    if nextCol < 0 or nextCol >= len(data):
        return
    
    nextBlock = data[nextRow][nextCol]

    match nextBlock, heading:
        case '.', _:
            move(nextRow, nextCol, heading)
        
        case ('/', 0 | 2) | ('\\', 1 | 3):
            heading = (heading + 1) % 4
            move(nextRow, nextCol, heading)
        case ('/', 1 | 3) | ('\\', 0 | 2):
            heading = (heading - 1) % 4
            move(nextRow, nextCol, heading)
        
        case ('|', 1 | 3) | ('-', 0 | 2):
            h1 = (heading + 1) % 4
            h2 = (heading - 1) % 4
            move(nextRow, nextCol, h1)
            move(nextRow, nextCol, h2)
        case ('|', 0 | 2) | ('-', 1 | 3):
            move(nextRow, nextCol, heading)
        
    return



def getAns():
    # find unique coords in history
    coords = [(row, col) for (row, col, _) in history]
    uniqueCoords = set(coords)
    numUniqueCoords = len(uniqueCoords) - 1
    return numUniqueCoords



def printMap(map):
    # list of strings
    for line in map:
        print(line)
    print()



def visMap():
    coords = [(row, col) for (row, col, _) in history]
    uniqueCoords = set(coords)

    vis = copy.deepcopy(data)
    vis = [list(line) for line in vis]
    for coord in uniqueCoords:
        vis[coord[0]][coord[1]] = '#'

    vis = ["".join(line) for line in vis]
    printMap(vis)



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


with open("input.txt", "r") as fid:
    data = fid.readlines()

data = [line.strip() for line in data]


debug = False
sys.setrecursionlimit(5000)  # should have added coordinates to queue instead of recursive calls


maxTiles = 0
for rowInd in range(len(data)):
    move(rowInd, -1, 1)
    ans = getAns()
    history.clear()

    maxTiles = max(maxTiles, ans)

    move(rowInd, len(data[0]), 3)
    ans = getAns()
    history.clear()

    maxTiles = max(maxTiles, ans)


for colInd in range(len(data[0])):
    move(-1, colInd, 2)
    ans = getAns()
    history.clear()

    maxTiles = max(maxTiles, ans)

    move(len(data), colInd, 0)
    ans = getAns()
    history.clear()

    maxTiles = max(maxTiles, ans)




print("Answer:", maxTiles)