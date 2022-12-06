"""    [D]    
    [N] [C]    
    [Z] [M] [P]
     1   2   3 

     move 1 from 2 to 1
     move 3 from 1 to 3
     move 2 from 2 to 1
     move 1 from 1 to 2
"""

from copy import deepcopy


input = ""


def transpose(list_of_lists):
    transposed = []
    for i in range(len(list_of_lists[0])):
        row = list()
        for sublist in list_of_lists:
            row.append(sublist[i])
        transposed.append(row)
    return transposed

with open("05.txt") as f:
    lines = f.read()
    crates, instructions = lines.split("\n\n")
    cratelines = crates.split('\n')[::-1]

    cols1 = {int(i):[] for i in cratelines[0].split()}
    cols2 = deepcopy(cols1)

    cratelines = transpose(cratelines[1:])

    filtered = [line for line in cratelines if str.isalpha(line[0])]

    for i,line in enumerate(filtered):
        for c in line:
            if c != ' ':
                cols1[i+1].append(c)
                cols2[i+1].append(c)

    for inst in instructions.split('\n'):
        _, q, _, source, _, dest = inst.split(' ')
        q = int(q)
        source = int(source)
        dest = int(dest)

        """
        print(cols)
        print('----')
        print(f"moving {q} from {source} to {dest}")
        print(cols[source][-q:])
        print(cols[source][:-q])
        print('---')
        print(cols)
        """

        for _ in range(q):
            cols1[dest].append(cols1[source].pop())

        cols2[dest].extend(cols2[source][-q:])
        cols2[source] = cols2[source][:-q]


    tops = []
    for k,v in cols1.items():
        tops += v[-1]
    print(''.join(tops))


    tops2 = []
    for k,v in cols2.items():
        tops2 += v[-1]
    print(''.join(tops2))


