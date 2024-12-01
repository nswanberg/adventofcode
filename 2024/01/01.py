from collections import defaultdict 

with open("01.txt") as f:
    lines = f.readlines()

leftints=[]
rightints=[]


for line in lines:
    left, right = line.split()
    leftints.append(int(left))
    rightints.append(int(right))

diffs = []

leftints = sorted(leftints)
rightints = sorted(rightints)

for i in range(len(leftints)):
    #print(leftints[i])
    #print(rightints[i])
    #print(f"Diff: {abs(leftints[i] - rightints[i])}")
    diffs.append(abs(leftints[i] - rightints[i]))
print(sum(diffs))


rightcounts=defaultdict(int)

for i in rightints:
    rightcounts[i]+=1

print(sum([i * rightcounts[i] for i in leftints]))
