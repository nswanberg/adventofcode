import re
import math

with open('20.txt') as f:
  input = f.read()

tiles_text = input.strip().split('\n\n')

class Tile:
  def __init__(self, text):
    lines = text.splitlines()
    self.id = re.search('(\d+)',lines[0])[1]
    self.top = lines[1]
    self.bottom = lines[-1]
    self.left = ''.join([l[0] for l in lines[1:]])
    self.right = ''.join([l[-1] for l in lines[1:]])
    self.text = [[c for c in row] for row in text.splitlines()[1:]]

  def gettop(self):
    return ''.join(self.text[0])

  def getbottom(self):
    return ''.join(self.text[-1])

  def getleft(self):
    return ''.join([l[0] for l in self.text])

  def getright(self):
    return ''.join([l[-1] for l in self.text])
 
  def sides(self):
    sides=[]
    sides.append(self.top)
    sides.append(''.join([i for i in reversed(self.top)]))
    sides.append(self.bottom)
    sides.append(''.join([i for i in reversed(self.bottom)]))
    sides.append(self.left)
    sides.append(''.join([i for i in reversed(self.left)]))
    sides.append(self.right)
    sides.append(''.join([i for i in reversed(self.right)]))
    return sides

  def flip(self, orientation):
    #print('flip before ', orientation % 4)
    #print( self.showtext())

    if orientation % 4 == 0: # flip y
      self.text = [i for i in reversed(self.text)]

    if orientation % 4 == 2: # flip x
      for i in range(len(self.text)):
        self.text[i] = [c for c in reversed(self.text[i])]

    if orientation % 4 == 1: # flip xy 
      #print('flipping xy')
      for i in range(len(self.text)):
        for j in range(i,len(self.text)):
          tmp = self.text[i][j] 
          #print(i,j,'i j', self.text[i][j],'j i',self.text[j][i])
          self.text[i][j] = self.text[j][i]
          self.text[j][i] = tmp

    if orientation % 4 == 3: # flip yx
      #print('flipping yx')
      # all orientations
      self.text = [i for i in reversed(self.text)]

      for i in range(len(self.text)):
        self.text[i] = [c for c in reversed(self.text[i])]

      for i in range(len(self.text)):
        for j in range(i,len(self.text)):
          tmp = self.text[i][j] 
          #print(i,j,'i j', self.text[i][j],'j i',self.text[j][i])
          self.text[i][j] = self.text[j][i]
          self.text[j][i] = tmp

    #print('flip after ', orientation % 4)
    #print( self.showtext())


  def showtext(self):
    text=""
    for row in self.text:
      for c in row:
        text+=c
      text+='\n' 
    return text

  def print(self, border=1):
    ret = []
    start = border
    end = len(self.text) - border
    for row in self.text[start:end]:
      line=''.join(row[start:end])
      ret.append( line ) 
    return ret

  def __str__(self):
    return str(self.id)
  
  def __repr__(self):
    return str(self.id)

def get_matching_tile(tiles,tile,side):
  for candidate in tiles:
    if tile.id == candidate.id:
      continue
    if side in candidate.sides():
      return candidate           

def find_neighbors(tiles, tile):
  has_top = get_matching_tile(tiles, tile, tile.top)
  has_bottom = get_matching_tile(tiles, tile, tile.bottom)
  has_left = get_matching_tile(tiles, tile, tile.left)
  has_right = get_matching_tile(tiles, tile, tile.right)
  return (has_top, has_bottom, has_left, has_right)

tiles=[]
for t in tiles_text:
  tile = Tile(t)
  tiles.append(tile) 

