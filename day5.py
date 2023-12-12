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
    
def splitcategory(n: str):
    "Split colon separated string 'name:ints' into (name, [ints])"
    n = n.partition(':')
    return (n[0].strip(), list(map(int, n[2].split())))

def trace_almanac(input, output=9999999999):
    "Input list of seeds to get smallest almanac location, takes single ints as a location to backtrack to seed"
    # Assumes almanac maps are ordered from seed -> ... -> location
    output = 9999999999 if output == None else output
    if input == None:
        return 0
    
    if output > 0:
        input = [input] if type(input) != list else input
        for s in input:
            for cat in almanac.values():
                for dst, src, stp in cat:
                    if s in range(src, src + stp):
                        s = s-src+dst
                        break
            output = min(s, output)

    if output < 0:
        output = int(input)
        for cat in reversed(almanac.values()):
            for ds, sr, z in cat:
                if output in range(ds, ds + z):
                    output = output-ds+sr
                    break

    return output

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
print('part1:', trace_almanac(seeds))

# Part 2 solution
# Seeds are actually ranges instead of locations, taken by pairs (start, length)
# Top-down brute force still takes forever for large inputs

seeds = [(s, s+w-1) for s, w in grouper(seeds, 2)]
# max_location = 0
# for d, s, p in next(reversed(almanac.values())):
#     max_location = max(d, max_location)
smol = (99999999999,99999999999999)
low_loc = 99999999999999999999
seed_map = set()
for group in seeds:
    a = tuple(map(trace_almanac, group))
    seed_map.add(range(min(group), max(group) + 1))
    if low_loc > min(a):
        smol = group
        low_loc = min(a)

found = None
n = 0
while n < low_loc + 1 and not found:
    n += 1
    s = trace_almanac(n, -1)
    for s_range in seed_map:
        if s in s_range:
            found = s
print('part2:', n)
