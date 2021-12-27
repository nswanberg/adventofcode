from collections import defaultdict
import heapq

with open("15.txt") as f:
    maplines = f.readlines()
    mp = []
    for line in maplines:
        line = line.strip()
        mp.append(line)
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

def get_neighbors(mp, pos):
    """ Returns a tuple containing the cost for each possible pos"""
    cur_x, cur_y = pos
    possible = [(cur_x + dx, cur_y + dy) for dx, dy in  [(0,-1),(1,0),(0,1),(-1,0)]]

    return [(get_map_val(mp, new_x, new_y), (new_x, new_y)) for new_x, new_y in possible if 0 <= new_x < len(mp[0])*5 and 0 <= new_y < len(mp)*5]

def Hs(start, finish):
    start_x, start_y = start
    finish_x, finish_y = finish
    return abs(start_x - finish_x) + abs(start_y - finish_y)

def dij(mp, start, finish):
    visited=set()
    start_cost = 0
    Q = [(start_cost,start)]
    heapq.heapify(Q)
    g_score=defaultdict(lambda: float('inf'))
    g_score[start] = 0
    while Q:
        cur_cost, cur_pos = heapq.heappop(Q)
        if cur_pos in visited:
            continue
        visited.add(cur_pos)
        if cur_pos == finish:
            if False:
                for y in range(H):
                    for x in range(W):
                        print(f"{g_score[(x,y)]:3}", end='')
                    print("")
                for y in range(H):
                    for x in range(W):
                        print(f"{mp[y][x]:>3}", end='')
                    print("")
            return cur_cost
        for new_cost, new_pos in get_neighbors(mp, cur_pos):
            temp_cost = cur_cost + new_cost
            if temp_cost < g_score[new_pos]:
                g_score[new_pos] = temp_cost
                if new_pos not in visited:
                    heapq.heappush(Q, (temp_cost, new_pos))
    return -1 # not possible
        
print(dij(mp, (0,0), ((W*5)-1, (H*5)-1)))