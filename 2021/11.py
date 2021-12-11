import copy

with open('11.txt') as f:
    lines = f.readlines()

octo=[]
for line in lines:
    line = line.strip()
    octo.append([int(o) for o in line])

newocto=copy.deepcopy(octo)

def printg(grid):
    for l in grid:
        print(''.join([str(i) for i in l]))
    print()

def get_relative_pos(cur,rel,map):
    x,y = rel 
    x1,y1 = cur
    dx = x+x1
    dy = y+y1
    # skip out of bounds
    if dy < 0 or dy >= len(map):
        return None
    if dx < 0 or dx >= len(map[0]):
        return None
    # skip self
    if rel == (0,0):
        return None
    return (dx,dy)
   
def get_element(matrix,tup):
    x,y = tup
    return matrix[y][x]

def inc_element(matrix,tup):
    x,y = tup
    val = matrix[y][x]
    matrix[y][x] += 1
    return matrix[y][x]

def set_element(matrix,tup, val):
    x,y = tup
    matrix[y][x] = val 

flashes=0
firstzeros=-1
s=0
while firstzeros == -1:
    octsum=0
    for r in octo:
        octsum+=sum(r)
    if octsum==0:
        firstzeros=s
        print(s)
    #print(s)
    #printg(octo)
    flashpoints=[]
    flashed=set()
    for y in range(len(octo)):
        for x in range(len(octo[0])):
            # increment every element
            pos=(x,y)
            val = inc_element(octo,pos)
            if val == 10:
                flashpoints.append(pos)
            else:
                # none should be over 10 now
                assert val < 10, f"pos {pos} val {val} invalid"
       
    while True:
        if not flashpoints:
            break
        pos = flashpoints.pop()
        if pos in flashed:
            continue
        flashed.add(pos)
        flashes+=1
        set_element(octo, pos, 0)
        # increment elements surrounding flash, but skip those already flashed
        for y1 in [-1,0,1]:
            for x1 in [-1,0,1]:
                relpos = get_relative_pos(pos, (x1,y1), octo)
                if relpos and relpos not in flashed:
                    val = inc_element(octo, relpos)
                    if val == 10:
                        flashpoints.append(relpos)
    s+=1

printg(octo)
print(flashes)
print(firstzeros)
                    



