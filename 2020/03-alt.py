"""
From a solution on reddit
"""


import math

# lines = open("input", "r").read().splitlines()
# width = len(lines[0])
# answers = []
# for r, d in [[3, 1], [1, 1], [5, 1], [7, 1], [1, 2]]:
#     cnt = 0
#     for i in range(0, len(lines) // d):
#         row, col = i * d, (i * r) % width
#         if lines[row][col] == "#":
#             cnt += 1
#     answers.append(cnt)
# print(answers[0], math.prod(answers))



for i in range(0, 10 // 2):
  print(i, i * 2, i % 3)
