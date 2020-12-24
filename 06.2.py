import collections
import math
import re
import sys

with open('06.txt') as f:
  input=f.read()

groups=input.split('\n\n')

unique=0
for group in groups:
  answers=set()
  people=0
  for a in group.split('\n'):
    people+=1
    for c in a:
      answers.add(c)
  unique+=len(answers)

print(unique)
