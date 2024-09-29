class Circle:
    def __init__(self, radius):
        self.radius = radius

    
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    
    def area(self):
        return 3.14 * (self.radius ** 2)

   
    def display(self):
        print(f"Radius: {self.radius}")
        print(f"Area: {self.area()}")



circle1 = Circle(5)
circle2 = Circle(7)


print("Circle 1:")
circle1.display()
print("\nCircle 2:")
circle2.display()


circle3 = circle1 + circle2


print("\nAfter adding Circle 1 and Circle 2:")
circle3.display()
