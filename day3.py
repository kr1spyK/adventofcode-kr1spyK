'''
2023 Advent of Code - Day 03: Gear Ratios
(https://adventofcode.com/2023/day/3)
From input (the schematic), numbers adjacent to a symbol are "part numbers".
Periods (.) are empty spaces and do not count as symbols.
Return sum of all "part numbers".
'''

import re, math

with open("input3.txt") as fin:
    schematic = [line.strip() for line in fin]

# Search for groups of numbers and save coords for each digit
sym_coords = {(r, c): [] for r in range(len(schematic)) for c in range(len(schematic[r]))
                         if schematic[r][c] not in '123456789.'}

for row, line in enumerate(schematic):
    for num_match in re.finditer(r'\d+', line):
        span = num_match.span()
        adj = {(x, y) for x in (row - 1, row, row + 1) if x >= 0
                      for y in range(span[0] - 1, span[1] + 1) if y >= 0}
        
        for hit in adj & sym_coords.keys():
            sym_coords[hit].append(int(num_match.group()))

print(sum(sum(s) for s in sym_coords.values()))
print(sum(math.prod(s) for s in sym_coords.values() if len(s) == 2))
