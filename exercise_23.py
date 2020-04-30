s=float(input('Enter the length of the side of regular polygon'))
n=int(input('Enter the number of sides of the regular hexagon'))
from math import tan,pi
a= (n*s*s)/4*tan(pi/n)
print('The area of the Regular polygon is ',a)