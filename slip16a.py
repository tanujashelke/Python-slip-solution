class Rectangle:
    def __init__(self,l,b):
       self.l=l
       self.b=b
    def display(self):
        print("length of rectangle is",self.l)
        print("bridth of rectangle is",self.b)
    def area(self):
        return(self.l*self.b)
    def perimeter(self):
        return(2*self.l+2*self.b)
l=int(input("enter length"))
b=int(input("enter  breadth"))
r=Rectangle(l,b)
r.display()
print(r.area())
print(r.perimeter())       