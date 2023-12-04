# Day 2: Cube Conundrum
# For an arbitrary amount of games, there are n rounds of colored cubes drawn.
# Find all possible games with 12 red cubes, 13 green cubes, and 14 blue cubes.
# return sum of game IDs for every possible game.
with open("input2.txt") as fin:
    lines = fin.readlines()

# line format, colors are random  - eg. Game N: x red, x blue, x green;
# Game id followed by colon, comma separated counting each rgb cube, each draw separated by semicolon
cube_limit = {'red': 12, 'green': 13, 'blue': 14}
id_sum = 0
power_sum = 0
for line in lines:
    gameid = line.find(':')
    draws = line[gameid+2:].strip().split('; ')
    gameid = int(line[5:gameid])
    
    # print("Gmae", gameid, end=' ')
    
    drawcount = 1
    cube_count = {'red': 0, 'green': 0, 'blue': 0}
    for draw in draws:
        cubes = draw.split(',')
        ## print(f"({drawcount})", end=' ')
        for rgb in cubes:
        # rgb[1] will be the color, rgb[0] will be the count
            rgb = rgb.split()
            count = int(rgb[0])
            cube_count[rgb[1]] = max(count, cube_count[rgb[1]])
            if count > cube_limit[rgb[1]]:
                gameid = 0
            ## print(f"{rgb[1]}: {rgb[0]}", end=' ')
        ## print()
        drawcount += 1

    id_sum += gameid

    # if gameid == 0:
    #     print("invalid")
    # else: print()

# In part two need the minimum set of cubes that still make game possible.
# I already count the highest amount ddrawn for every color in each game
# Take power of a set (r*g*b) and return sum of every power

    # print(f"count: {cube_count}")
    # print(cube_count.values())
    power = 1
    for x in cube_count.values():
        power *= x
    power_sum += power
print("idsum:", id_sum)
print("powersum:", power_sum)
