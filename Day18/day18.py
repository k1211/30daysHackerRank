# Check if the given string, s, is a palindrome

s = (raw_input()).strip()

if s == s[::-1]:
    print "'The word %s is a palindrome.'"%s
else:
    print "'The word %s is not a palindrome.'"%s