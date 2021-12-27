with open("15a.txt") as f:
    maplines = f.readlines()
    mp = []
    for line in maplines:
        line = line.strip()
        mp.append(line)


mp=[[8]]

H = len(mp)
W = len(mp[0])

def get_map_val(mp, x, y):
    real_x = x % W
    real_y = y % H
    factor_x = x // W
    factor_y = y // H

    original = int(mp[real_y][real_x]) 

    if factor_y + factor_x == 0:
        return original

    update = (original + factor_x + factor_y)
    if update >= 10:
        return (update % 10) + 1
    return update

for y in range(H*5):
    for x in range(W*5):
        print(get_map_val(mp, x,y), end='')
    print()