import functools
from collections import defaultdict

with open('08.txt') as f:
    lines = f.readlines()

uniques = defaultdict(int)
total=0
for line in lines:
    line = line.strip()
    signals,output = line.split(' | ')
   
    numbers = defaultdict(set)
    for o in output.split():
        uniques[len(o)] += 1

    numbers = defaultdict(set)
    unknown = defaultdict(set)
    for s in signals.split():
        numbers[len(s)].update(*s)
        unknown[len(s)].add(s)
    
    ssd={}

    one=set(numbers[2])
    seven=set(numbers[3])
    four=set(numbers[4])
    eight=set(numbers[7])


    # Characters
    # zero   6
    # one    2
    # two    5
    # three  5
    # four   4
    # five   5
    # six    6
    # seven  3
    # eight  7
    # nine   6

    """
    print(one)
    print(seven)
    print(four)
    print(eight)
    """
   
    ssd['a']=seven-one
    unique_to_five_seg = functools.reduce( lambda a, b: a.intersection(b), [set(x) for x in  unknown[5]])
    ssd['g']=unique_to_five_seg - seven.union(four)
    ssd['e']=eight-seven.union(four)-ssd['g']
    ssd['d']=unique_to_five_seg - ssd['a'].union(ssd['g'])
    ssd['b']=four-one.union(ssd['d'])
    segments_in_five = ssd['a'].union(ssd['b']).union(ssd['d']).union(ssd['g'])
    unique_to_five = [set(x) - segments_in_five  for x in  unknown[5] if segments_in_five.issubset(x)][0]
    ssd['f']=unique_to_five
    ssd['c']=one-unique_to_five


    """
    print([x for x in numbers[5]])
    print("*****")
    print([set(set(x) - four.union(seven)) for x in unknown[5]])
    print([set(set(x) - four.union(seven)) for x in unknown[6]])
    print(functools.reduce( lambda a, b: a.intersection(b), [set(x) for x in  unknown[6]]))


    print(ssd)
    """


    zero=''.join(sorted([s for s in ssd['a'].union(ssd['b'],ssd['c'],ssd['e'],ssd['f'],ssd['g'])]))
    one=''.join(sorted(one))
    two=''.join(sorted([s for s in ssd['a'].union(ssd['c'],ssd['d'],ssd['e'],ssd['g'])]))
    three=''.join(sorted([s for s in ssd['a'].union(ssd['c'],ssd['d'],ssd['f'],ssd['g'])]))
    four=''.join(sorted(four))
    five=''.join(sorted([s for s in ssd['a'].union(ssd['b'],ssd['d'],ssd['f'],ssd['g'])]))
    six=''.join(sorted([s for s in ssd['a'].union(ssd['b'],ssd['d'],ssd['e'],ssd['f'],ssd['g'])]))
    seven=''.join(sorted(seven))
    eight=''.join(sorted(eight))
    nine=''.join(sorted([s for s in ssd['a'].union(ssd['b'],ssd['c'],ssd['d'],ssd['f'],ssd['g'])]))

    digits={}

    digits[zero]=0
    digits[one]=1
    digits[two]=2
    digits[three]=3
    digits[four]=4
    digits[five]=5
    digits[six]=6
    digits[seven]=7
    digits[eight]=8
    digits[nine]=9

    val = 0
    print(output)
    for i,o in enumerate(reversed(output.split())):
        o = ''.join(sorted(o))
        val += digits[o] * 10**i

    total += val



print(uniques[2]+uniques[4]+uniques[3]+uniques[7])


print(total)


