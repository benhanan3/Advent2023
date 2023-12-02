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

    possible = True
    for round in rounds:
        red = [int(i) for i in re.findall(regexRed, round)]
        green = [int(i) for i in re.findall(regexGreen, round)]
        blue = [int(i) for i in re.findall(regexBlue, round)]

        if (red and (max(red) > 12)) or (green and (max(green) > 13)) or (blue and (max(blue) > 14)):
            possible = False

    if possible == True:
        total += game
        print(game)

print(total)