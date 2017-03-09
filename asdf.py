class Name(object):
    #  constructor method - instantiation(parameter list, starting with self)
    def __init__(self, first, middle, last):
        self.first = first
        self.middle = middle
        self.last = last

    def printname(self):
        print(self.first, self.middle, self.last)

a = Name('Mary', 'Liz', 'Smith')
a.printname()