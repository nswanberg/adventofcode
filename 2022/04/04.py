with open('input.txt') as f:
    lines = f.readlines()
    contains = 0
    for line in lines:
        line = line.strip()
        range1,range2=line.split(',')
        X = tuple(int(x) for x in range1.split('-'))
        Y = tuple(int(x) for x in range2.split('-'))
        if X[0] <= Y[0] and X[1] >= Y[1]:
            contains += 1
        elif Y[0] <= X[0] and Y[1] >= X[1]:
            contains += 1

    print(contains)

    overlaps = 0
    for line in lines:
        line = line.strip()
        range1,range2=line.split(',')
        X = tuple(int(x) for x in range1.split('-'))
        Y = tuple(int(x) for x in range2.split('-'))
        if X[0] <= Y[1] and X[1] >= Y[0]:
            overlaps += 1
        elif Y[0] <= X[1] and Y[1] >= X[0]:
            overlaps += 1

    print(overlaps)

