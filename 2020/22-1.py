smallinput = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

with open('22.txt') as f:
  input = f.read()

player1, player2 = input.strip().split('\n\n')

player1 = [int(i) for i in player1.splitlines()[1:]]
player2 = [int(i) for i in player2.splitlines()[1:]]

while len(player1) and len(player2):
  p1 = player1.pop(0)
  p2 = player2.pop(0)
  if p1 > p2:
    player1.extend([p1,p2])
  else:
    player2.extend([p2,p1])

if len(player1):
  print('player 1')
  score = player1
else:
  score = player2

print(score)

acc=0
for i, n in enumerate(reversed(score)):
  acc+= (i+1) * n 

print(acc)
