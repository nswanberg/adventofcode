def loop(initial, subject):
  initial*=subject
  return initial % 20201227

doorpub = 11404017
cardpub = 13768789
"""
cardpub = 5764801
doorpub = 17807724
"""
i=0
card=1
door=1
doorresult=None
cardresult=None
while doorresult == None or cardresult == None: 
  i+=1
  card = loop(card, 7)
  door = loop(door, 7)
  if card == cardpub:
    cardresult = i
  if door == doorpub:
    doorresult = i
    print('door', i)

print(cardresult, doorresult)

i = 0
door = 1
while i < doorresult:
  door = loop(door, cardpub)
  i+=1

print(door)
