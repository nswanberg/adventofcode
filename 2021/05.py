from typing import NamedTuple
import sys

with open('05.txt', 'r') as f:
    textlines = f.readlines()


class Point(NamedTuple):
    x: int
    y: int

class Line(NamedTuple):
    p1: Point
    p2: Point

lines=[]
max_x=0
max_y=0
for line in textlines:
    line = line.strip()
    p1txt, p2txt = line.split(' -> ')
    x1, y1 = p1txt.split(',')
    x2, y2 = p2txt.split(',')
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    if x1 > max_x:
        max_x = x1
    if x2 > max_x:
        max_x = x2
    if y1 > max_y:
        max_y = y1
    if x2 > max_x:
        max_y = y2
   

    line = Line(Point(int(x1),int( y1)), Point(int(x2),(y2)))
    lines.append(line)
    
canvas = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]

def draw_line(line: Line, canvas):
    if line.p1.x == line.p2.x:
        if line.p1.y <= line.p2.y:
            smaller = line.p1.y
            larger = line.p2.y
        else:
            smaller = line.p2.y
            larger = line.p1.y
        n=smaller
        while(n<=larger):
            canvas[n][line.p1.x] += 1
            n+=1
    elif line.p1.y == line.p2.y: 
        if line.p1.x <= line.p2.x:
            smaller = line.p1.x
            larger = line.p2.x
        else:
            smaller = line.p2.x
            larger = line.p1.x
        n=smaller
        while(n<=larger):
            canvas[line.p1.y][n] += 1
            n+=1
    else:
        nx=line.p1.x
        ny=line.p1.y
        while(nx!=line.p2.x and ny!=line.p2.y):
            canvas[ny][nx] += 1
            if line.p1.x < line.p2.x:
                nx+=1
            elif line.p1.x > line.p2.x:
                nx-=1
            if line.p1.y < line.p2.y:
                ny+=1
            elif line.p1.y > line.p2.y:
                ny-=1
        canvas[ny][nx] += 1


for line in lines:
    draw_line(line, canvas)

overlaps=0
for row in canvas:
    for c in row:
        if c >= 2:
            overlaps+=1

print(overlaps)
sys.exit(0)

for row in canvas:
    print(''.join([str(s) if s > 0 else '.' for s in row]))
