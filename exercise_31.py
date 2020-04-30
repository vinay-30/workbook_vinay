#1kp=0.145 pounds per sq inch
#1kpa=7.50062 mm of hg
#1kpa = 0.00987 atm

p=float(input('Enter pressure in kilo pascals '))
print('Equivalent pressure in Pounds per square inch is ',p*0.145)
print('Equivalent pressure in Millimetres of Mercury   is ',p*7.50062,'mm of hg')
print('Equivalent pressure in atmosphere is ',p*0.00987)