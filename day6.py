'''
2023 Advent of Code - Day 06: Wait For IT
(https://adventofcode.com/2023/day/6)
A "water rally" time card gives max time allowed and farthest distance for a course.
Toy boats are charged up by holding a button and move once released. Charge starts the clock.
'''
def td_calc(td: list):
    permute = 1
    for t, d in td:
        wins = 0
        for i in range(1, t):
            if i*(t-i) > d:
                wins += 1
        permute *= wins
    return permute

with open("input6.txt") as fin:
    time = fin.readline().partition(':')[2].split()
    dist = fin.readline().partition(':')[2].split()

# Part 1: time and distance given as milliseconds and millimeters
# Boat starts at zero speed, each ms of charging gives 1 mm/ms
# Return total permutations where you beat records in each race.
td = list(zip([int(i) for i in time], [int(i) for i in dist]))
part1 = td_calc(td)
print('part1:', part1)

# Part 2: input is actually records for one race, kerning is off.
# EZIST PART YET omg
td= (int(''.join(time)), int(''.join(dist)))
print(td_calc([td]))
