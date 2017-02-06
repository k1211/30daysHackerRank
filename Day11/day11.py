# Context
# Given a 6x6 2D Array, A :
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
#
# We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:
#
# a b c
#   d
# e f g
#
# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.
#
# INPUT: 6 lines of input, where each line contains  space-separated integers describing 2D Array ;
# every value in  will be in the inclusive range of -9 to 9.
#
# Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

arr = []
for arr_i in xrange(6):
   arr_row = map(int,raw_input().strip().split(' '))
   arr.append(arr_row)

def hourglass(matrix):

    max_sum = None
    sum_arr = []

    for i in range(0, len(matrix) - 2):
        for j in range(0, len(matrix) - 2):
            a = matrix[i][j]
            b = matrix[i][j+1]
            c = matrix[i][j+2]
            d = matrix[i+1][j+1]
            e = matrix[i+2][j]
            f = matrix[i+2][j + 1]
            g = matrix[i+2][j + 2]

            suma = a + b + c + d + e + f + g
            sum_arr.append(suma)

            if suma > max_sum:
                max_sum = suma

    return max_sum

result = hourglass(arr)
print result