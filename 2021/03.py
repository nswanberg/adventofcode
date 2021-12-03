from collections import defaultdict

with open('03.txt') as f:
    lines = f.readlines()

gamma=0
epsilon=0

values=defaultdict(int)

for line in lines:
    nums = [int(c) for c in line.strip()]
    for i,n in enumerate(nums):
        values[(i,n)]+=1

result=[]
for i in range(len(lines[0].strip())): 
    zeros = values[(i,0)]
    ones  = values[(i,1)]

    print(ones,zeros)

    if zeros > ones:
        result.append(0)
    else:
        result.append(1)

inverse = []
for i in result:
    if i == 0:
        inverse.append(1)
    else:
        inverse.append(0)

resultnum=0
for i,n in enumerate(result[::-1]):
    resultnum+=n*2**i

print(resultnum)

inverseresultnum=0
for i,n in enumerate(inverse[::-1]):
    inverseresultnum+=n*2**i

print(inverseresultnum)

print(resultnum*inverseresultnum)




## Part 2

candidates=[]
for line in lines:
   candidates.append([int(n) for n in line.strip()])

 
for i in range(len(candidates[0])):
    ones=0
    zeros=0
    nextcandidates=[]
    for c in candidates:
        if c[i] == 0:
            zeros+=1
        else:
            ones+=1
    if zeros > ones:
        comp = 0
    else:
        comp = 1
    print(i,comp)
    for c in candidates:
        if c[i] == comp:
            nextcandidates.append(c)
    candidates=nextcandidates[:]

resultnum=0
for i,n in enumerate(candidates[0][::-1]):
    resultnum+=n*2**i

print(resultnum)


candidates=[]
for line in lines:
   candidates.append([int(n) for n in line.strip()])


for i in range(len(candidates[0])):
    ones=0
    zeros=0
    nextcandidates=[]
    for c in candidates:
        if c[i] == 0:
            zeros+=1
        else:
            ones+=1
    if ones < zeros:
        comp = 1 
    else:
        comp = 0 
    print(i,comp)
    for c in candidates:
        if c[i] == comp:
            nextcandidates.append(c)
    candidates=nextcandidates[:]
    if len(candidates) == 1:
        break

resultnum2=0
for i,n in enumerate(candidates[0][::-1]):
    resultnum2+=n*2**i


print(resultnum*resultnum2)
