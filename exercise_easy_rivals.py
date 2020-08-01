#
# Description: Compare the hits of one business with that of a rival business.
#
# Author: Ninad Dipal Zambare
#
import math


hits_first_business = 293
rate_increase_first_business = 2.6

hits_second_business = 130
rate_increase_second_business = 5

for i in range (1, 10):
    hits_first_business = math.floor(hits_first_business * ((1 + rate_increase_first_business / 100) ** i))
    hits_second_business = math.floor(hits_second_business * ((1 + rate_increase_second_business / 100) ** i))
    if hits_second_business > hits_first_business:
        print("Weeks it took for the rivals to overtake the original business: " + str(i))
        break