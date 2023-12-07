'''
2023 Advent of Code - Day 04: Scratchcards
(https://adventofcode.com/2023/day/4)
Scratchcards made of lists of winning numbers and playing numbers, separated by vertical bar.
'''

# ------Part 1 solution
# First match = one point, subsequent matches double the total value.
point_total = 0
with open("input4.txt") as fin:
    for card in fin:
        card = card.strip().partition(':')
        numbers = card[2].partition('|')
        winning = {int(n) for n in numbers[0].split()}
        players = {int(n) for n in numbers[2].split()}

        win = [n for n in winning if n in players]
        points = 2**(len(win) - 1) if win else 0

        point_total += points
        # print(f"{card[0]}: {points} won, {point_total} total")
