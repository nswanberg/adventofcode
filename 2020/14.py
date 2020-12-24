from copy import deepcopy
import collections
import math
import re
import sys

with open('14.txt') as f:
  biginput=[l for l in f.read().split('\n') if l]

smallinput="""mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
smallinput=[l for l in smallinput.split('\n') if l]

input = biginput


def applymask(mask,n):
  conv = [int(i) for i in bin(int(n))[2:]]
  conv = ([0] * (36 - len(conv))) + conv
  #print(conv)
  #print('mask',mask)
  for i in range(len(mask)):
    if mask[i] == '0':
      continue
    elif mask[i] == '1':
      conv[i] = 1
  xcount = mask.count('X')
  copycount = 2**xcount
  reslist=[]
  for c in range(copycount):
    reslist.append(conv.copy())
  #print('copies',xcount,copycount,len(reslist)) 
  count=0
  for r in range(len(reslist)):
    #print('before',reslist[r])
    binstring=bin(count)[2:]
    binstring=('0' * (xcount - len(binstring))) + binstring
    pos=0
    for i in range(len(mask)):
      if mask[i] == 'X':
        #print(len(reslist[r]))
        #print(r,i,len(binstring),xcount,count,xcount-pos-1)
        #print('binstring',binstring)
        reslist[r][i] = int(binstring[xcount-pos-1])
        pos+=1
    count+=1
    #print(' after',reslist[r])
  #print(conv)
  #print(reslist)
  return [int(''.join(map(str, r)), 2) for r in reslist]


mem={}
for op in input:
  op, val = op.split(' = ')
  if "mask" in op:
    mask=val
  else:
    val=int(val)
    addr = re.search('\[(\d+)\]',op)[1]
    addrs=applymask(mask,addr)
    #print('addrs',addrs)
    for a in addrs:
      mem[a]=val
#print(mask, mem)

print(sum([v for v in mem.values()]))
