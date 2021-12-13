with open('13.txt') as f:
   input = f.read()

dotsinput, foldinput = input.split('\n\n')

folds=[]
for fold in foldinput.split('\n'):
    fold=fold.replace('fold along ','')
    folds.append(fold)

foldaxis,foldpos = folds[0].split('=')
foldpos=int(foldpos)

#print(foldpos)

points=set()
for dotinput in dotsinput.split('\n'):
    x,y = dotinput.split(',')
    points.add((int(x),int(y)))

def get_fold(points, foldaxis, foldpos):
    newpoints=set()
    for point in points:
        foldmax = foldpos * 2
        x,y = point
        if foldaxis == 'x':
            if x > foldpos:
                x = foldmax - x
            newpoints.add((x,y))
        else:
            if y > foldpos:
                y = foldmax - y
            newpoints.add((x,y))
    return newpoints

lastxpos = -1
lastypos = -1
for fold in folds[:]:
    foldaxis,foldpos = fold.split('=')
    foldpos=int(foldpos)
    if foldaxis == 'x':
        lastxpos = foldpos
    else:
        lastypos = foldpos
    points = get_fold(points, foldaxis, foldpos)
    print(len(points))

    maxxpos = lastxpos
    maxypos = lastypos

    for i in range(maxypos+1):
        for j in range(maxxpos+1):
            if (j,i) in points:
                print('#',end='')
            else:
                print('.',end='')
        print()
    print()

