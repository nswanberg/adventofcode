import re

testinput = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

with open('19.txt') as f:
  input=f.read()

#part 2 replace
input = input.replace('8: 42', '8: 42 | 42 8').replace('11: 42 31','11: 42 31 | 42 11 31')


rules, inputlines = input.strip().split('\n\n')

ruledict={}
for rule in rules.splitlines():
  num, evals = rule.split(':')
  num = int(num)
  evals = evals.strip().replace('"','')
  if "|" in evals:
    evals = '( '+evals+' )'
  ruledict[num] = evals

#print(ruledict)

#print(ruledict[0])


print(max([len(r) for r in inputlines.strip().splitlines()]))


reg=None
loops = 0
#part 1
#while re.search("\d+",ruledict[0]):
while loops < 10:
  for i in reversed(range(len(ruledict.keys()))):
    eval = ruledict[i]
    #print('reviewing eval ',eval)
    eval_list = [r for r in eval.split(' ')]
    #print('eval_list',eval_list)
    for j in range(len(eval_list)):
      if eval_list[j] in "()|ab":
        #print('found a ()|')
        continue
      eval_list[j] = ruledict[int(eval_list[j])]
    #print('new eval list', eval_list)
    ruledict[i] = ' '.join(eval_list)
    if i == 0:
      #print('final eval list', ''.join(eval_list))
      reg = '^' + ''.join(eval_list) + '$'

  reg = reg.replace(' ','')
  #print(reg)
 
  # part2 repeat this section 
  matchcount=0
  for line in inputlines.strip().splitlines():
    if re.match(reg,line):
      matchcount+=1
  print(matchcount)
  loops += 1
