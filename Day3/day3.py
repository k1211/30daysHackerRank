# Given an integer, n , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5 , print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird
# Complete the stub code provided in your editor to print whether or not  is weird.


N = int(raw_input().strip())

if N % 2 != 0:
    print "Weird"
else:
    if N >= 2 and N<= 5:
        print "Not Weird"
    elif N>=6 and N<= 20:
        print "Weird"
    else:
        print "Not Weird"