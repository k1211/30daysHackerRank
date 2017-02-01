# Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! ( N factorial).

num = int(raw_input("Enter a number: "))


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print "The number's factorial is ", factorial(num)
