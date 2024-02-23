class Animal:
    def __init__(self, name,color):
        self.name = name
        self.color = color
        
    def __str__(self):
        return 'name: {0}, color: {1}'.format(self.name,self.color)
        
class Dog(Animal):
    def __init__(self, name, color,leg):
        super().__init__(name, color)
        self.leg = leg
        
    def setName(self,name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def setColor(self,color):
        self.color = color
        
    def getColor(self):
        return self.color
    
    def setLeg(self,leg):
        self.leg = leg
        
    def getLeg(self):
        return self.leg
    
    def __str__(self):
        return '{0}, leg: {1}'.format(super().__str__(),self.leg)

dog1 = Dog('Darling','Orange',4)
print(dog1)
dog1.setColor('Pink')
print(dog1)