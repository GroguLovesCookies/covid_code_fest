#
# Description: Check if a word matches particular criteria
#
# Author: Ninad Dipal Zambare
#
'''
Tests:
    As: Invalid
    As9: Valid
    isnt: Invalid
    isn9: Invalid
    Is a0: Invalid
Result: Correct
'''

import re


wordRegex = re.compile("[A-Z]{1}[a-z]+[0-9]{1}")
word = input("Enter a word")
if re.match(wordRegex, word):
    print("Valid")
else:
    print("Invalid")