'''
2023 Advent of Code - Day 09: Mirage Maintenance
(https://adventofcode.com/2023/day/9)
Report is a sequence of numbers representing change of a single value over time.
For each line
'''

with open("input9.txt") as fin:
    oasis = [[int(i) for i in l.split()] for l in fin.readlines()]

for h in oasis:
    dif = h.copy(); h.clear(); h.append(dif)
    while any(dif):
        new = [(dif[i] - dif[i-1]) for i in range(1, len(dif))]
        # if not any(new): new.append(0)
        h.append(new)
        dif = new
# Part 1: extrapolate next value by sum of differences, return sum of results.
# Part 2: extrapolate prev value and return sum of result, same way.
part1, part2 = 0, 0
for hist in oasis:
    # print([d for d in reversed(hist)])
    nex, pre = 0, 0
    for dif in reversed(hist):
        nex += dif[-1]
        dif.insert(0, pre := dif[0] - pre)
        
    # print([d for d in reversed(hist)])
    part1 += nex
    part2 += pre
print(part1)
print(part2)
