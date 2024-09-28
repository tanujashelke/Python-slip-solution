class Shape:
    pass
class Square(Shape):
    def __init__(self,l):
        self.l=l
    def area(self):
        a=self.l*self.l
        print("Area of square is:",a)
    def volume(self):
        vol=4*self.l
        print("volume of square is:",vol)
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def cArea(self):
        ac=3.14*self.r*self.r
        print("area of circle is:",ac)
    def cVolume(self):
        cv=2*3.14*self.r*self.r
        print("volume of circle is:",cv)
l=int(input("enter length of square"))              
r=int(input("enter radius of circle"))
c=Circle(r)       
c.cArea()
c.cVolume()
c=Square(l)
c.area()
c.volume()