#!/usr/bin/env python

from math import factorial

# The rows represent the truth label and the columns the predicted label
p_conf = [[1, 0,    0,    0,    0],
         [0, 0.97, 0.03, 0,    0],
         [0, 0.03, 0.96, 0.01, 0],
         [0, 0,    0,    1,    0],
         [0, 0,    0,    0.01, 0.99]]


# Performs combinatorial of two numbers
def comb(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)


def b(n):
    b_res = 0
    for i in range(max(0, n-4), min(4, n)+1):
        for j in range(max(0, n-4), min(4, n)+1):
            b_res += p_conf[i][j] * p_conf[n-i][n-j]
    return b_res


# Number of possible compositions of a n people, into m modules, with a restriction of r maximum people in each module
def c(n, m, r):
    c_res = 0
    for k in range(0, (n // (r+1))+1):        # // Performs a floor division
        c_res += (-1)**k * comb(m, k) * comb(n + m - 1 - k*(r+1), n - k*(r+1))
    return c_res


# Case M = 2
m = 2
n = 4*m
r = 4

sum = 0

for i in range(0, n+1):
    sum += b(i)/c(i, m, r)

av_accuracy = 1/(n+1) * sum

print('The average accuracy in a', m, 'module system is: ', av_accuracy)
