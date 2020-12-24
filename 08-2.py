import collections
import math
import re
import sys

#with open('08-small.txt') as f:
with open('08.txt') as f:
  input=f.read()

def parse_inst(inst):
	op, val = inst.split(' ')
	val = int(val)
	return (op, val)

instructions = [parse_inst(i) for i in input.split('\n') if i]

#print(instructions)

def eval(instructions):
	cur=0
	acc=0
	exec=set()
	while True:
	  if cur == len(instructions):
	    return acc
	  if cur > len(instructions):
            return -1
	  #print(instructions[cur], cur, acc)
	  op, val = instructions[cur]
	  if cur in exec :
	    #print('breaking on ', cur, exec)
	    break
	  else:
	    exec.add(cur)
	  if op == 'nop':
	    cur+=1
	  elif op == 'acc':
	    acc+=val
	    cur+=1
	  elif op == 'jmp':
	    cur+=val
	  else:
	    print('bad inst ' + op)
	return -1 

for i in range(len(instructions)):

  op,val = instructions[i]
  mod_inst = instructions.copy()
  if op == 'nop':
    mod_inst[i] = ('jmp', val)
  elif op == 'jmp':
    mod_inst[i] = ('nop',val)
  res = eval(mod_inst)
  if res > -1:
    print(i,res)
    break
    
