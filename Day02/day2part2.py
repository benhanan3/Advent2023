import re

with open("input.txt", "r") as fid:
    data = fid.readlines()

regexRed = r"(\d+)\sred"
regexGreen = r"(\d+)\sgreen"
regexBlue = r"(\d+)\sblue"

total = 0
for line in data:
    line = line.strip()

    line = line.split(":")
    
    game = int(re.findall("\d+", line[0])[0])
    
    cubesList = line[1]

    rounds = cubesList.split(";")

    minRed = 0
    minBlue = 0
    minGreen = 0
    for round in rounds:
        red = [int(i) for i in re.findall(regexRed, round)]
        green = [int(i) for i in re.findall(regexGreen, round)]
        blue = [int(i) for i in re.findall(regexBlue, round)]

        if not red:
            red = [0]
        
        if not green:
            green = [0]
        
        if not blue:
            blue = [0]


        if max(red) > minRed:
            minRed = max(red)

        if max(green) > minGreen:
            minGreen = max(green)

        if max(blue) > minBlue:
            minBlue = max(blue)

    
    power = minBlue * minRed * minGreen
    total += power

print(total)