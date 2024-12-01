import re
from collections import defaultdict, deque

with open("04.txt") as f:
    total_cards = 0
    all_cards = dict()
    plays_for_card = defaultdict(int)
    # first load all cards, and each will be played once
    for i, line in enumerate(f.readlines()):
        cardnum = i + 1
        line = line.strip()
        winners, cards = line.split(" | ")
        # use regexp to remove "Card   N: "
        winners = re.sub(r"Card\s+\d+:\s+", "", winners)
        winners = set([int(n) for n in winners.split(" ") if n])
        cards = set([int(n) for n in cards.split(" ") if n])
        all_cards[cardnum] = (winners, cards)
        plays_for_card[cardnum] += 1
        total_cards += 1
    for cardnum in range(1, max(all_cards.keys())):
        for plays in range(plays_for_card[cardnum]):
            #print(f"Playing card {cardnum} for the {plays + 1}th time")
            points = 0
            current_winners, current_card_numbers = all_cards[cardnum]
            for c in current_card_numbers:
                if c in current_winners:
                    points += 1
            total_cards += points
            for next_play in range(cardnum + 1, cardnum + 1 + points):
                #print(f"Adding card {next_play} to the deck")
                plays_for_card[next_play] += 1
    print(total_cards)
