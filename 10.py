import collections
import math
import re
import sys

#with open('10-small.txt') as f:
with open('10.txt') as f:
  input=f.read().split('\n')

nums = [int(n) for n in input if n]
nums.append(0)
nums.sort()
nums.append(nums[-1]+3)

print(nums)

diffs=[]
for i in range(1, len(nums)):
  diffs.append(nums[i] - nums[i-1])
print(diffs)
print(diffs.count(1) * diffs.count(3))

# split on 3s.  Multiply by 3 * 2^(n-1)
options=1
num_ones=0
for n in diffs:
  if n == 1:
    num_ones+=1
  if n == 3:
    if num_ones <= 1:
      pass  
    elif num_ones == 2:
      options*=2
    else:
      perms=3*(2**(num_ones-3))+1
      #print('perms',perms)
      options*=perms
    num_ones=0
  #print(options,num_ones)
print(options)

