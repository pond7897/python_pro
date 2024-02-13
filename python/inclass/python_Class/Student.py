class Student:
    def __init__ (self, FirstName, LastName, Age, Sex, Weight):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Age = Age
        self.Sex = Sex
        self.Weight = Weight
    def hello(self):
        print("Hello %s %s" %(self.FirstName, self.LastName))
s1 = Student()
print(s1)