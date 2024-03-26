#OOPS Task
#1 Create a program class called circle with constructor which will take a list as an argument for the task.
#The List is[10,501,22,37,100,999,87,351]
class circle:
    print("Class executed")
# constructor
    def __init__(self):
# initializing instance variable
        print("Constructor executed")
        self.m=[10,501,22,37,100,999,87,351]

# a method
    def read_number(self):
        print("Method is executed")
        print(self.m)

# creating object of the class. This invokes constructor
obj = circle()

# calling the instance method using the object obj
obj.read_number()