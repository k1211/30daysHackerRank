# Read a string, s, and print its integer value; if  cannot be converted to an integer, print Bad String.

s = raw_input().strip()

try:
    print int(s)
except:
    print "Bad String"