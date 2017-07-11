# -*- coding: utf-8 -*-
def decorator(aClass):
    class newClass:  # Returns a new class newClass in the decorator
        def __init__(self, age):
            self.total_display   = 0
            self.wrapped         = aClass(age)  # Record the object in the original object
        def display(self):
            self.total_display += 1  # New property total_display was added in order to record the time calling display. Also changed the method 'display'
            print("total display", self.total_display)
            self.wrapped.display()
    return newClass

@decorator
class Bird:
    def __init__(self, age):
        self.age = age
    def display(self):
        print("My age is",self.age)

eagleLord = Bird(5)
for i in range(3):
    eagleLord.display()


