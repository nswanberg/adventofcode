vals={}
for i, x in enumerate("abcdefghijklmnopqrstuvwxyz"):
    vals[x]=i+1
    vals[x.upper()]=i+1+26

with open('03.txt') as f:
    backpacks = f.readlines()

    val = 0
    for b in backpacks:
        b = b.strip()

        first_half, second_half = b[:(len(b)//2)], b[(len(b)//2):]
        first = set(first_half)
        second = set(second_half)
        uniq=first.intersection(second)
        val+= vals[list(uniq)[0]]

    print(val)

    badgevals = 0
    for i in range(0, len(backpacks), 3):
        chars = set()
        group = backpacks[i:i+3]

        g1 = set(group[0].strip())
        g2 = set(group[1].strip())
        g3 = set(group[2].strip())

        badge = g1.intersection(g2.intersection(g3))
        badgevals += vals[list(badge)[0]]


    print(badgevals)




        

