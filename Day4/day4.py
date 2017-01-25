# Write a Person class with an instance variable, age , and a constructor that takes an integer, initial_age, as a parameter.
# The constructor must assign initial_age to age after confirming the argument passed as initial_age is not negative;
# if a negative argument is passed as initial_age, the constructor should set age to 0
# and print Age is not valid, setting age to 0..
# In addition, you must write the following instance methods:
#
# yearPasses() should increase the  instance variable by 1.
# amIOld() should perform the following conditional actions:
# If age<13, print You are young..
# If  age>=13 and age <18, print You are a teenager..
# Otherwise, print You are old..
#  t - number of test cases

class Person(object):

    def __init__(self, initial_age):
        # Add some more code to run some checks on initial_age
        if initial_age < 0:
            print "Age is not valid, setting age to 0."
            self.age = 0
        else:
            self.age = initial_age

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print "You are young."
        elif self.age >= 13 and self.age < 18:
            print "You are a teenager."
        else:
            print "You are old."

    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1

t = int(raw_input())
for i in range(0, t):
    age = int(raw_input())
    p = Person(age)
    p.amIOld()
    for j in range(0, t):
        p.yearPasses()
    p.amIOld()
    print("")