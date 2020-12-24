from collections import defaultdict

with open('21-small.txt') as f:
  input = f.read()

foods = input.strip().splitlines()

allingredients=set()
candidates=defaultdict(list)
allallergens=defaultdict(set)
pairs=defaultdict(int)
options=defaultdict(int)
for food in foods:
  ingredientstext, allergenstext = food.replace(')','').replace(',','').split(' (contains ')
  ingredients = ingredientstext.split(' ')
  allergens = allergenstext.split(' ')
  for i in ingredients:
    allingredients.add(i)
    candidates[i].append(tuple(allergens))
    options[(tuple(allergens),i)]+=1
    for a in allergens:
      allallergens[a].add(i)
      pairs[(a,i)]+=1
  if len(a) == 1:
    removelist=[]
    for i in allergens[a]:
      if i not in ingredients:
        removelist.append(i)
    for r in removelist:
      allergens[a].remove(r)

#print(allingredients)
#for c in candidates:
#  print(c, candidates[c])
#for p in pairs:
#  print(p, pairs[p])
#print('allallergens',allallergens)
for o in options:
  print(o, options[o])
