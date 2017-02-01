# Given a base-10 integer, , convert it to binary (base-2).
# Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.


num = int(raw_input("Enter a number: "))

def binary_rep(n):
    return bin(n)[2:]

def count_ones(b):

    b = str(b)
    max_len = 0

    for i in b.split("0"):
        if max_len < len(i):
            max_len = len(i)

    return max_len


print binary_rep(num)
print count_ones(binary_rep(num))