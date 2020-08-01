#
# Description: Find the triangular number with 200+ factors
#
# Author: Ninad Dipal Zambare
#

# The calculation will take approximately 1 minute 30 seconds


import math


def factorize(number):
    factors = 0
    x = 1
    while x <= math.sqrt(number):
        if number // x == number / x:
            factors += 1
    return factors


triangular_number = 0
i = 0
while factorize(triangular_number) <= 200:
    i += 1
    triangular_number += i

print("The first triangular number with more than 200 divisors is the " + str(i) + "th triangular number: " + str(
    triangular_number))
