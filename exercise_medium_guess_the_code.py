#
# Description: Guessing the code for a safe
#
# Author: Ninad Dipal Zambare
#

import random
code = str(random.randrange(1000, 10000))
guess = input("Enter a guess: ")
number_satisfying_criteria_1 = 0
number_satisfying_criteria_2 = 0
if len(guess) == 4:
    for i in range (0, 4):
            if guess[i] in code:
                if code[i] == guess[i]:
                    number_satisfying_criteria_1 += 1
                else:
                    number_satisfying_criteria_2 += 1
    print(str(number_satisfying_criteria_1) + " digits are in the right place.")
    print(str(number_satisfying_criteria_2) + " digits are in the code but are in the wrong place")
else:
    print("Please enter a valid code")