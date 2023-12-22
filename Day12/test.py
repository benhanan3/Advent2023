import re

def finishLine(line):
    line = "".join(line)

    line = re.sub(r'\?', '.', line)
    
    return line


line = '##..??'

line = finishLine(line)
print(line)