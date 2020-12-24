from copy import deepcopy
import collections
import math
import re
import sys

with open('13-small.txt') as f:
  smallinput=[l for l in f.read().split('\n') if l]

input = smallinput

with open('13.txt') as f:
  input=[l for l in f.read().split('\n') if l]

timestamp=int(input[0])
busses=[int(i) for i in input[1].split(',') if i != 'x']

foundbus=False
t=timestamp
pickup=[]
while True:
  pickup = [t % b for b in busses]
  if 0 in pickup:
    break
  t+=1

print(input[1])
print(pickup)
print(t-timestamp)
