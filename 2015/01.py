with open('01.txt') as f:
    parens = f.read()

    floor=0 
    for i,p in enumerate(parens):
        if p == '(':
            floor+=1
        elif p == ')':
            floor-=1
        else:
            pass
        if floor==-1:
            print("floor",i+1)
    print(floor)
