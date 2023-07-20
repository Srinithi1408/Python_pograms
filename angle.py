def square():
    print("\tSquare")
    area1=int(input('Length of the side:'))
    c=area1*area1
    print('Area of Sequar:',c)
print(square())


def rectangle():
    print("\n\tRectagle")
    length=int(input('value is length:'))
    breath=int(input('value is breath:'))
    c=length*breath
    print('Area of Rectangle:',c)
print(rectangle())


def triangle():
    print("\n\tTriangle")
    breath=int(input('Enter Breath: '))
    hight=int(input('Enter Hight: '))
    c=(1/2)*breath*hight
    print('Area of Triangle:',c)
print(triangle())


import math
def circle():
    print("\n\tCircle")
    radius=int(input('Enter the value of Circle:'))
    c=3.14*radius*radius
    print("Area of the Circle is:",c)
print(circle())
    
    
