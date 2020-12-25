testinput = "389125467"
input = "253149867"

def input_to_ints(input):
  return [int(c) for c in input]

ints = input_to_ints(testinput)

class Cup:
  def  __init__(self, num):
    self.num = num
    self.next = None

def make_cups(ints, n):
  prevCup = Cup(-1)
  firstCup = prevCup
  nums = ints + [i for i in range(len(ints)+1, n+1)]
  #print(nums)
  for i in nums:
    cup = Cup(i)
    prevCup.next = cup
    prevCup = cup
  prevCup.next = firstCup.next
  return firstCup

highest=10000
current = make_cups(ints, highest)
# drop the first placeholder cup (was -1)
current = current.next
destination = None

temp = current
while temp.num != 1:
  temp = temp.next
one = temp

i=1
while i <=highest * 10 :
  if i % 10000 == 0:
    print(i)
  # slice out pickups
  pickup = current.next
  lastPickup = pickup.next.next
  pickups=[pickup.num, pickup.next.num, pickup.next.next.num]
  current.next = lastPickup.next

  # find dest val
  destVal = current.num - 1
  #print('pickups', pickups, 'destVal', destVal)
  while destVal in pickups or destVal == 0:
    destVal -= 1
    if destVal <= 0:
      destVal = highest 
  #print('got destval', destVal)

  destination=lastPickup.next
  while destination.num != destVal:
    #print('destination.num', destination.num, 'destVal', destVal, 'pickups', pickups)
    destination = destination.next

  rest = destination.next
  destination.next = pickup
  lastPickup.next = rest

  current = current.next

  # place dest val 
  i+=1

print(one.next.num * one.next.next.num)
