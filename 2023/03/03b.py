from collections import defaultdict
from math import prod

with open("03.txt") as f:
    lines = f.readlines()
    numbers = defaultdict(list)

    for rownum, line in enumerate(lines):
        in_number = False
        active_number_chars = []
        active_number = 0
        number_start = 0
        number_end = 0
        for charnum,c in enumerate(line):
            if c.isdigit():
                if not in_number:
                    in_number = True
                    number_start = charnum
                active_number_chars.append(c)
            else:
                if in_number:
                    in_number = False
                    active_number = int(''.join(active_number_chars))
                    print(f"Found number {active_number} at {number_start} to {charnum}")
                    active_number_chars = []
                    number_end = charnum
                    # search for symbols surrounding number
                    y_start = rownum - 1 if rownum > 0 else rownum
                    y_end = rownum + 2 if rownum + 1 < len(lines) else rownum
                    x_start = number_start - 1 if number_start > 0 else number_start
                    x_end = number_end + 1 if number_end + 1 < len(line) else number_end

                    print(f"At row {rownum}. Checking {active_number} at {y_start} up to but not including {y_end} and {x_start} up to not including {x_end}")
                    for y in range(y_start, y_end):
                        for x in range(x_start, x_end):
                            print(f"Checking {x},{y}: {lines[y][x]}")
                            if lines[y][x] ==  '*':
                                numbers[(x,y)].append(active_number)
                                break
                    print(f"done checking {active_number}")


total = 0

for num_list in numbers.values():
    if len(num_list) > 1:
        total += prod(num_list)

print(total)