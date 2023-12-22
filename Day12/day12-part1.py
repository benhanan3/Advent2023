

def solve(line, index, runningTotal, totalNum, groups):
    # base case
    if (runningTotal == totalNum):
        line = finishLine(line, index)
        variations = checkConfig(line, groups)
        return variations

    if (index >= len(line)):  # ran out of '?' But has not reached totalNum. Automatically invalid.
        return 0

    while( line[index] != "?" ):
        index += 1
        if (index >= len(line)):  # ran out of '?' But has not reached totalNum. Automatically invalid.
            return 0

    variations = 0
    line[index] = '#'
    variations += solve(line.copy(), index+1, runningTotal+1, totalNum, groups)

    line[index] = '.'
    variations += solve(line.copy(), index+1, runningTotal, totalNum, groups)

    return variations


def finishLine(line, index):
    length = len(line)
    for i in range(index, length):
        if line[index] == '?':
            line[index] = '.'
    
    return line


def checkConfig(line, ansGroups):
    # returns 1 if the line satisfies group
    # returns 0 if its not a valid match
    length = len(line)
    index = 0
    foundGroups = []
    while (index < length):
        runningTotal = 0
        # finds index of '#'
        while ((index < length) and (line[index] != '#')):
            index += 1
        
        while ((index < length) and (line[index] == '#')):
            runningTotal += 1
            index += 1

        if runningTotal != 0:
            foundGroups.append(runningTotal)

        index += 1

    if foundGroups == ansGroups:
        return 1
    else:
        return 0



with open("input.txt", "r") as fid:
    data = fid.readlines()


answer = 0  # sum of total possible arrangements
for line in data:
    puzzle, groups = line.strip().split(" ")

    puzzle = list(puzzle)

    groups = groups.split(",")
    groups = [int(i) for i in groups]

    totalNum = 0
    for char in puzzle:
        if (char == '#'):
            totalNum += 1
    totalNum = sum(groups) - totalNum  # total number of '#' to be placed


    # iterate through line. At every question mark you can
    # place a # or a .
    # Once you run out of total #, round is finished.
    # Count the arrangement only if valid

    rtv = solve(puzzle, 0, 0, totalNum, groups)
    print(rtv)
    answer += rtv


print("Answer:", answer)