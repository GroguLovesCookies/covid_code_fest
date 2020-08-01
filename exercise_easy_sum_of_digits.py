#
# Description: Sum of digits of 2^1450
#
# Author: Ninad Dipal Zambare
#


def sum_of_digits(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    print(total)


sum_of_digits(2**1450)
