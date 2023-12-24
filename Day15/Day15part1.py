


with open("input.txt", "r") as fid:
    data = fid.read()

data = data.strip().split(",")

total = 0
for segment in data:
    currVal = 0
    for char in segment:
        currVal += ord(char)
        currVal *= 17
        currVal %= 256
    
    total += currVal

print("Answer:", total)