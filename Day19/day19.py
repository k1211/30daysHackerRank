# Write Caltulator class.
# The implementation for the divisor_sum method must take an integer parameter,n , and return the sum of all its divisors.

class Calculator(object):

    def __init__(self,n):
        self.n = n

    def divisor_sum(self):
        sum_list=[]
        for i in range(1,self.n+1):
            if self.n % i == 0:
                sum_list.append(i)
        return sum(sum_list)

num = int(raw_input("Enter a number: "))
my_calc = Calculator(num)
print my_calc.divisor_sum()