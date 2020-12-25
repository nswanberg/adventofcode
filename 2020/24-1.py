from collections import defaultdict

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
