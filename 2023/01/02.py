number_words = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9
}

with open("01.txt") as f:
    total = 0
    for line in f:
        first = None
        last = 0
        n = None
        for i,c in enumerate(line):
            if c in "0123456789":
                n = int(c)
            else:
                for word in number_words:
                    #print(line[i:i+len(word)])
                    if line[i:i+len(word)] == word:
                        print(f"Found {word}")
                        n = number_words[word]
            print(n)
            if first is None and n is not None:
                first = n
            last = n
        print (first, last)
        total += first*10 + last
    print(total)
