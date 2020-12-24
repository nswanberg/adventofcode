from copy import deepcopy
import collections
import math
import re
import sys

with open('12-small.txt') as f:
  smallinput=[l for l in f.read().split('\n') if l]

with open('12.txt') as f:
  input=[l for l in f.read().split('\n') if l]

shipx=0
shipy=0
wptx=10
wpty=1

for input in input:
  op = input[0]
  val = int(input[1:])
  if op == 'N':
    wpty+=val
  elif op == 'E':
    wptx+=val
  elif op == 'S':
    wpty-=val
  elif op == 'W':
    wptx-=val
  elif op == 'F':
    i=0
    while i < val:
      shipx+=wptx
      shipy+=wpty
      i+=1
  elif (op == 'L' and val == 90) or (op == 'R' and val == 270):
    wptx,wpty = wpty,wptx
    wptx*=-1
  elif (op == 'L' or op == 'R') and val == 180:
    wptx*=-1
    wpty*=-1
  elif (op == 'L' and val == 270) or (op == 'R' and val == 90):
    wptx,wpty=wpty,wptx
    wpty*=-1
  print(shipx,shipy,wptx,wpty)

print(abs(shipx)+abs(shipy))
