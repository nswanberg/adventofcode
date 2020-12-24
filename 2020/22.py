from collections import defaultdict

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

def checkdeck(deck):
  for i, _ in enumerate(deck):
    if (i+1) not in deck:
      return False
  return True

decksize=len(player1+player2)
assert checkdeck(player1+player2)

gamecount=0

def play_2(player1, player2, depth):
  
  if depth == 0:
    assert checkdeck(player1+player2)
  indent = depth * ' '
  #print(indent,'depth: ', depth)
  depth+=1
  rounds=defaultdict(int)
  r=0
  assert player1 and player2
  while player1 and player2:
    # memoize round
    round = (tuple(player1),tuple(player2))
    if rounds[round] >= 1:
      assert r > 0
      #print(indent,'automatic winner',r)
      return (1,player1)
    rounds[round]=1

    #print(indent,'player1', player1)
    #print(indent,'player2', player2)

    p1 = player1.pop(0)
    p2 = player2.pop(0)
   
    if p1 <= len(player1) and p2 <= len(player2):
      #print(indent,'starting subgame', p1, len(player1), p2, len(player2))
      winner, _ = play_2(player1[:p1],player2[:p2],depth)
   
      if winner == 1: 
        player1.extend([p1,p2])
        #print(indent,'player 1 won sub')
      elif winner == 2:
        player2.extend([p2,p1])
        #print(indent,'player 2 won sub')
      else:
        assert False

    elif p1 > len(player1) or p2 > len(player2):
     
      if p1 > p2:
        player1.extend([p1,p2])
        #print(indent,'player 1 won ', [p1,p2])
      else:
        player2.extend([p2,p1])
        #print(indent,'player 2 won ', [p2,p1])

    else:
      assert False
    r+=1
  
  if player1:
    return (1, player1) 
  elif player2: 
    return (2, player2) 
  else:
    assert False

winner, score = play_2(player1, player2,0)

assert len(score) == decksize
assert checkdeck(score)

acc=0
for i, n in enumerate(reversed(score)):
  acc+= (i+1) * n 

print(score)
print(winner)
print(acc)
