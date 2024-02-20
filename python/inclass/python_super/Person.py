class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = int(age)
    def __str__ (self):
        return 'name: {0}\nage: {1}'.format(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,grades):
        Person.__init__(self,name,age)
        self.grades = float(grades)

    def __str__ (self):
        return super().__str__() +'\ngrade: {:.2f}'.format(self.grades)
student = Student('Thanida', 20, 4.00)           
print(student)