corners=[]
for t in tiles:
  matches=0
  for s in t.sides():
    for candidate in tiles:
      if t.id == candidate.id:
        continue
      if s in candidate.sides():
        matches+=1
  if (matches//2)==2:
    corners.append(t)

res=1
for c in corners:
  res*=int(c.id)
# part 1 sln
#print(res)

side_len = int(math.sqrt(len(tiles)))
tilearray=[[ None for j in range(side_len)] for i in range(side_len)]

# get the first corner tile
# upper right
upper_right=None
for c in corners:
  n = find_neighbors(tiles, c)
  print('neighbors',n)
  if n[1] and n[3]:
    upper_right = c

for c in corners:
  print(c.id)

#manually set upper right to last
#upper_right = corners[1]

#print('upper right corner', upper_right)
#print(upper_right.showtext())

"""
print(upper_right.getleft())
print(upper_right.getright())
print(upper_right.gettop())
print(upper_right.getbottom())
"""

# now have the upper right corner (has a right and bottom)
tilearray[0][0] = upper_right

for i in range(len(tilearray)):
  for j in range(len(tilearray)):
    if i == j == 0:
      continue
    if j == 0: # use match bottom of i-1 to top of j
      prev = tilearray[i-1][0]
      #print('finding tile in', i, j, 'to match', prev.id)
      foundtile=False
      #print(prev.showtext())
      #print(find_neighbors(tiles, prev))
      for tile in tiles:
        #print('checking tile ', prev, tile)
        if prev.id == tile.id:
          continue
        for orientation in range(8):
          tile.flip(orientation)
          #print(matched, prev, orientation)
          #print(tile, prev, orientation, tile.gettop(), prev.getbottom(), tile.gettop() == prev.getbottom())
          if tile.gettop() == prev.getbottom():
            #print('found match', tile.id)
            tilearray[i][j] = tile
            foundtile=True
            break
      assert foundtile
      """
      print('prev')
      print(prev.showtext(), '\n')
      print('matched')
      print(matched.showtext(),'\n')
      """
    else: #match right side of tile
      prev = tilearray[i][j-1]
      #print('finding tile in', i, j, 'to match', prev.id)
      # add the tile that matches the right side
      foundtile=False
      for tile in tiles:
        #print('checking tile ', prev, tile)
        if prev.id == tile.id:
          continue
        for orientation in range(8):
          tile.flip(orientation)
          #print(tile, prev, orientation, tile.getleft(), prev.getright(), tile.getleft() == prev.getright())
          if tile.getleft() == prev.getright():
            #print('found match', tile.id)
            tilearray[i][j] = tile
            foundtile = True
            break
      assert foundtile
      """
      print('prev')
      print(prev.showtext(), '\n')
      print('matched')
      print(matched.showtext(),'\n')
      """

"""
for r in tilearray:
  print(r)

print(upper_right.print())
""" 
image = ""

for i in range(len(tilearray)):
  for l in range(len(tilearray[0][0].print())):
    for j in range(len(tilearray)):
      image += tilearray[i][j].print()[l] # + ' '
    image += '\n'
  #image += '\n'

print(image)
print(len(image.splitlines()))
print(len(image.splitlines()[0]))

seamonsterpattern="""                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

seamonsterarray=[[c for c in line] for line in seamonsterpattern.splitlines()]

seamonsterpos=[]
for i,row in enumerate(seamonsterarray):
  for j,c in enumerate(row):
    if c == '#':
      seamonsterpos.append((j,i))

s_h=len(seamonsterarray)
s_w=len(seamonsterarray[0])
print(seamonsterpos, s_w, s_h)

def scan_monster(seamonsterpos, monster_width, monster_height, image):
  imagearray = [[c for c in row] for row in image.splitlines()]
  for i in range(len(imagearray)-monster_height):
    for j in range(len(imagearray[0]) - monster_width):
      found_monster=True
      #print('looking at ',i,j,i+monster_height,j+monster_width)
      for k in range(i, i+monster_height):
        for l in range(j, j+monster_width):
          checkpos=(l-j, k-i)
          #print(i,j,k,l,checkpos, checkpos in seamonsterpos, imagearray[k][l]) 
          if (l-j,k-i) in seamonsterpos and imagearray[k][l] != '#':
            found_monster=False
            #print('no monster', (l-j,k-i), (l,k))
            break
      if not found_monster:
        continue
      #print('found monster at ', i,j)
      for k in range(i, i+monster_height):
        for l in range(j, j+monster_width):
          if (l-j,k-i) in seamonsterpos and imagearray[k][l] == '#':
            imagearray[k][l]='O' 
  return showtext(imagearray)

def showtext(textarray):
  text=""
  for row in textarray:
    for c in row:
      text+=c
    text+='\n' 
  return text


originaltestimage=""".####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.O#..
#.O.##.OO#.#.OO.##.OOO##
..#O.#O#.O##O..O.#O##.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.##O###.
.O##.#OO.###OO##..OOO##.
..O#.O..O..O.#O##O##.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#"""

testimage=originaltestimage.replace('O','#')

scanned=scan_monster(seamonsterpos, s_w, s_h, testimage)
print(scanned)
print('testimage',scanned.count('#'))
print('originaltestimage', originaltestimage.count('#'))

diff=""

def flip(text, orientation):
  textarray = [[c for c in row] for row in text.splitlines()]
  if orientation % 4 == 0: # flip y
    #print('flip y')
    textarray = [i for i in reversed(textarray)]

  if orientation % 4 == 2: # flip x
    #print('flip x')
    for i in range(len(textarray)):
      textarray[i] = [c for c in reversed(textarray[i])]

  if orientation % 4 == 1: # flip xy 
    #print('flip xy')
    for i in range(len(textarray)):
      for j in range(i,len(textarray)):
        tmp = textarray[i][j] 
        #print(i,j,'i j', textarray[i][j],'j i',textarray[j][i])
        textarray[i][j] = textarray[j][i]
        textarray[j][i] = tmp

  if orientation % 4 == 3: # flip yx
    #print('flip all')
    # all orientations
    textarray = [i for i in reversed(textarray)]

    for i in range(len(textarray)):
      textarray[i] = [c for c in reversed(textarray[i])]

    #print(len(textarray), len(textarray[0]))

    for i in range(len(textarray)):
      for j in range(i,len(textarray)):
        #print(i,j)
        tmp = textarray[i][j] 
        textarray[i][j] = textarray[j][i]
        textarray[j][i] = tmp

  return showtext(textarray)

for o in range(8):
  image = flip(image,o)
  scanned=scan_monster(seamonsterpos, s_w, s_h, image)
  print('habitat',scanned.count('#'))

