
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



with open("input.txt", "r") as fid:
    data = fid.read()
    data = data.split("\n\n")
    data = [group.split() for group in data]



vertical = 0
horizontal = 0
groupList =[]
for ind, group in enumerate(data):
    # check vertical
    for cInd in range(len(group[0]) - 1):
        currCol = [group[i][cInd] for i in range(len(group))]
        nextCol = [group[i][cInd + 1] for i in range(len(group))]

        if (currCol == nextCol):
            if checkVertRefl(group, cInd):
                vertical += cInd + 1
                groupList.append(ind)


    # check horizontal
    for hInd in range(len(group) - 1):
        currRow = group[hInd]
        nextRow = group[hInd + 1]

        if (currRow == nextRow):
            if checkHorzRefl(group, hInd):
                horizontal += hInd + 1
                groupList.append(ind)



print(horizontal)
print(vertical)

print("Answer:", vertical + 100*horizontal)

print(len(groupList))
print(len(set(groupList)))