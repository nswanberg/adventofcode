import collections
import math
import re
import sys

#with open('09-small.txt') as f:
with open('09.txt') as f:
  input=f.read().split('\n')

# Code here
nums = [int(n) for n in input if n]

windowsize=25
start=windowsize
end=len(nums)

def is_in_window(x, nums):
 possible=set()
 for i in nums:
   for j in nums[1:]:
     if i != j:
       possible.add(i+j)
 if x not in possible:
   return x
 else:
   return None

for i in range(len(nums)-windowsize):
  missing = is_in_window(nums[windowsize+i], nums[i:windowsize+i])
  if missing:
    print(missing)


