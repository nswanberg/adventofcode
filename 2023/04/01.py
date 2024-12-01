import re

with open("04.txt") as f:
    total = 0
    for line in f.readlines():
        line = line.strip()
        winners, cards = line.split(" | ")
        # use regexp to remove "Card   N: "
        winners = re.sub(r"Card\s+\d+:\s+", "", winners)
        winners = set([int(n) for n in winners.split(" ") if n])
        cards = set([int(n) for n in cards.split(" ") if n])
        points = 0
        for cards in cards:
            if cards in winners:
                if points == 0:
                    points += 1
                else:
                    points *= 2 
        total += points
    print(total)
