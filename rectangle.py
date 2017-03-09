class Shape(object):
    def __init__(self, xcor, ycor):
        self.x = xcor
        self.y = ycor

    def __str__(self):
        return 'x: ' + str(self.x) + ' y: ' + str(self.y)

    def move(self, x1, y1):
        self.x = self.x + x1
        self.y = self.y +y1


class Rectangle(Shape):
    def __init__(self, xcor, ycor, width, height):
        Shape.__init__(self, xcor, ycor)
        '''
        ^^^^^^^^^This is a call to the base class constructor
        '''
        self.width = width
        self.height = height

    def __str__(self):
        retstr = Shape.__str__(self)
        '''
        now we want to add to whats in the base class...concatenate to the current value
        '''
        retstr += ' width: ' + str(self.width) + \
            ' height: ' + str(self.height)
        return retstr

#  now create a rectangle using a x = 5, y = 10, width =8, height of 9
rec = Rectangle(5, 10, 8, 9)
print(rec)
#  now move the rectangle to a new xy coord and print it again
rec.move(10, 12)
print(rec)
