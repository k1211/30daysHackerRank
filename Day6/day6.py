# Task
# Given a string, S , of length N that is indexed from 0 to N-1 , print its even-indexed and odd-indexed characters
# as 2 space-separated strings on a single line.

# Input Format:
# The first line contains an integer, T (the number of test cases).
# Each line i of the T subsequent lines contain a String,S .

t = int(raw_input("Number of test cases: "))

def odd_even(s):

    s_odd = ''
    s_even = ''

    for i in range(0,len(s)):
        if i % 2 == 0:
            s_even += s[i]
        else:
            s_odd += s[i]

    return s_even, s_odd


for i in range(0,t):
    word = raw_input("Give a word: ")
    odd, even = odd_even(word)
    print odd + ' ' + even