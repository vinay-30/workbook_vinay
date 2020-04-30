s1=float(input('Enter the First side of the Triangle'))
s2=float(input('Enter the second side of the Traingle '))
s3=float(input('Enter the third side of the Triangle '))
s=(s1+s2+s3)/2
from math import sqrt
a=sqrt(s*(s-s1)*(s-s2)*(s-s3))
print('The Area of the traingle is ',a)
