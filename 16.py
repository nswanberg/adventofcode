from copy import deepcopy
from collections import deque, defaultdict
import math
import re
import sys
from itertools import chain

#with open('16-2-small.txt') as f:
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

ticketvalues=[]
for t in notbadtickets:
  ticketvals = [int(i) for i in t.split(',')]
  ticketvalues.append(ticketvals)

#print(ticketvalues)

columns=[]
for i in range(len(ticketvalues[0])):
  column=[]
  for j in range(len(ticketvalues)):
    column.append([])
  columns.append(column)

print(len(columns),len(columns[0]))
print(len(ticketvalues),len(ticketvalues[0]))

for i in range(len(ticketvalues)):
  for j in range(len(ticketvalues[0])):
    #print((i,j),(j,i))
    columns[j][i] = ticketvalues[i][j]

#print(columns)

myticketvals=[int(i) for i in myticket.split('\n')[1].split(',')]

departurevals=[]
colpos={}
coloptions=defaultdict(set)
for rulename in rulesdict.keys():
  ranges=[]
  print('rulename',rulesdict[rulename])
  
  for range_text in rulesdict[rulename]:
    first,last=range_text.split('-')
    first=int(first)
    last=int(last)
    ranges.append(range(first,last+1))

  for c in range(len(columns)):
    #print(set(columns[c]))
    #print(set(chain(*ranges)))
    if set(columns[c]) <= set(chain(*ranges)):
      print('match for ',rulename, '. It is ',str(c))
      #if 'departure' in rulename:
      #departurevals.append(myticketvals[c])
      coloptions[rulename].add(c)
    else:
      #print('no')
      print('missing',set(columns[c]) - set(chain(*ranges)))
      pass

print(coloptions)

confirmed=set()
while [len(v) for v in coloptions.values() if len(v) > 1]:
  certain=None
  for name in coloptions.keys():
    if len(coloptions[name]) == 1 and list(coloptions[name])[0] not in confirmed:
      certain = list(coloptions[name])[0]
  for val in coloptions.values():
    if certain in val and len(val) > 1:
      val.remove(certain)
  confirmed.add(certain)
  print(coloptions, confirmed)

for key in coloptions.keys():
  if "departure" in key:
    print(coloptions[key])
    departurevals.append(myticketvals[list(coloptions[key])[0]])
 
print(departurevals)
print(math.prod(departurevals)) 
