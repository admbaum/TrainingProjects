class Student(object):
    grades = []  #  The constructor has no part in initializing the grades field. An empty list will be generated when the
              #  Student object is created.

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def addgrade(self, grade):  #  adds grades to the empty list
        self.grades.append(grade)

    def showgrades(self):
        grds = ''
        for grade in self.grades:
            grds += str(grade) + ' '
        return grds

stu1 = Student('Jones', '123')
stu1.addgrade(88)
stu1.addgrade(64)
stu1.addgrade(70)
stu1.addgrade(90)
print(stu1.showgrades())