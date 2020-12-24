import collections
import math
import re
import sys

with open('06.txt') as f:
  input=f.read()

groups=input.split('\n\n')

everyone=0
for group in groups:
  print('--')
  answers=collections.defaultdict(int)
  people=0
  for a in group.split('\n'):
    if not a:
      break
    people+=1
    for c in a:
      print('adding ',c)
      answers[c]+=1
  print(answers.keys())
  for a in answers.keys():
    print(a,people)
    if answers[a]==people:
      print('adding ',a)
      everyone+=1     

print(everyone)
