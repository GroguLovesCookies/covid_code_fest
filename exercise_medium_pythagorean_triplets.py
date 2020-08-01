#
# Description: Find the pythagorean triplets a, b, and c such that a + b + c = 1000 & a^2 + b^2 = c^2
#
# Author: Ninad Dipal Zambare
#

for i in range(1, 1001):
    for j in range (1, 1001-i):
        k = 1000-(i+j)
        if i**2 + j**2 == k**2:
            print("The numbers are %d, %d and %d. Their product is %d" %(i, j, k, i*j*k))
            break