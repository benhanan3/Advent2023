import re
import math

with open("input.txt", "r") as fid:
    data = fid.readlines()



time = [ int(i) for i in re.findall(r"\d+", data[0]) ]
distance = [ int(i) for i in re.findall(r"\d+", data[1]) ]


ans = 1
for ind, time in enumerate(time):
    recordDist = distance[ind]

    try:
        x1 = ( (time) - math.sqrt((time ** 2) - 4 * recordDist) ) / 2
        x2 =  ( (time) + math.sqrt((time ** 2) - 4 * recordDist) ) / 2
    except ValueError:
        x1 = 0
        x2 = 0

    x1 = math.ceil(x1 + .00001) # non inclusive boundaries. Looking to win, not tie
    x2 -= .00001
    count = 0
    while(x1 < x2):
        count += 1
        x1 += 1

    if count != 0:
        ans *= count


print(ans)