class Circle:
    def __init__(self, r):
        self.r = r
    
    def area(self):
        a = 3.14 * self.r * self.r
        print("Area of the circle is:", a)
    
    def perimeter(self):
        p = 2 * 3.14 * self.r
        print("Perimeter of the circle is:", p)


c = Circle(7)
c.area()
c.perimeter()
       