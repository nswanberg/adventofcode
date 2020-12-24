from copy import deepcopy
import collections
import math
import re
import sys

with open('11-small.txt') as f:
  smallinput=[list(l) for l in f.read().split('\n') if l]

with open('11.txt') as f:
  input=[list(l) for l in f.read().split('\n') if l]

def arrlen(arr):
  return len([x for y in arr for x in y])

def inrange(pos,m):
  height = len(m)
  width =  len(m[0])
  return 0 <= pos[1] < height and 0 <= pos[0] < width 

def addadj(pos,m,adj):
  if inrange(pos,m):
    adj.append(m[pos[1]][pos[0]])

def get_north(x,y,m):
  if y == 0:
    return None 
  for i in range(y-1,-1,-1):
    c = m[i][x]
    if c != '.':
      return c
  return None

def get_northeast(x,y,m):
  if x == len(m[0])-1 and y == 0:
    return ''
  i=x+1
  j=y-1
  while i < len(m[0]) and j >= 0:
    c = m[j][i]
    if c != '.':
      return c
    i+=1
    j-=1
  return None

def get_east(x,y,m):
  if x == len(m[0])-1:
    return ''
  for i in range(x+1,len(m[0])):
    c = m[y][i]
    if c != '.':
      return c 
  return None

def get_southeast(x,y,m):
  if x == len(m[0])-1 and y == len(m)-1:
    return ''
  i=x+1
  j=y+1
  while i < len(m[0]) and j < len(m):
    c = m[j][i]
    if c != '.':
      return c
    i+=1
    j+=1
  return None

def get_south(x,y,m):
  if y == len(m)-1:
    return ''
  for i in range(y+1,len(m)):
    c = m[i][x]
    if c != '.':
      return c
  return None

def get_southwest(x,y,m):
  if x == 0 and y == len(m)-1:
    return ''
  i=x-1
  j=y+1
  while i >= 0 and j < len(m):
    c = m[j][i]
    if c != '.':
      return c
    i-=1
    j+=1
  return None

def get_west(x,y,m):
  if x == 0:
    return ''
  for i in range(x-1,-1,-1):
    c = m[y][i]
    if c != '.':
      return c
  return None

def get_northwest(x,y,m):
  if x == 0 and y == 0:
    return ''
  i=x-1
  j=y-1
  while i >= 0 and j >= 0:
    c = m[j][i]
    if c != '.':
      return c
    i-=1
    j-=1
  return None

def get_directions(x,y,input):
  seat = input[y][x]

  adj=[]

  adj.append(get_north(x,y,input))
  adj.append(get_northeast(x,y,input))
  adj.append(get_east(x,y,input))
  adj.append(get_southeast(x,y,input))
  adj.append(get_south(x,y,input))
  adj.append(get_southwest(x,y,input))
  adj.append(get_west(x,y,input))
  adj.append(get_northwest(x,y,input))

  #if x == 8 and y == 0:
  #  print(adj)

  adj = [a for a in adj if a]

  #if x == 8 and y == 0:
  #  print(adj)

  if seat == 'L':
    if adj.count('#') == 0:
      return '#'
  if seat == '#':
    #print('count #', adj.count('#'))
    #print(adj)
    if adj.count('#') >= 5:
      return 'L'
  return seat 
  

def get_adjacent(x,y,input):
  seat = input[y][x]
  upperleft =  (x-1,y-1)
  upper =      (x,  y-1)
  upperright = (x+1,y-1)
  left =       (x-1,  y)
  right =      (x+1,  y)
  lowerleft =  (x-1,y+1)
  lower     =  (x  ,y+1)
  lowerright = (x+1,y+1)

  adj=[]

  addadj(upperleft,input,adj)
  addadj(upper,input,adj)
  addadj(upperright,input,adj)
  addadj(left,input,adj)
  addadj(right,input,adj)
  addadj(lowerleft,input,adj)
  addadj(lower,input,adj)
  addadj(lowerright,input,adj)

  if seat == 'L':
    if adj.count('#') == 0:
      return '#'
  if seat == '#':
    #print('count #', adj.count('#'))
    #print(adj)
    if adj.count('#') >= 4:
      return 'L'
  return seat 
   

def evolve(input):
  mod = deepcopy(input)
  for y in range(len(input)):
    for x in range(len(input[0])):
      mod[y][x] = get_directions(x,y,input)
  return mod 

def printarray(input,name=""):
  for r in input:
    print(''.join(r))
  print('---',name,'\n')

def arrtostr(a):
  return ''.join([x for y in a for x in y])

def arrequal(a,b):
  return arrtostr(a)==arrtostr(b)


itr=0
arr_a = deepcopy(input)
arr_b = evolve(arr_a)
#printarray(arr_b, str(itr))
while not arrequal(arr_a, arr_b):
  arr_a = arr_b
  arr_b = evolve(arr_a)
  itr+=1
  #printarray(arr_b, str(itr))

print('seats: ', arrtostr(arr_b).count('#'))

#for r in arr_b:
#  print(''.join(r))
