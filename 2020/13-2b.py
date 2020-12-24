def valid(i, list):
	res = {(i + n) % int(list[n]) for n in range(len(list)) if list[n] != 'x'}
	#print('i',i,'list',list,'res',res)
	return len(res) == 1 and 0 in res and list[-1] != 'x'

#input = "17,x,13,19"
#input = "67,7,59,61"                
#input = "67,x,7,59,61"
#input = "67,7,x,59,61"
#input = "1789,37,47,1889"

with open('13.txt') as f:
  input=[l for l in f.read().split('\n') if l]
input=input[1]

input=[i for i in input.split(',')]

timestamp=0
for inp in range(len(input)):
  if input[inp] == 'x':
    print('bypassing ', input[inp])
    continue
  try:
    if inp == 0:
      inc=1
    else:
      for i in range(len(input)):
        if i < inp and input[i] != 'x':
          new_inc = int(input[i])
      print(inc, new_inc)
      inc *= new_inc
    print('inc is now ', inc)
  except:
    print('inc cannot be ', input[i])
    continue
  timestamp += inc
  while not valid(timestamp,input[:inp+1]):
    timestamp+=inc
  
print(timestamp)   
