from copy import deepcopy
import collections
import math
import re
import sys

with open('18.txt') as f:
  input=[l for l in f.read().strip().splitlines() if l]

#testinput="1 + 2 * 3 + 4 * 5 + 6"
testinput="1 + (2 * 3) + (4 * (5 + 6))"


def eval(inputstring):
	ops = list(inputstring.replace(' ',''))
	#print(ops)
	i=0
	#opstate f o s
	opstate='f'
	op=None
	opstack=[]
	total=0
	while i<len(ops):
	 #print('total', total, 'i', i, 'ops[i]', ops[i], 'opstate', opstate, 'op', op, 'opstack', opstack)
	 # regular case
	 if opstate == 'f':
	   #print('looking for first')
	   nextop = ops[i]
	   if nextop == '(':
	     opstack.append((None,total))
	     opstate='f'
	     total=0
	   else:
	     total=int(ops[i])
	     opstate='o'
	 elif opstate == 'o':
	   #print('looking for operator')
	   nextop = ops[i]
	   if nextop == ')':
	     op, prevtotal = opstack.pop() 
	     if op == None or op == '+':
	       total += prevtotal
	     elif op == '*':
	       total *= prevtotal
	     #opstate = 'o'
	     op=None
	   else:
	     op = nextop
	     opstate='s'
	 elif opstate == 's':
	   #print('looking for operand')
	   nextop = ops[i]
	   if nextop == '(':
	     opstack.append((op,total))
	     total=0
	     op=None
	     opstate='f'
	   else:
	     if op == '+':
	       total += int(ops[i])
	       opstate='o'
	     if op == '*':
	       #print('multiplying', total, ops[i])
	       total *= int(ops[i])
	       opstate='o'
	 #print('total', total, 'i', i, 'ops[i]', ops[i], 'opstate', opstate, 'op', op, 'opstack', opstack)
	 #print('--')
	 i+=1
	return total

#print(sum([eval(s) for s in input]))

def lexer(inputstring):
  return list(inputstring.replace(' ',''))

def eval2(inputstring):
  tokens=lexer(inputstring)
  opstack=[]
  numstack=[]
  

eval2("1 + 2 * 3 + 4 * 5 + 6")
