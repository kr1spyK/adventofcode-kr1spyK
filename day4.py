'''
2023 Advent of Code - Day 04: Scratchcards
(https://adventofcode.com/2023/day/4)
Scratchcards made of lists of winning numbers and playing numbers, separated by vertical bar.
'''

# ------Part 1 solution
# First match = one point, subsequent matches double the total value.
point_total = 0
with open("input4.txt") as fin:
    cards = fin.readlines()
    card_count = [1] * len(cards)

    for i, card in enumerate(cards):
        numbers = card.strip().partition(':')[2]
        winning, players = numbers.split('|')
        winning, players = winning.split(), players.split()

        w = len(set(winning) & set(players))

        point_total += 2**(w - 1) if w else 0

        # print(f" {point_total} total")
        # Part 2: cards reward cards
        for j in range(w):
            card_count[i + j + 1] += card_count[i]

print(sum(card_count))
