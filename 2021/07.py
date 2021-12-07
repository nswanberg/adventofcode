from statistics import median

with open('07.txt') as f:
    positions = [int(p) for p in f.read().strip().split(',')]

# Pt 1
med = median(positions)

print(sum([abs(med-i) for i in positions]))

# Pt 2
avg = round(sum(positions)/len(positions))
print(f"avg: {avg}")
min = sum([(abs(avg-i)*(abs(avg-i)+1)//2) for i in positions])
pos=0
for n,j in enumerate(range(max(positions))):
    s = sum([(abs(j-i)*(abs(j-i)+1)//2) for i in positions])
    if s < min:
        min = s
        pos=n

print(f"min: {min} pos:{n}")



