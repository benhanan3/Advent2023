import re


def checkCoords(row, col, data):
    if (row < 0 or col < 0):
        return False
    if (row >= len(data) or col >= len(data[0])):
        return False
    
    if re.match(r"\d", data[row][col]):
        return True


with open("input.txt", "r") as fid:
    data = fid.readlines()

data = [list(line.strip()) for line in data]

# for l in data:
#     print(l)

sumNum = 0
sumSet = set()
for row, line in enumerate(data):
    
    for col, char in enumerate(line):
        if re.match(r"[^\w.]", char):
            print(char)

            for rowAdj in [-1, 0 , 1]:
                for colAdj in [-1, 0 ,1]:
                    # ensures the indices are in bounds. returns True if a digit is found
                    if checkCoords(row + rowAdj, col + colAdj, data):
                        # search the row where the digit is found to assemble the full digit
                        minCol = col + colAdj
                        while( (minCol >= 0) and re.match(r"\d", data[row + rowAdj][minCol]) ):
                            minCol -= 1

                        maxCol = col + colAdj
                        while( (maxCol < len(data[0])) and re.match(r"\d", data[row + rowAdj][maxCol]) ):
                            maxCol += 1

                        # concatenate digits from [minCol + 1, maxCol - 1], inclusive
                        number = ''
                        for colInd in range(minCol + 1, maxCol):
                            number += data[row + rowAdj][colInd]

                        number = int(number)
                        print(number)
                        sumSet.add(number)
            
            # only count a given part number once per symbol. Can be counted multiple times overall
            sumNum += sum(sumSet)
            sumSet = set()

print(sumNum)