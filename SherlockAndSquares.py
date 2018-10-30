"""
Solution for challenge: Sherlock and Squares,
Link: https://www.hackerrank.com/challenges/sherlock-and-squares/problem
Difficulty: Easy
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    rt_a, rt_b = math.sqrt(a), math.sqrt(b)
    if rt_a**2 == a:
        return (rt_b - rt_a + 1)
    return (rt_b - rt_a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()

#-------------- ALTERNATE SOLUTIONS --------------#
#def squares(a, b):
#    rt_a, rt_b = math.sqrt(a), math.sqrt(b)
#    return len([x for x in range(math.ceil(rt_a), math.floor(rt_b)+1)])
