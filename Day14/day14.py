# Complete the Difference class by writing the following:
#   - A class constructor that takes an array of integers as a parameter and saves it to the elements instance variable.
#   - A computeDifference method that finds the maximum absolute difference between any 2 numbers in the array
#     and stores it in the maximum_difference instance variable.

class Difference(object):

    def __init__(self, a):
        self.__elements = a
        self.maximum_difference = 0

    def compute_difference(self):

        for i in xrange(len(self.__elements)):
            for j in xrange(len(self.__elements)):
                temp = abs(self.__elements[i] - self.__elements[j])
                if temp > self.maximum_difference:
                    self.maximum_difference = temp

# End of Difference class

a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.compute_difference()

print d.maximum_difference