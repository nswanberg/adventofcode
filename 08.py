import collections
import math
import re
import sys

#with open('08-small.txt') as f:
with open('08.txt') as f:
  input=f.read()

instructions = [i for i in input.split('\n') if i]

print(instructions)

cur=0
acc=0
exec=set()
while True:
  print(instructions[cur], cur, acc)
  op, val = instructions[cur].split(' ')
  val = int(val)
  if cur in exec:
    print('breaking on ', cur, exec)
    break
  else:
    exec.add(cur)
  if op == 'nop':
    cur+=1
  elif op == 'acc':
    acc+=val
    cur+=1
  elif op == 'jmp':
    cur+=(val)
  else:
    print('bad inst ' + op)

print(acc)
 
