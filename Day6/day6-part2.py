import re
from functools import reduce
import math

with open("input.txt", "r") as fid:
    data = fid.readlines()



time = [ i for i in re.findall(r"\d+", data[0]) ]
distance = [ i for i in re.findall(r"\d+", data[1]) ]

time = int(reduce((lambda x, y: x+y), time))
distance = int(reduce((lambda x, y: x+y), distance))


try:
    x1 = ( (time) - math.sqrt((time ** 2) - 4 * distance) ) / 2
    x2 =  ( (time) + math.sqrt((time ** 2) - 4 * distance) ) / 2
except ValueError:
    x1 = 0
    x2 = 0

x1 = math.ceil(x1 + .00001) # non inclusive boundaries. Looking to win, not tie
x2 -= .00001
count = 0
while(x1 < x2):
    count += 1
    x1 += 1

print(count)


