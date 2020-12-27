from collections import defaultdict

with open('21.txt') as f:
  input = f.read()

foods = input.strip().splitlines()

allingredients=defaultdict(int)
allallergens=defaultdict(set)
for food in foods:
  ingredientstext, allergenstext = food.replace(')','').replace(',','').split(' (contains ')
  ingredients = ingredientstext.split(' ')
  allergens = allergenstext.split(' ')
  #print(allergens)
  #print(ingredients)
  # append allergens listed in this food to each ingredient
  for i in ingredients:
    allingredients[i]+=1
  for a in allergens:
    if len(allallergens[a]) == 0:
      allallergens[a].update(ingredients)
    else:
      removals=[]
      for i in allallergens[a]:
        if i not in ingredients:
          removals.append(i)
      for r in removals:
        allallergens[a].remove(r)

print('allergens')
for a in allallergens.keys():
  print(a, allallergens[a])
known=set()
for v in allallergens.values():
  known.update(v)
for k in known:
  allingredients.pop(k)
print(sum(allingredients.values()))

# part 2

knowningredients={}
while max([len(a) for a in allallergens.values()]) > 1:
  print(knowningredients)  
  print(allallergens)
  for a in allallergens.keys():
    if a in knowningredients.keys():
      continue
    if len(allallergens[a]) == 1:
      knowningredients[a]=list(allallergens[a])[0]
      continue
    removals=[]
    for i in allallergens[a]:
      if i in knowningredients.values():
        removals.append(i)
    for r in removals:
      allallergens[a].remove(r)
    if len(allallergens[a]) == 1:
      knowningredients[a]=list(allallergens[a])[0]
      continue

knownkeys=list(knowningredients.keys())
knownkeys.sort()
known=[]
for k in knownkeys:
  known.append(knowningredients[k])
print(','.join(known))  
