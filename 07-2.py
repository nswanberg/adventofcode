import collections
import math
import re
import sys

#with open('07-small.txt') as f:
with open('07.txt') as f:
  input=f.read()


def split_count(bag):
  r=re.search('(\d+) ([a-z ]+)',bag)
  if r:
    return (int(r.group(1)), r.group(2))
  return None

rules = input.split('\n')
bagdict={}
invertdict=collections.defaultdict(list)
for rule in rules:
  if not rule:
    break
  rule = rule.replace('bags','bag')
  splitted=rule.split('contain')
  splitted=[str.strip() for str in splitted if str]
  bags = [split_count(bag) for bag in splitted[1].split(',')]
  bagdict[splitted[0]] = bags

for key in bagdict.keys():
  for val in bagdict[key]:
    invertdict[val].append(key)

#print(invertdict)
print(bagdict)

def get_bag_count(search_bag):
  bagcount=0
  bags = bagdict[search_bag]
  for bag in bags:
    if bag:
      bagcount+= bag[0]
      bagcount +=  (bag[0] * get_bag_count(bag[1]))
  return bagcount

bagcount= get_bag_count('shiny gold bag')

print(bagcount)
