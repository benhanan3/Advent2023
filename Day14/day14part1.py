

def printData(data):
    for rowInd, row in enumerate(data):
        for colInd, char in enumerate(data[rowInd]):
            print(char, end ="")
        print()

def tiltNorth(data):
    boundary = ["#"] * len(data[0])
    boundary = "".join(boundary)
    data.insert(0, boundary)
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


def totalLoad(data):
    total = 0
    length = len(data)
    for rowInd, row in enumerate(data):
        for colInd, char in enumerate(data[rowInd]):
            if char == "#" or char == ".":
                continue
            elif char == 'O':
                total += length - rowInd
    return total


with open("input.txt", "r") as fid:
    data = fid.readlines()

data = [list(line.strip()) for line in data]


printData(data)
print()

data = tiltNorth(data)

printData(data)

ans = totalLoad(data)

print("Answer:", ans)