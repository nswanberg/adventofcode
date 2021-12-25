from collections import defaultdict
from types import new_class

with open("14.txt") as f:
    input = f.read()
    template, rulelines = input.split("\n\n")

rules={}
for r in rulelines.splitlines():
    r = r.strip()
    _from, _to = r.split(" -> ")

    rules[_from] = _to

LOOPS = 40

def calculate_string_1(inputstring):
    curstring=template
    nextstring=""
    for _ in range(LOOPS):
        for i in range(len(curstring)-1):
            mid = rules[curstring[i:i+2]]
            nextstring += curstring[i] + mid
        curstring = nextstring + curstring[-1]
        nextstring = ""

        chars = defaultdict(int)
        for c in curstring:
            chars[c] += 1
        nums = sorted(chars.items(), key=lambda x: x[1])
    temppairs=defaultdict(int)
    for i in range(len(curstring)-1):
        temppairs[curstring[i:i+2]] += 1

    return (nums[-1][1] - nums[0][1])

def calculate_string_2(inputstring):
    letter_count = defaultdict(int)
    pairs = defaultdict(int)
    for c in inputstring:
        letter_count[c]+=1
    for i in range(len(inputstring)-1):
        pairs[inputstring[i:i+2]] += 1
    for _ in range(LOOPS):
        next_pairs = defaultdict(int, pairs)
        for pair, count in pairs.items():
            res=rules[pair]
            letter_count[res] += count
            first, second = pair
            next_pairs[first+res] += count
            next_pairs[res+second] += count
            next_pairs[pair] -= count
        pairs = defaultdict(int, {pair: count for pair, count in next_pairs.items() if count > 0})
    
    nums = sorted(letter_count.items(), key=lambda x: x[1])
    return (nums[-1][1] - nums[0][1])


#print(calculate_string_1(template))
print(calculate_string_2(template))

