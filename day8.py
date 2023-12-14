'''
2023 Advent of Code - Day 08: Haunted Wasteland
(https://adventofcode.com/2023/day/8)
Navigate using the map of left-right sequence string 'LR...' and 
Node coordinates 'AAA = (BBB, CCC)'
'''
from itertools import cycle
from math import lcm

def tracemap(strt: str) -> int:
    "Takes beginning node and returns number of steps to reach (**Z)"
    node = strt
    for i, turn in enumerate(cycle(turns), 1):
        node = node_dict[node][turn]
        if node.endswith('Z'):
            break
    return i

with open("input8.txt") as fin:
    turns, _, *nodes = fin.read().splitlines()

node_dict = {n[:3]: {'L': n[7:10], 'R': n[12:15]} for n in nodes}

# Part 1: Navigate from 'AAA' to 'ZZZ' with the LR string and node map.
if 'AAA' in node_dict.keys():
    print(tracemap('AAA'))

# Part 2: Looks like amount of nodes ending in 'A' (**A) = 'Z' ending nodes.
# Find number of steps where all nodes reach their destination simultaneously.
starts = [n for n in node_dict.keys() if n.endswith('A')]
cycles = [tracemap(c) for c in starts]

print(lcm(*cycles))
