import re


def hash(string):
    currVal = 0
    for char in string:
        currVal += ord(char)
        currVal *= 17
        currVal %= 256
    return currVal



with open("input.txt", "r") as fid:
    data = fid.read()

data = data.strip().split(",")
boxes = {i:{} for i in range(256)}  # list of { boxNum : { label: lens, label2: lens2 } }


for segment in data:
    labelMatch = re.match(r'\w+', segment)
    
    label = labelMatch.group()
    endInd = labelMatch.span()[1]
    operation = list(segment)[endInd]

    if len(segment) > endInd:
        lensNum = "".join(list(segment)[endInd + 1:])

    box = hash(label)
    contents = boxes[box]

    if operation == '-':
        if label in contents:
            contents.pop(label)
    
    else:
        contents[label] = lensNum


total = 0
for boxNum, key in enumerate(boxes):
    focusPower = 0
    for lensInd, lensLabel in enumerate(boxes[key]):
        lensNum = int(boxes[key][lensLabel])
        focusPower = (boxNum + 1) * (lensInd + 1) * (lensNum)

        total += focusPower


print("Answer:", total)
    


    

