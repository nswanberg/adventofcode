from copy import deepcopy
import collections
import math
import re
import sys

with open('14l.txt') as f:
  smallinput=[l for l in f.read().split('\n') if l]

input = smallinput


def applymask(mask,n):
  conv = [int(i) for i in bin(n)[2:]]
  conv = ([0] * (36 - len(conv))) + conv
  #print(conv)
  for i in range(len(mask)):
    if mask[i] == 'X':
      continue
    elif mask[i] == '0':
      conv[i] = 0
    elif mask[i] == '1':
      conv[i] = 1
  #print(conv)  
  return int(''.join(map(str, conv)), 2)


mem={}
for op in input:
  op, val = op.split(' = ')
  if "mask" in op:
    mask=val
  else:
    val=int(val)
    conv=applymask(mask,val)
    addr = re.search('\[(\d+)\]',op)[1]
    mem[addr]=conv
#print(mask, mem)

print(sum([v for v in mem.values()]))
