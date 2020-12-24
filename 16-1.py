from copy import deepcopy
from collections import deque, defaultdict
import math
import re
import sys

with open('16.txt') as f:
  rules, myticket, neartickets = f.read().strip().split('\n\n') 

rulesdict={}
for line in rules.split('\n'):
 name, listtext = line.split(': ')
 rulesdict[name]=listtext.split(' or ')

badvals=[]
notbadtickets=[]
for t in neartickets.split('\n')[1:]:
  ticketvals = [int(i) for i in t.split(',')]
  tickethasbadval=False
  for val in ticketvals:
    found=False
    for rule in rulesdict.values():
      for range_text in rule:
         first,last=range_text.split('-')
         first=int(first)
         last=int(last)
         if val in range(first,last+1):
           #print('found ',str(val),'in ',range_text)
           found=True
    if not found:
      #print('not find ',str(val))
      badvals.append(val)
      tickethasbadval=True
  if not tickethasbadval:
    notbadtickets.append(t)



print(sum(badvals))
print(len(notbadtickets))


