a=int(input('Enter the first numvber'))
b=int(input('Enter the second number'))
c=int(input('Enter the third number'))
print('The Smallest number is ',min(a,b,c))
print('The Largest number is ',max(a,b,c))
d=a+b+c-min(a,b,c)-max(a,b,c)
print('The middle value is ',d)