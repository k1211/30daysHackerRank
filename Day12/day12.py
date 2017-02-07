# You are given two classes, Person and Student, where Person is the base class and Student is the derived class.
# Completed code for Person and a declaration for Student are provided for you in the editor.
# Observe that Student inherits all the properties of Person.
#
# Complete the Student class by writing the following:
# A Student class constructor, which has  parameters:
# -A string, first_name.
# -A string, last_name.
# -An integer, id.
# -An integer array (or vector) of test scores, scores.
# -A char calculate() method that calculates a Student objects average
# and returns the grade character representative of their calculated average:
# O 90 <= a <= 100
# E 80 <= a <= 90
# A 70 <= a <= 80
# P 55 <= a <= 70
# D 40 <= a <= 55
# T a < 40

# INPUT
# The first line contains first_name, last_name and id respectively.
# The second line contains the number of test scores.
# The third line of space-separated integers describes scores .

class Person(object):
    def __init__(self, firstName, lastName, idNumber):
        self.first_name = firstName
        self.last_name = lastName
        self.id = idNumber

    def printPerson(self):
        print "Name:", self.last_name + ",", self.first_name
        print "ID:", self.id

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):

        num_scores = len(self.scores)
        grade = sum(self.scores)/num_scores

        if grade >=90:
            return "O"
        elif grade >= 80 and grade < 90:
            return "E"
        elif grade >= 70 and grade < 80:
            return "A"
        elif grade >= 55 and grade < 70:
            return "P"
        elif grade >= 40 and grade < 55:
            return "D"
        else:
            return "T"


line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = map(int, raw_input().split())

s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()