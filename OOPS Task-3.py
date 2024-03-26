# Class function to calculate Area and Perimeter of a circle using two classes
class Area_Of_Circle():
    def __init__(self, radius):
        self.radius = radius
        #print("Program to find the Area and Perimeter of Circle")
        #print("The Given Radius is:", self.radius)
        

    def area(self):
        print("Area of Circle is:", 3.141 * self.radius * self.radius)
        
class Perimeter_Of_Circle(Area_Of_Circle):
    def __init__(self, radius):
       super().__init__(radius)
       self.radius = radius
       
    def areaof(self):
        print("Perimeter of Circle is:", 2 * 3.141 * self.radius)
            
print("Program to find the Area and Perimeter of Circle")
rad=5
print("The Given Radius is:", rad)
red= Area_Of_Circle(rad)
print(red.area())
blue = Perimeter_Of_Circle(rad)
print(blue.areaof())