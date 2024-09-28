class Rectangle:
    def accept(self):
        self.l = int(input("Enter length of rectangle: "))
        self.b = int(input("Enter breadth of rectangle: "))
    
    def area(self):
        a = self.l * self.b
        print("Area of the rectangle is:", a)

# Create an instance of Rectangle
r = Rectangle()
r.accept()
r.area()
