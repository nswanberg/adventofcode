with open('10.txt') as f:
    lines = f.readlines()


score=0
incomplete_lines=[]
complete_scores = []
for line in lines:
    linescore=0
    stack = []
    for c in line:
        if c in '[{<(':
            stack.append(c)
            continue
        if c in ']}>)':
            p = stack.pop()
            if p+c in '[]{}()<>':
                continue
            if c == ')':
                linescore += 3
            elif c == ']':
                linescore += 57
            elif c == '}':
                linescore += 1197
            elif c == '>':
                linescore += 25137
            else:
                print(c)
                assert False
    if linescore == 0:
        incomplete_lines.append(line)
        print("incomplete stack")
        print(''.join(stack))
        complete_score = 0
        for s in reversed(stack):
            complete_score *= 5
            if s == '(':
                complete_score += 1
            elif s == '[':
                complete_score += 2 
            elif s == '{':
                complete_score += 3
            elif s == '<':
                complete_score += 4
        complete_scores.append(complete_score)
    
print(score)

print(incomplete_lines)
print(complete_scores)
print(sorted(complete_scores)[len(complete_scores)//2])

"""
}}]])})] - 288957 total points.
)}>]}) - 5566 total points.
}}>}>)))) - 1480781 total points.
]]}}]}]}> - 995444 total points.
])}> - 294 total points.
"""


"""
[({(<(())[]>[[{[]{<()<>>}}]])})]
[(()[<>])]({[<{<<[]>>()}>]})
(((({<>}<{<{<>}{[]{[]{}}}>}>))))
{<[[]]>}<{[{[{[]{()[[[]]]}}]}]}>
<{([{{}}[<[[[<>{}]]]>[]]])}>


[({(<(())[]>[[{[]{<()<>> - Complete by adding }}]])})].
[(()[<>])]({[<{<<[]>>( - Complete by adding )}>]}).
(((({<>}<{<{<>}{[]{[]{} - Complete by adding }}>}>)))).
{<[[]]>}<{[{[{[]{()[[[] - Complete by adding ]]}}]}]}>.
<{([{{}}[<[[[<>{}]]]>[]] - Complete by adding ])}>.
"""