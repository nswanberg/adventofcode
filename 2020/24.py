from collections import defaultdict
import copy

tinyinput = """esew
nwwswee"""

smallinput = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

lines = smallinput.splitlines()
#lines = tinyinput.splitlines()

with open('24.txt') as f:
  lines = f.read().strip().splitlines()

def tile_directions(s):
  directions=[]
  i = 0
  while i < len(s):
    if s[i] == 'n' or s[i] == 's':
      directions.append(s[i:i+2])
      i+=2
    else:
      directions.append(s[i])
      i+=1
  return directions


tiles=defaultdict(int)
for l in lines:
  currentTile = (0,0)
  for d in tile_directions(l):
    #print(currentTile,d)
    if d == 'e':
      currentTile = (currentTile[0]+1, currentTile[1])
    elif d == 'w':
      currentTile = (currentTile[0]-1, currentTile[1])
    elif d == 'ne':
      currentTile = (currentTile[0]+(currentTile[1] % 2), currentTile[1]-1)
    elif d == 'nw':
      currentTile = (currentTile[0]-((currentTile[1]+1) % 2), currentTile[1]-1)
    elif d == 'se':
      currentTile = (currentTile[0]+(currentTile[1] % 2), currentTile[1]+1)
    elif d == 'sw':
      currentTile = (currentTile[0]-((currentTile[1]+1) % 2), currentTile[1]+1)
    else:
      assert False
    #print(currentTile)
  tiles[currentTile] = (tiles[currentTile] + 1) % 2

print(sum(tiles.values()))
print(len(tiles.keys()))
#for t in tiles.keys():
#  print(t, tiles[t])

def getTileValue(tiles, currentTile, d):
    if d == 'e':
      currentTile = (currentTile[0]+1, currentTile[1])
    elif d == 'w':
      currentTile = (currentTile[0]-1, currentTile[1])
    elif d == 'ne':
      currentTile = (currentTile[0]+(currentTile[1] % 2), currentTile[1]-1)
    elif d == 'nw':
      currentTile = (currentTile[0]-((currentTile[1]+1) % 2), currentTile[1]-1)
    elif d == 'se':
      currentTile = (currentTile[0]+(currentTile[1] % 2), currentTile[1]+1)
    elif d == 'sw':
      currentTile = (currentTile[0]-((currentTile[1]+1) % 2), currentTile[1]+1)
    else:
      assert False
    return tiles[currentTile]

def getAdjacentList(tiles, currentTile):
    adjacent=[]
    adjacent.append((currentTile[0]+1, currentTile[1]))
    adjacent.append((currentTile[0]-1, currentTile[1]))
    adjacent.append((currentTile[0]+(currentTile[1] % 2), currentTile[1]-1))
    adjacent.append((currentTile[0]-((currentTile[1]+1) % 2), currentTile[1]-1))
    adjacent.append((currentTile[0]+(currentTile[1] % 2), currentTile[1]+1))
    adjacent.append((currentTile[0]-((currentTile[1]+1) % 2), currentTile[1]+1))
    return adjacent

def getAdjacentBlackCount(tiles, loc):
  ne = getTileValue(tiles, loc, 'ne') 
  nw = getTileValue(tiles, loc, 'nw') 
  e = getTileValue(tiles, loc, 'e') 
  se = getTileValue(tiles, loc, 'se') 
  sw = getTileValue(tiles, loc, 'sw') 
  w = getTileValue(tiles, loc, 'w')
  #print([ne, nw, e, se, sw, w])
  return sum([ne, nw, e, se, sw, w])

tilesEvolve = copy.copy(tiles)
i=1
while i <= 100:
  #print('Day ',i,': ', sum(tiles.values()))
  for loc in tiles.keys():
    # if black, ensure surrounding keys are present
    if tiles[loc]:
      for l in getAdjacentList(tiles, loc):
        tiles[l]=tiles[l]
  for loc in tiles.keys():
    tileColor = tiles[loc]
    blackCount = getAdjacentBlackCount(tiles, loc)
    if tileColor: # black tile
      if blackCount == 0 or blackCount > 2:
        tilesEvolve[loc] = 0
    else: # white tile
      if blackCount == 2:
        tilesEvolve[loc] = 1
    #print('loc', loc, 'tileColor', tileColor, 'blackCount', blackCount, 'new',tilesEvolve[loc],\
    #  'changed', tilesEvolve[loc] != tiles[loc])
  tiles = copy.copy(tilesEvolve) 
  #print(sum(tiles.values()))
  i+=1

print(sum(tiles.values()))

