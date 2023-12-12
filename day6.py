'''
2023 Advent of Code - Day 06: Wait For IT
(https://adventofcode.com/2023/day/6)
A "water rally" time card gives max time allowed and farthest distance for a course.
Toy boats are charged up by holding a button and move once released. Charge starts the clock.
'''

with open("input6.txt") as fin:
    time = fin.readline().partition(':')[2].split()
    dist = fin.readline().partition(':')[2].split()

# Part 1: time and distance given as milliseconds and millimeters
# Boat starts at zero speed, each ms of charging gives 1 mm/ms
# Return total permutations where you beat records in each race.
td = list(zip([int(i) for i in time], [int(i) for i in dist]))
permute = 1
for t, d in td:
    wins = 0
    for i in range(1, t):
        race = i*(t-i)
        if race > d:
            wins += 1
    # print('wins', wins)
    permute *= wins
print(permute)
