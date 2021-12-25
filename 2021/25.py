from copy import deepcopy

with open("25.txt") as f:
   fieldlines = f.readlines()

field=[]

for line in fieldlines:
    line = line.strip()
    field.append([c for c in line])

len_y = len(field)
len_x = len(field[0])

def iterate_field(field):
    newfield = deepcopy(field)
    for y, line in enumerate(field):
        for x, _ in enumerate(line):
            c =  field[y][x]
            if c == '.':
                continue
            elif c == '>':
                next_x = (x + 1) % len_x 
                if field[y][next_x] == '.':
                    newfield[y][next_x] = '>'
                    newfield[y][x] = '.'
    field = deepcopy(newfield)
    for y, line in enumerate(field):
        for x, _ in enumerate(line):
            c =  field[y][x]
            if c == '.':
                continue
            elif c == 'v':
                next_y = (y + 1) % len_y
                if field[next_y][x] == '.':
                    newfield[next_y][x] = 'v'
                    newfield[y][x] = '.'
    return newfield

def field_to_string(field):
    s = ""
    for line in field:
        s += "".join(line)
    return s

steps = 1
newfield = iterate_field(field)
while field_to_string(newfield) != field_to_string(field):
    field = newfield
    newfield = iterate_field(field)
    steps+=1

print(steps)
