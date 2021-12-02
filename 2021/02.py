with open('02.txt') as f:
    lines = f.readlines()

depth=0
horizontal=0
for line in lines:
    arg, quant = line.split()
    quant = int(quant)
    if arg == "forward":
        horizontal += quant
    elif arg == "down":
        depth += quant
    elif arg == "up":
        depth -= quant

print(depth*horizontal)


depth=0
horizontal=0
aim=0
for line in lines:
    arg, quant = line.split()
    quant = int(quant)
    if arg == "forward":
        horizontal += quant
        depth += (aim * quant)
    elif arg == "down":
        aim += quant
    elif arg == "up":
        aim -= quant

print(depth*horizontal)
