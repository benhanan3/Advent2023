

def solve(line, index, runningTotal, totalNum, groups, totalArrangements):
    # base case
    if (runningTotal == totalNum):
        totalArrangements += checkConfig(line, groups)

    while( line[index] != "?" ):
        index += 1

    line[index] = '#'
    solve(line, index+1, )



def checkConfig(line, groups):
    pass



with open("input-test.txt", "r") as fid:
    data = fid.readlines()


for line in data:
    puzzle, groups = line.strip().split(" ")

    groups = groups.split(",")
    groups = [int(i) for i in groups]

    totalNum = sum(groups)

    print(puzzle)
    print(groups)
    print(totalNum)
    print()

    # iterate through line. At every question mark you can
    # place a # or a .
    # Once you run out of total #, round is finished.
    # Count the arrangement only if valid


