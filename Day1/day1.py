import re

def convert(word):
    # word is either a spelled out digit or a number (as a string)
    if (word == "one"):
        out = 1
    elif (word == "two"):
        out = 2
    elif (word == "three"):
        out = 3
    elif (word == "four"):
        out = 4
    elif (word == "five"):
        out = 5
    elif (word == "six"):
        out = 6
    elif (word == "seven"):
        out = 7
    elif (word == "eight"):
        out = 8
    elif (word == "nine"):
        out = 9
    
    else:  # word is a number (as a string)
        out = word
    
    return str(out)


with open("input.txt", "r") as fid:
    data = fid.readlines()


regex_part1 = r"\d"
regex_part2 = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"  # allows for overlaps with lookahead

part = int(input("Select part [1 | 2]: "))
if (part == 1):
    regex = regex_part1
else:
    regex = regex_part2


total = 0
for line in data:
    line = line.strip()

    nums = re.findall(regex, line)  # returns list (ordered) of patterns found

    if len(nums) > 1:
        num1 = convert(nums[0])
        num2 = convert(nums[-1])

        sum = num1 + num2  # string concatenation
        total += int(sum)

    else:
        num3 = convert(nums[0])
        sum = int(num3 + num3)
        total += sum


print("Answer for part {}:".format(part))
print(total)
    




