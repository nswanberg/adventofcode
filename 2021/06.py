from collections import defaultdict

fishes = defaultdict(int)
with open('06.txt') as f:
    fishstring = f.read().strip().split(',')
    for i in range(9):
        fishes[i]=0
    for f in sorted(fishstring):
        fishes[int(f)]+=1


for d in range(256):
    tempfishes=defaultdict(int)
    for k in range(9):
        if k > 0:
            tempfishes[k-1] += fishes[k]
        else:
            tempfishes[6] += fishes[0]
            tempfishes[8] += fishes[0]
    fishes=tempfishes.copy()

print(sum(fishes.values()))
