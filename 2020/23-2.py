"""
TODO

create a reference in each cup to the cup whose label is one less
update the desination algorithm to go straight to the destination
deal with the case where the destination is in pickups
"""


testinput = "389125467"
input = "253149867"

def input_to_ints(input):
  return [int(c) for c in input]

ints = input_to_ints(input)

def printfrom1(current):
  acc = ""
  temp = current
  while temp.num != 1:
    temp = temp.next
  one = temp
  temp = one.next
  while temp != one:
    acc += str(temp.num)
    temp = temp.next
  return acc

class Cup:
  def  __init__(self, num):
    self.num = num
    self.next = None
    self.lesser = None

def make_cups(ints, n):
  zeroCup = Cup(0)
  prevCup = zeroCup
  # initialize first cups
  for i in range(1,max(ints)+1):
    cup = Cup(i)
    cup.lesser = prevCup
    prevCup.next = cup
    prevCup = cup

  # drop zeroCup
  oneCup = zeroCup.next
  prevCup.next = oneCup
  oneCup.lesser = prevCup

  #print('cups: ', printfrom1(oneCup))
  temp = oneCup.next
  while temp.next != oneCup:
    #print('num: ', temp.num, 'lesser: ', temp.lesser.num)
    temp = temp.next
 
  # order first cups 
  firstCup = None
  maxCup = prevCup
  #print('maxCup: ', maxCup.num)
  prevCup = None
  assert maxCup
  for i in ints:
    temp = maxCup
    while temp and temp.num != i:
      #print(i, temp.num)
      temp = temp.lesser
    if not firstCup:
      firstCup = temp
      prevCup = firstCup
      print('firstCup: ', firstCup.num)
    else:
      prevCup.next = temp
      print('linking ', prevCup.num, ' to ', temp.num)
      prevCup = temp

  temp.next = firstCup
  
  print('ordereed cups: ', printfrom1(oneCup))

  temp = firstCup
  i=0
  while i < 11:
    print(temp.num, temp.lesser.num, temp.next.num)
    temp = temp.next
    i+=1
 
  if n <= len(ints) - 1:
    return firstCup 
    
  nums = [i for i in range(len(ints)+1, n+1)]
  first = True
  for i in nums:
    cup = Cup(i)
    if first: # should be 10
      cup.lesser = maxCup
      first = False
    else:
      cup.lesser = prevCup
    prevCup.next = cup
    prevCup = cup
  prevCup.next = firstCup 
  oneCup.lesser = prevCup
  return firstCup 

#highest=9
highest=1000000
current = make_cups(ints, highest)
i=0
temp = current
"""
while i <= 22:
  print('current: ',temp.num)
  print('lesser: ', temp.lesser.num)
  temp=temp.next
  i+=1
print(' all list ')
"""
destination = None
"""
print('oneCup', temp.num)
print('oneCup.next', temp.next.num)
print('oneCup.lesser', temp.lesser.num)
"""

temp = current
while temp.num != 1:
  temp = temp.next
one = temp

i=1
while i <=highest * 10 :
#while i <= 100:
  #print('move: ', i, printfrom1(current))
  if i % 100000 == 0:
    print(i)
  # slice out pickups
  pickup = current.next
  lastPickup = pickup.next.next
  pickups=[pickup.num, pickup.next.num, pickup.next.next.num]
  current.next = lastPickup.next

  # find dest val
  destination = current.lesser
  assert destination
  while destination == pickup or destination == pickup.next or destination == pickup.next.next:
    destination = destination.lesser
  #print('current: ', current.num, 'pickups: ',pickups, 'destination: ', destination.num)

  rest = destination.next
  destination.next = pickup
  lastPickup.next = rest

  current = current.next

  # place dest val 
  i+=1

#print(printfrom1(one))

print(one.next.num * one.next.next.num)
