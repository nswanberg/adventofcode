import collections
import math
import re
import sys

 with open('07-small.txt') as f:
#with open('07.txt') as f:
  input=f.read()


def remove_count(bag):
  r=re.search('\d+ ([a-z ]+)',bag)
  if r:
    return r.group(1)
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
  bags = [remove_count(bag) for bag in splitted[1].split(',')]
  bagdict[splitted[0]] = bags

for key in bagdict.keys():
  for val in bagdict[key]:
    invertdict[val].append(key)

print(invertdict)
print(bagdict)

search='shiny gold bag'
search_queue=[search]

checked_bag=set()
container_bags=set()
while len(search_queue) > 0:
  query=search_queue.pop()
  if query not in checked_bag:
    for result in invertdict[query]:
      print(result + ' contains ' + query)
      container_bags.add(result)
      search_queue.append(result)
  checked_bag.add(query)

print(len(container_bags))
