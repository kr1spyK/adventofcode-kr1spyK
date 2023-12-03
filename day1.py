# Day 1: Trebuchet?!
# For each line of text combine first digit and last digit to form a two-digit number.
# Return sum of all numbers for a document to get calibration number.
# assumes calibration document is a reasonable size of arbitrary length lines

file = open('input1.txt', 'r')
lines = file.readlines()

calibration_sum = 0
for line in lines:
    digits = [int(x) for x in line if x.isdigit()]
    calibration_val = digits[0] * 10 + digits[-1]
    # print(calibration_val, end=' ')
    calibration_sum += calibration_val
    
# print()
print(calibration_sum)
file.close()
