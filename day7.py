'''
2023 Advent of Code - Day 07: Camel Cards
(https://adventofcode.com/2023/day/7)
Version of five card draw with multiple hands and no exchanging cards.
Faces no suits,
'''
from collections import Counter
from operator import itemgetter

hands = ['high', 'pair', 'dubs', 'trip', 'full', 'quad', 'five']

def norm_deck(d):
    vals1 =['','','2','3','4','5','6','7','8','9','T','J','Q','K','A']
    ranks = {r:[] for r in hands}
    for h, b in d:   
        count = Counter(h)
        rank = None
        match len(count.keys()):
            case 1: rank = 'five'
            case 2: 
                rank = 'quad'
                if 3 in count.values():
                    rank = 'full'
            case 3: 
                rank = 'trip'
                if 2 in count.values():
                    rank = 'dubs'
            case 4: rank = 'pair'
            case 5: rank = 'high'
        h = [vals1.index(c) for c in h]
        ranks[rank].append([h, b])

    for v in ranks.values():
        if len(v) > 1: v.sort(key= itemgetter(0))
        for t in v:
            txt = ''.join(map(lambda x: vals1[x], t[0]))
            t[0] = txt

    return ranks

def wyld_deck(d):
    vals2 = ['','J','2','3','4','5','6','7','8','9','T','Q','K','A']
    ranks = {r:[] for r in hands}
    for h, b in d:  
        count = Counter(h)
        jays = count['J'] 
        suts = len(count.keys())
        rank = None
 
        # print(dict(count), end=' ')
        comm = count.most_common(2)
        com = comm[0][1] if comm[0][1] != jays else comm[-1][1]
        
        co = com + jays if suts != 5 != jays else com
        co = com + jays if com == 1 == jays else co
        match co:
            case 5:
                rank = 'five'
            case 4:
                rank = 'quad'
            case 3:
                rank = 'full'
                if comm[1][1] == 1:
                    rank = 'trip'
            case 2:
                rank = 'dubs'
                if suts == 4 or jays == 1:
                    rank = 'pair'
            case 1:
                rank = 'high'
        # print('com', com, 'j', jays, end=' ')
        # print(h)
        h = [vals2.index(c) for c in h]
        ranks[rank].append([h, b])
        # print(rank)

    for v in ranks.values():
        if len(v) > 1: v.sort(key= itemgetter(0))
        for t in v:
            txt = ''.join(map(lambda x: vals2[x], t[0]))
            t[0] = txt

    return ranks

with open("input7.txt") as fin:
    draws = [(h.split()[0], int(h.split()[1])) for h in fin.readlines()]

# Part 1 - Hands are ranked out of all draws, and is multiplier for each bid.
part1 = norm_deck(draws)
# for u in part1.items():
#     print(len(u[1]), u)
p1 = [t for ts in part1.values() for t in ts if t != []]
winnings = 0
for rank, play in enumerate(p1, 1):
    winnings += rank * play[1]
print(rank, play, winnings)

# Part 2 - 'J's are now jokers, wildcards. They are valued at 1 to compensate.
part2 = wyld_deck(draws)
# for u in part2.items():
#     print(len(u[1]), u)
p2 = [t for ts in part2.values() for t in ts if t != []]
winnings = 0
for rank, play in enumerate(p2, 1):
    winnings += rank * play[1]
print(rank, play, winnings)
