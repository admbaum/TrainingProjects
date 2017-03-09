"""
abstract data types

Name:
    Attributes:
        First name, Middle name, last name
    behaviors:
        first-middle-name
        last-first-middle
        initials
"""


class Name(object):
    #  constructor method - instantiation(parameter list, starting with self)
    def __init__(self, first, middle, last):
        self.first = first
        self.middle = middle
        self.last = last

    #  to-string method - to look at the current state of a class object or display the current state of a class object
    def __str__(self):
        return self.first + ' ' + self.middle + ' ' + self.last

    def lastfirst(self):
        return self.last + ' ' + self.first + ' ' + self.middle

    def initials(self):
        return self.first[0] + self.middle[0] + self.last[0]

aName = Name('Mary', 'Liz', 'Smith')
print(aName)    # the to-string method is required to make this print the contents of the instance and not the memory
# location, a way to remember is its an parameter to-string method
print(aName.lastfirst())
print(aName.initials())


