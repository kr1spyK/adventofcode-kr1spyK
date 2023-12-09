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

# LMAO TOO MUCH MEMORY
for cat, vals in almanac.items():
    # Sources and destinations are mapped 1:1 so they can be stored in same 'plot'
    plot = {}
    for v in vals:
        dst, src, stp = v
        for i in range(stp):
            plot[src + i] = dst + i
    almanac[cat] = plot

# Assumes almanac maps are ordered from seed -> ... -> location
location = []
for s in seeds:
    print("current seed:", s)
    for p in almanac.values():
        print(p)
        if s in p: 
            print(p[s])
            s = p[s]
        else: print(s)
    location.append(s)
print(location, min(location))
