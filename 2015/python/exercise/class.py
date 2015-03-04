#!/usr/bin/env python
# coding=utf-8
class Robot:
    population = 0
    def __init__(self, name):
        self.name = name
        print("(Initializing {0})".format(self.name))
        Robot.population += 1

    def die(self):
        print("{0} is being destroyed!".format(self.name))
        Robot.population -= 1

        if  Robot.population == 0:
            print("{0} was the last one.".format(self.name))
        else:
            print("There are still {0:d} robots working.".format(Robot.population))
    def  sayHi(self):
        print("Greetings, my masters call me {0}.".format(self.name))
    
    @classmethod
    def howMany(cls):
        print("We have {0:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.sayHi()
Robot.howMany()

droid2 = Robot("C-3P0")
droid2.sayHi()
Robot.howMany()

print("\nRobots can do some work here.\n")
print("Robot have finished their work. So let's destroy them.\n")

droid1.die()
droid2.die()

Robot.howMany()

print("=================")

class SchoolMember:
    def __init__(self, name, age):
        self.name =name
        self.age =age
        print('(Initialized SchoolMember: {0})'.format(self.name))

    def tell(self):
        print('Name:"{0}" Age:"{1}"'.format(self.name, self.age), end ="")

class Teacher(SchoolMember):
    """docstring for ClassName"""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {0})'.format(self.name))

    def  tell(self):
        SchoolMember.tell(self)
        print('Salary:"{0:d}"'.format(self.salary))

class Student(SchoolMember):
    """docstring for ClassName"""
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {0})'.format(self.name))
        
    def  tell(self):
        SchoolMember.tell(self)
        print('Marks:"{0:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()

members = [t, s]
for member in members:
    member.tell()

