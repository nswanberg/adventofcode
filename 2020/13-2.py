from copy import deepcopy
import collections
import math
import re
import sys

with open('13-small.txt') as f:
  smallinput=[l for l in f.read().split('\n') if l]

#input = smallinput

input = "17,x,13,19"
input = "67,7,59,61"
input = "67,x,7,59,61"
input = "67,7,x,59,61"
input = "1789,37,47,1889"

with open('13.txt') as f:
  input=[l for l in f.read().split('\n') if l]
input=input[1]

busses=[i for i in input.split(',') ]

foundbus=False
t=-1
#t= 100000000000000
#t=100000178000000
maxnum = max([int(n) for n in busses if n != 'x'])
#skips=100000309000000 // maxnum 
#skips=100078631599956 // maxnum
skips=1447446942161519 // maxnum

def find(t):
  pickup=[]
  firstmatch=0
  timestamp_1=None
  for i in range(len(busses)):
    if busses[i] != 'x' and t % (i+x):
      return false
    else:
      return t

while True:
  t=maxnum*skips
  pos=busses.index(str(maxnum))
  t-=pos
  if skips % 100000 == 0:
    print(t)
  res=find(t)
  if res:
    print(res)
    break
  skips+=1

