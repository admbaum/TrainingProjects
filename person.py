class Person(object):
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def __str__(self):
        return self.name + ' ' + self.sex + ' ' + str(self.age)

    def changename(self, name):
        self.name = name

    def changeage(self):
        self.age = self.age + 1

person1 = Person('Jane Doe', 'F', 23)
person2 = Person('Bob Smith', 'M', 55)
print('Person 1: ' + str(person1))
person1.changeage()
print('Person 1: ' + str(person1))
person1.changename('Jane Brown')
print('Person 1: ' + str(person1))