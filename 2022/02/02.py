
with open ('02.txt') as f:
    lines = f.readlines()

opval = {
    "A": 1,
    "B": 2,
    "C": 3
}

myval = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

gameval = {
    "l": 0,
    "t": 3,
    "w": 6
    }

results = {
    "AX": "t",
    "AY": "w",
    "AZ": "l",
    "BX": "l",
    "BY": "t",
    "BZ": "w",
    "CX": "w",
    "CY": "l",
    "CZ": "t",
    }

matches = []
for line in lines:
    matches.append(line.strip().split(' '))

score = 0
for match in matches:
    score += gameval[results[match[0]+match[1]]] + myval[match[1]]

print(score)



# part 2

results = { 
    "AX": 0+3,
    "AY": 3+1,
    "AZ": 6+2,
    "BX": 0+1,
    "BY": 3+2,
    "BZ": 6+3,
    "CX": 0+2,
    "CY": 3+3,
    "CZ": 6+1,
    } 

score = 0
for match in matches:
    score += results[match[0]+match[1]]

print(score)
