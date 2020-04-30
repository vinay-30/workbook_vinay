print('1. a)Height in metres   b) Weight in kg' )
print(' 2. a)Height in Inches   b) Weight in Pounds')
a=int(input('Please select the option '))
if(a == 1):
    height=float(input('Enter the height in metres  '))
    weight=float(input('Enter the weight in kg '))
    bmi=(weight)/(height*height)
    print('BOdy mass index is ',bmi)
elif(a == 2):
    height=float(input('Enter the height in inches  '))
    weight=float(input('Enter the weight in pounds '))
    bmi=(weight*703)/(height*height)
    print('BOdy mass Index is ',bmi)
else :
     print('Invalid option')