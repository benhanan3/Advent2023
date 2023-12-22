
import re

def solve(line, index, groups):
    # always check if on the right track
    if (not checkLine(line, index, groups)):
        return 0
    
    # Count how many '#' have been placed. Count how many total
    hashtagGroups = re.findall(r'#+', "".join(line))
    hTagString = "".join(hashtagGroups)
    runningTotal = len(hTagString)

    totalNum = sum(groups)

    # base case. When all '#' have been placed.
    if (runningTotal == totalNum):
        line = finishLine(line)  # replaces all '?' with '.'
        variations = checkLine(line, len(line), groups)
        return variations

    if (index >= len(line)):  # ran out of '?' But has not reached totalNum. Automatically invalid.
        return 0

    while( line[index] != "?" ):
        index += 1
        if (index >= len(line)):  # ran out of '?' But has not reached totalNum. Automatically invalid.
            return 0

    variations = 0
    line[index] = '#'
    variations += solve(line.copy(), index+1, groups)

    line[index] = '.'
    variations += solve(line.copy(), index+1, groups)

    return variations


def finishLine(line):
    line = "".join(line)

    re.sub(r'\?', '.', line)
    
    return line


def checkLine(line, index, ansGroups):
    line = line[0:index + 1]
    line = "".join(line)

    rtv = re.findall(r'#+', line)
    groups = [str(len(i)) for i in rtv]
    
    if groups:
        del groups[-1]  # account for group in progress
    
    stringAnsGroups = "".join([str(i) for i in ansGroups])
    stringGroups = "".join(groups)
    if stringAnsGroups.startswith(stringGroups):
        return 1
    else:
        return 0




with open("input-test.txt", "r") as fid:
    data = fid.readlines()


answer = 0  # sum of total possible arrangements
for line in data:
    puzzle, groups = line.strip().split(" ")

    # puzzle and groups are lists to facilitate iteration and changing characters
    puzzle = '?'.join([puzzle for i in range(5)])
    puzzle = list(puzzle)

    groups = groups.split(",")
    groups = [int(i) for i in groups]
    groups = groups * 5

    # finds all sets of '#'
    hashtags = re.findall(r'#+', "".join(puzzle) )
    stringVers = "".join(hashtags)  # combines the list into one string of '#'. Allows for counting

    totalNum = sum(groups) - len(stringVers)  # number of '#' left to place in '?' spots.


    # iterate through line. At every question mark you can
    # place a # or a .
    # Once you run out of total #, round is finished.
    # Count the arrangement only if valid

    rtv = solve(puzzle, 0, groups)
    print(rtv)
    answer += rtv


print("Answer:", answer)