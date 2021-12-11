with open('09.txt') as f:
    lines = f.readlines()

cavemap = []
for line in lines:
    line=line.strip()
    caverow=[int(c) for c in line]
    cavemap.append(caverow)

print(f"h: {len(cavemap)}")
print(f"w: {len(cavemap[0])}")

lowpoints=[]

for i in range(len(cavemap)):
    for j in range(len(cavemap[0])):
        surround = []
        center = cavemap[i][j]
        #top
        if i>0:
            surround.append(cavemap[i-1][j])
        #middle
        if j>0:
            surround.append(cavemap[i][j-1])
        if j<len(cavemap[0])-1:
            surround.append(cavemap[i][j+1])

        #bottom
        if i<len(cavemap)-1:
            surround.append(cavemap[i+1][j])

        lowers = [i for i in surround if i<=center]
        if surround and not lowers:
            lowpoints.append(center+1)

print(sum(lowpoints))

def valid_pos(pos, cavemap, explored):
    x,y = pos
    if y < 0 or y >= len(cavemap):
        return False
    if x < 0 or x >= len(cavemap[0]):
        return False
    if pos in explored:
        return False
    return True

def find_boundaries(pos, cavemap, explored):
    basin=[]
    explored.add(pos)
    x,y = pos
    val=cavemap[y][x]
    if val == 9:
        return []
    basin.append(val)
    for dx,dy in [(0,-1),(0,1),(-1,0),(1,0)]:
        relpos = (x+dx,y+dy)
        if valid_pos(relpos, cavemap, explored):
          basin = basin + find_boundaries(relpos, cavemap, explored)
    return basin

explored=set()
basins=[]
for i in range(len(cavemap)):
    for j in range(len(cavemap[0])):
        if (j,i) in explored:
            continue
        explored.add((j,i))
        val = cavemap[i][j]
        if val == 9:
            continue
        basin = find_boundaries((j,i),cavemap, explored)
        basins.append(basin)

acc=1
for i in sorted([len(b) for b in basins],reverse=True)[:3]:
    acc*=i
print(acc)
   
