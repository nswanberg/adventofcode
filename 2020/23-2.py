testinput = "389125467"
input = "253149867"

def input_to_ints(input):
  return [int(c) for c in input]

ints = input_to_ints(input)

def make_cups(ints, n):
  return ints + [i for i in range(len(ints)+1, n+1)]

cups = make_cups(ints, 20)

print(cups)

