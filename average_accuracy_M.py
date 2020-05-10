#!/usr/bin/env python

from math import factorial
from numpy import prod

# The rows represent the truth label and the columns the predicted label
p_conf = [[1, 0,    0,    0,    0],
         [0, 0.97, 0.03, 0,    0],
         [0, 0.03, 0.96, 0.01, 0],
         [0, 0,    0,    1,    0],
         [0, 0,    0,    0.01, 0.99]]


# Performs combinatorial of two numbers
def comb(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)

# def add(value):
#     global b_res
#     b_res +=

b_res = 0

def b(n, m):

    global b_res
    b_res = 0
    # i_start = []
    # i_stop = []
    #
    # i_start.append(0)                       # Index 1 will be the first element in the list
    # i_stop.append(0)                        # Index 1 will be the first element in the list
    # i_start.append(max(0, n - 4*(m-1)))
    #
    # for k in range(1, m):
    #     i_start.append(max(0, n - 4(m-k) - sum(i_start)))
    #     i_stop.append(min(4, n - sum(i_start)))
    #
    # j_start = i_start
    # j_stop = i_stop

    indices_i = [0] * (m+1)    # The indices of the i nested loops. indices_i[0] is not used
    indices_j = [0] * (m+1)    # The indices of the j nested loops. indices_j[0] is not used

    # Variable number of for loops using recursion
    def loop_rec(q):
        if q >= 1:
            for i in range(max(0, n - 4*q - sum(indices_i[1:(m-q)])), min(4, n - sum(indices_i[1:m-q])) + 1):
                for j in range(max(0, n - 4*q - sum(indices_j[1:(m-q)])), min(4, n - sum(indices_j[1:m-q])) + 1):
                    indices_i[m-q] = i
                    indices_j[m-q] = j
                    loop_rec(q - 1)
        else:
            prod = 1
            for k in range(1, m):
                prod *= p_conf[indices_i[k]][indices_j[k]]
            global b_res
            b_res += prod * p_conf[n-sum(indices_i[1:m])][n-sum(indices_j[1:m])]

    loop_rec(m-1)

    return b_res


# Number of possible compositions of a n people, into m modules, with a restriction of r maximum people in each module
def c(n, m, r):
    c_res = 0
    for k in range(0, (n // (r+1))+1):        # // Performs a floor division
        c_res += (-1)**k * comb(m, k) * comb(n + m - 1 - k*(r+1), n - k*(r+1))
    return c_res


# Case variable M
m = 7
N_max = 4*m
r = 4

summation = 0

for n in range(0, N_max+1):
    summation += b(n, m)/c(n, m, r)

av_accuracy = 1/(N_max+1) * summation

print('The average accuracy in a', m, 'module system is: ', av_accuracy)