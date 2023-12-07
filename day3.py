'''
2023 Advent of Code - Day 03: Gear Ratios
(https://adventofcode.com/2023/day/3)
From input (the schematic), numbers adjacent to a symbol are "part numbers".
Periods (.) are empty spaces and do not count as symbols.
Return sum of all "part numbers".
'''

import re

with open("test3.txt") as fin:
    schematic = [line.strip() for line in fin]

# Search for groups of numbers and save coords for each digit
num_coords = []
# sym_coords = {}
adj_nums = []
search_group = []
adj = [(k, l) for k in (-1, 0, 1)
              for l in (-1, 0, 1) if k != 0 or l != 0]

for row, line in enumerate(schematic):
    num_collector = re.finditer(r'\d+', line)
    for num_match in num_collector:
        digit_coords = []
        span = num_match.span()

        # start = span[0], end = span[1]
        for i in range(span[1] - span[0]):
            digit_coords.append((row, span[0] + i))
        num_coords.append([num_match.group(), digit_coords])

    sym_collector = re.finditer(r'[^.\d]', line)
    for sym_match in sym_collector:
        for pair in [(row + r, sym_match.start() + c) for r, c in adj]:
            search_group.append(pair)
        # sym_coords[(row, sym_match.start())] = sym_match.group()

for group in num_coords:
    for coord in group[1]:
        if coord in search_group:
            adj_nums.append(int(group[0]))
            break

# print('adj', adj_nums)
print('sum', sum(adj_nums))
