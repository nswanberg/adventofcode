with open('01.txt') as f:
    lines = f.readlines()

prev = None
increase = 0
for i in lines:
    i = int(i)
    if prev and i > prev:
        increase+=1
    prev=i

print(increase)




prev = None
increase = 0
num_lines = [int(i) for i in lines]
for i in range(len(num_lines)-2):
    n = sum(num_lines[i:i+3])
    if prev and n > prev:
        increase += 1
    prev = n

print(increase)

