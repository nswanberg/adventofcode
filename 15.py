from copy import deepcopy
from collections import deque, defaultdict
import math
import re
import sys

with open('15.txt') as f:
  input=[l for l in f.read().strip().split('\n') if l]

#inputstring = "0,3,6"
inputstring = "0,6,1,7,2,19,20"

input=[int(i) for i in inputstring.strip().split(',')]

#print(input)

turn=1
spoken=defaultdict(deque)
lastspoken=None
while turn <= 30000000:
  if turn <= len(input):
    spoken[input[turn-1]].append(turn)
    lastspoken=input[turn-1]
  else:
    lastspokencount = len(spoken[lastspoken])
    if lastspokencount == 1:
      lastspoken=0
    else:
      lastspoken=spoken[lastspoken][-1] - spoken[lastspoken][-2]
    spoken[lastspoken].append(turn)
    lastspokencount = len(spoken[lastspoken])
    if lastspokencount == 3:
      spoken[lastspoken].popleft()
  #print(turn,lastspoken, spoken)
  #print(lastspoken, [v for s in spoken.keys() for v in spoken[s]])
  turn+=1
print(lastspoken)
