#OOPS Task-2
# Creating Private Variable with value 3.141
class pi:
    def __init__(self,a):
        self.a=a
    def print123(self):
        print(self.a)
    def private(self):
        self.print123()
p=pi(3.141)
p.private()