from copy import deepcopy
import collections
import math
import re
import sys

with open('12-small.txt') as f:
  smallinput=[l for l in f.read().split('\n') if l]

with open('12.txt') as f:
  input=[l for l in f.read().split('\n') if l]

px=0
py=0
heading=90

for input in input:
  op = input[0]
  val = int(input[1:])
  if op == 'N':
    py+=val
  elif op == 'E':
    px+=val
  elif op == 'S':
    py-=val
  elif op == 'W':
    px-=val
  elif op == 'F':
    if heading == 0:
      py+=val
    elif heading == 90:
      px+=val
    elif heading == 180:
      py-=val
    elif heading == 270:
      px-=val
  elif op == 'R':
    heading += val
    heading = heading % 360
  elif op == 'L':
    heading -= val
    heading = heading % 360
  print(px,py)

print(abs(px)+abs(py))
