import copy

def tiltNorth(data):
    for rowInd, row in enumerate(data):
        for colInd, char in enumerate(data[rowInd]):
            if char == "#" or char == ".":
                continue
            elif char == "O":
                swapRowInd = rowInd
                while ( data[swapRowInd - 1][colInd] == "."):
                    swapRowInd -= 1

                data[rowInd][colInd] = '.'
                data[swapRowInd][colInd] = 'O'
    return data


def tiltSouth(data):
    data.reverse()
    for rowInd, row in enumerate(data):
        for colInd, char in enumerate(data[rowInd]):
            if char == "#" or char == ".":
                continue
            elif char == "O":
                swapRowInd = rowInd
                while ( data[swapRowInd - 1][colInd] == "."):
                    swapRowInd -= 1

                data[rowInd][colInd] = '.'
                data[swapRowInd][colInd] = 'O'
    data.reverse()
    return data


def tiltWest(data):
    for rowInd, row in enumerate(data):
        for colInd, char in enumerate(data[rowInd]):
            if char == "#" or char == ".":
                continue
            elif char == "O":
                swapColInd = colInd
                while ( data[rowInd][swapColInd - 1] == "."):
                    swapColInd -= 1

                data[rowInd][colInd] = '.'
                data[rowInd][swapColInd] = 'O'
    return data


def tiltEast(data):
    for rowInd, row in enumerate(data):
        colOrder = list(enumerate(data[rowInd]))
        colOrder.reverse()
        for colInd, char in colOrder:
            if char == "#" or char == ".":
                continue
            elif char == "O":
                swapColInd = colInd
                while ( data[rowInd][swapColInd + 1] == "."):
                    swapColInd += 1

                data[rowInd][colInd] = '.'
                data[rowInd][swapColInd] = 'O'
    return data


def cycle(data):
    newData = copy.deepcopy(data)
    newData = tiltNorth(newData)
    newData = tiltWest(newData)
    newData = tiltSouth(newData)
    newData = tiltEast(newData)
    return newData


def totalLoad(data):
    tallyData = copy.deepcopy(data)
    del tallyData[0], tallyData[-1]  # delete the boundary lines
    total = 0
    length = len(tallyData)
    for rowInd, row in enumerate(tallyData):
        for colInd, char in enumerate(tallyData[rowInd]):
            if char == "#" or char == ".":
                continue
            elif char == 'O':
                total += length - rowInd
    return total


def printData(data):
    for rowInd, row in enumerate(data):
        for colInd, char in enumerate(data[rowInd]):
            print(char, end ="")
        print()


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


with open("input.txt", "r") as fid:
    data = fid.readlines()

data = [list(line.strip()) for line in data]


# add '#' as boundary lines
for rowInd, row in enumerate(data):
    row.insert(0, '#')
    row.insert(len(data[0]), '#')

boundary = ["#"] * len(data[0])
data.insert(0, boundary)
data.insert(len(data), boundary)

printData(data)
print()


# keep a set of dictionaries to associate the iteration and the current data
cacheData = {}  # key = data, value = epoch
cacheEpoch = {}  # key = epoch, value = data
for epoch in range(1000000000):
    dataHash = tuple([ tuple(list) for list in data ])  # create hashable format for dictionary lookups
    # if this data has already been seen, we have just completed one iteration of a loop
    if dataHash in cacheData:
        print("Epoch {} is repeated at epoch {}".format(epoch+1, cacheData[dataHash] + 1))
        break

    else:
        nextData = cycle(data)

    # store the data, iteration
    cacheData[dataHash] = epoch
    cacheEpoch[epoch] = data

    # reassign data and keep moving
    data = nextData


# number of iterations that comprise the loop
loopLength = epoch - cacheData[dataHash]
print("loop", loopLength)

# the iteration that is identical to the data at 1000000000 iterations
finalIter = ((1000000000 - cacheData[dataHash] ) % loopLength) + cacheData[dataHash]
print("final", finalIter)

# gets the data map from the dictionary, calculates the final load value
finalData = cacheEpoch[finalIter]
print("ans", totalLoad(finalData))



    


