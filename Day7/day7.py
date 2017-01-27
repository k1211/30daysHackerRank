# Given an array, arr , of n integers, print a 's elements in reverse order as a single line of space-separated numbers.


from __future__ import print_function

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
rarr = []
for i in reversed(arr):
    rarr.append(i)

for i in rarr:
    print(str(i)+ ' ', sep=' ', end='')

