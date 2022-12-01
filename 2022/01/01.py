with open('01.txt') as f:
    lines = f.readlines()

    elves=[]
    total = 0
    for line in lines:
        line = line.strip()
        if line:
            total += int(line)
        else:
            elves.append(total)
            total = 0
    print(max(elves))

    print(sum(sorted(elves)[-3:]))

