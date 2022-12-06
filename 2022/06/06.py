from collections import deque

with open('06.txt') as f:
    input=f.read()
    buf=deque()

    # Part 1
    for i,c in enumerate(input):
        buf.append(c)
        if len(buf) > 4:
            buf.popleft()
        if len(set(buf)) == 4:
            print(i+1)
            break

    # part 2
    for i,c in enumerate(input):
        buf.append(c)
        if len(buf) > 14:
            buf.popleft()
        if len(set(buf)) == 14:
            print(i+1)
            break

