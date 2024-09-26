'''pi=22/7

r = float(input('Radius of sphere: '))

sur_area = 4 * pi * r *r

volume = (4/3) * (pi * r * r * r)

print("Surface Area is: ", sur_area)

print("Volume is: ", volume)

 

def areaCube( a ):

    return (a * a * a)

 

def surfaceCube( a ):

    return (6 * a * a)

 

a = 5

print("Area =", areaCube(a))


print("Total surface area =", surfaceCube(a))

'''
pi=3.14
a=8
r=int(input("enter radius"))
def sphere():
    area=4*pi*r*r
    print("area of sphere is:",area)
    volume=(4/3)*pi*r*r*r
    print("volume of sphere is:",volume)
sphere()    
def cube():
   cubearea =a*a*a
   print("Area of cube is:",cubearea)
   cubevolume=6*a*a
   print("volume of cube is:",cubevolume)
cube()