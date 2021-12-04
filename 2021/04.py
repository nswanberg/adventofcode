with open('04.txt') as f:
    lines = f.read()

items =  lines.split('\n\n')

draws = [int(n) for n in items[0].split(',')]
boards = []
for board_lines in items[1:]:
  board=[]
  for line in board_lines.strip().split('\n'):
    board.append([int(n) for n in line.split(' ') if n != ''])

  transposed = list(map(list, zip(*board)))
  boards.append((board, transposed))

def search_board(latest, draws, board):
   d = set(draws)
   for row in board:
       s = set(row)
       if s.issubset(d):
           unpicked = []
           for row in board:
               for c in row:
                   if c not in d:
                       unpicked.append(c)
           print(f"board won with {latest}")
           print(board)
           print(sum(unpicked)*latest)
           return True

   return False

sofar=[]
for n in draws:
    unpicked=[]
    sofar.append(n)
    if len(sofar) >= 5:
        print(f"checking {n}, boards {len(boards)}")
        for board in boards:
            b, t = board
            pb = search_board(n, sofar,b)
            pt = search_board(n, sofar,t)
            if not pb and not pt:
                unpicked.append(board)
        boards = unpicked


