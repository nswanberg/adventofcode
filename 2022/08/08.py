import pprint

with open('08.txt') as f:
    lines = f.readlines()
    trees = []
    visible = []
    for line in lines:
        tree_row = []
        visible_row = []
        line = line.strip()
        for l in line:
            tree_row.append(int(l))
            visible_row.append(0)
        trees.append(tree_row)
        visible.append(visible_row)

    #pprint.pprint(trees)
    visible_count = 0
    H = len(trees)
    W = len(trees[0])

    for i in range(H):
        max_t = -1
        for j in range(W):
            if trees[i][j] > max_t:
                max_t = trees[i][j]
                visible[i][j] = 1

    for i in range(H):
        max_t = -1
        for j in range(W)[::-1]:
            if trees[i][j] > max_t:
                max_t = trees[i][j]
                visible[i][j] = 1

    for j in range(W):
        max_t = -1
        for i in range(H):
            if trees[i][j] > max_t:
                max_t = trees[i][j]
                visible[i][j] = 1

    for j in range(W):
        max_t = -1
        for i in range(H)[::-1]:
            if trees[i][j] > max_t:
                max_t = trees[i][j]
                visible[i][j] = 1

    #pprint.pprint(visible)

    total = 0
    for i in visible:
        for j in i:
            total += j

    print(total)

    
    max_score = 0

    def get_score_left(pos, trees):
        x,y = pos
        comp = trees[y][x]
        i=x-1
        score=0
        while i > -1:
            score+=1
            v = trees[y][i]
            if comp <= v:
                break
            i-=1
        #print(f"{pos} left  {score}")
        return score

    def get_score_right(pos, trees):
        x,y = pos
        comp = trees[y][x]
        i=x+1
        score=0
        while i < len(trees[0]):
            score+=1
            v = trees[y][i]
            if comp <= v:
                break
            i+=1
        #print(f"{pos} right {score}")
        return score

    def get_score_up(pos, trees):
        x,y = pos
        comp = trees[y][x]
        i=y-1
        score=0
        while i > -1:
            score+=1
            v = trees[i][x]
            #print(f"i:{i} comparing v:{v} to comp: {comp}")
            if comp <= v:
                break
            i-=1
        #print(f"{pos} up    {score}")
        return score

    def get_score_down(pos, trees):
        x,y = pos
        comp = trees[y][x]
        i=y+1
        score=0
        while i < len(trees):
            score+=1
            v = trees[i][x]
            if comp <= v:
                break
            i+=1
        #print(f"{pos} down  {score}")
        return score

    for y in range(1,H-1):
        for x in range(1,W-1):
            #print(f"checking {(x,y)}, {trees[y][x]}")
            score = (
                    get_score_left((x,y), trees) * 
                    get_score_right((x,y), trees) *
                    get_score_up((x,y), trees) *
                    get_score_down((x,y), trees) )
            #print(f"score is {score}")
            if score > max_score:
                max_score = score

    print(max_score)

