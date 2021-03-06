#!/usr/bin/env python

from math import factorial

# The rows represent the truth label and the columns the predicted label
p_conf = [[1, 0,    0,    0,    0],
          [0, 0.97, 0.03, 0,    0],
          [0, 0.03, 0.96, 0.01, 0],
          [0, 0,    0,    1,    0],
          [0, 0,    0,    0.01, 0.99]]

b_res = 0                       # The result of the b term must be a global variable


# Performs combinatorial of two numbers
def comb(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)


# Computation of b term in the average accuracy formula
def b(n, m):

    global b_res
    b_res = 0

    indices_i = [0] * m     # The indices of the i nested loops. indices_i[0] is not used
    indices_j = [0] * m     # The indices of the j nested loops. indices_j[0] is not used

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

    loop_rec(m-1)           # (m-1) is the number of summatories regarding one of the two indices i, j

    return b_res


# Number of possible compositions of a n people, into m modules, with a restriction of r maximum people in each module
def c(n, m, r):
    c_res = 0
    for k in range(0, (n // (r+1))+1):        # // Performs a floor division
        c_res += (-1)**k * comb(m, k) * comb(n + m - 1 - k*(r+1), n - k*(r+1))
    return c_res


############################### Modify m to test with different number of modules #####################################
m = 4           # Number of modules
r = 4           # Maximum number of people inside a module
N_max = r*m     # Maximum number of people in the queue
#######################################################################################################################

summation = 0

for n in range(0, N_max+1):
    summation += b(n, m)/c(n, m, r)

av_accuracy = 1/(N_max+1) * summation

print('The average accuracy in a', m, 'module system is: ', av_accuracy)
