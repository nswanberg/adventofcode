with open("01.txt") as f:
    total = 0
    for line in f:
        first = None
        last = 0
        for c in line:
            try:
                i = int(c)
                if first is None:
                    first = i
                last = i
            except:
                pass
        total += first*10 + last
    print(total)
