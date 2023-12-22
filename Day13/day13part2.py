
def checkHorzRefl(group, ind1):
    # ind1 is the topmost index of the reflection line
    ind2 = ind1 + 1
    maxLength = min(len(group) - ind2 - 1, ind1)

    top = group[ind1 - maxLength: ind1 + 1]
    bottom = group[ind2: ind2 + maxLength + 1]
    bottom.reverse()

    if top == bottom:
        return True
    else:
        return False
    

def checkVertRefl(group, ind1):
    # ind1 is the topmost index of the reflection line
    ind2 = ind1 + 1
    maxLength = min(len(group[0]) - ind2 - 1, ind1)

    left = [ [group[row][col] for row in range(len(group))] for col in range(ind1 - maxLength, ind1 + 1) ]
    right = [ [group[row][col] for row in range(len(group))] for col in range(ind2, ind2 + maxLength + 1) ]
    right.reverse()

    if left == right:
        return True
    else:
        return False


def checkGroup(group, origType, origInd):
    for rowInd in range(len(group)):
        for colInd, char in enumerate(group[rowInd]):
            singleVert = 0
            singleHorz = 0

            testGroup = group.copy()

            if char == '.':
                row = list(testGroup[rowInd])
                row[colInd] = '#'
                row = "".join(row)
                testGroup[rowInd] = row
            else:
                row = list(testGroup[rowInd])
                row[colInd] = '.'
                row = "".join(row)
                testGroup[rowInd] = row
    
            # check vertical
            for cInd in range(len(testGroup[0]) - 1):
                if (origType == "vert") and (origInd == cInd):
                    continue
                currCol = [testGroup[i][cInd] for i in range(len(testGroup))]
                nextCol = [testGroup[i][cInd + 1] for i in range(len(testGroup))]

                if (currCol == nextCol):
                    if checkVertRefl(testGroup, cInd):
                        singleVert = cInd + 1

            # check horizontal
            for hInd in range(len(testGroup) - 1):
                if (origType == "horz") and (origInd == hInd):
                    continue
                currRow = testGroup[hInd]
                nextRow = testGroup[hInd + 1]

                if (currRow == nextRow):
                    if checkHorzRefl(testGroup, hInd):
                        singleHorz = hInd + 1
            
            if singleHorz or singleVert:
                return singleHorz, singleVert
    
    print("No other line found")
    assert False


def intitalRefl(group):
    vertical = 0
    horizontal = 0
    # check vertical
    for cInd in range(len(group[0]) - 1):
        currCol = [group[i][cInd] for i in range(len(group))]
        nextCol = [group[i][cInd + 1] for i in range(len(group))]

        if (currCol == nextCol):
            if checkVertRefl(group, cInd):
                vertical = cInd + 1
                break

    # check horizontal
    for hInd in range(len(group) - 1):
        currRow = group[hInd]
        nextRow = group[hInd + 1]

        if (currRow == nextRow):
            if checkHorzRefl(group, hInd):
                horizontal = hInd + 1
                break
    
    if vertical:
        return "vert", cInd
    elif horizontal:
        return "horz", hInd


with open("input.txt", "r") as fid:
    data = fid.read()
    data = data.split("\n\n")
    data = [group.split() for group in data]


vertical = 0
horizontal = 0

for group in data:
    reflType, ind = intitalRefl(group)
    singleHorz, singleVert = checkGroup(group, reflType, ind)
    vertical += singleVert
    horizontal += singleHorz
                



print(horizontal)
print(vertical)

print("Answer:", vertical + 100*horizontal)