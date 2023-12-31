# Day 1: Trebuchet?!
# For each line of text combine first digit and last digit to form a two-digit number.
# Return sum of all numbers for a document to get calibration number.
# assumes calibration document is a reasonable size of arbitrary length lines with non-zero value.
import re

with open('input1.txt', 'r') as fin:
    lines = file.readlines()

solution1 = 0
solution2 = 0

num_pattern = re.compile('(?=(\d|one|two|three|four|five|six|seven|eight|nine))', re.IGNORECASE)
num_words = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

for line in lines:
# Part one solution only looks for digits.
    digits = [int(x) for x in line if x.isdigit()]
    calibration_val = digits[0] * 10 + digits[-1]
    solution1 += calibration_val

# Part two solution, looks for digits and written numerals (one, two, three, ..., seven, eight, nine).
# logic is non case-sensitive, at first I thought about trying to find() all the word strings, then the digits and map them or something
# too convoluted, and I found that regex can do it all with lookaround and zero-length assertions. sidenote: Stephen Kleene is an absolute madman
    digits = num_pattern.findall(line)

    try: first = int(digits[0])
    except: first = num_words[digits[0]]

    try: last = int(digits[-1])
    except: last = num_words[digits[-1]]

    solution2 += first * 10 + last

print(solution1, solution2)
