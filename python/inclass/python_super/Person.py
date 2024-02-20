class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = int(age)

class Student(Person):
    def __init__(self,name,age,grades):
        Person.__init__(self,name,age)
        self.grades = float(grades)

    def __str__ (self):
        return f'name: {self.name}\nage: {self.age}\ngrade: {self.grades}'
student = Student('Titipong',20,'4.00')           
print(student)