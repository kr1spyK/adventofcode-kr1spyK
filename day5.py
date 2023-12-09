'''
2023 Advent of Code - Day 05: If You Give A Seed A Fertilizer
(https://adventofcode.com/2023/day/5)
Almanac lists seeds to plant and mix with which soil, fertilizer, water.
Seeds and map locations are separated by spaces
'''
def grouper(iterable, n, *, incomplete='ignore', fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    return zip(*args)
    
def splitcategory(n):
    n = n.partition(':')
    return (n[0].strip(), list(map(int, n[2].split())))

with open("input5.txt") as fin:
    content = fin.read().split('\n')

maps = [''] * 8
for i in range(len(maps)):
    while content:
        line = content.pop(0)
        if line == '': break
        maps[i] = maps[i] + ' ' + line
maps = [splitcategory(m) for m in maps]
seeds = maps.pop(0)[1]
almanac = {cat : list(grouper(nums,3)) for cat, nums in maps}

# Part 1 solution - Dynamic solution by getting seeds index if its mapped.
# Assumes almanac maps are ordered from seed -> ... -> location
location = []
for s in seeds:
    # print("current seed:", s)
    for cat in almanac.values():
        for plot in cat:
            dst, src, stp = plot
            if s in range(src, src + stp):
                # print(s, end=' -> ')
                s = s-src+dst
                break
        # print(s)
    location.append(s)

print('lowest:', min(location))
