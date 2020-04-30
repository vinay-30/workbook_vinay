P=float(input('Enter the Pressure in Pascals '))
V=float(input('Enter the Volume in Litres'))
T=float(input('Enter the Temperature in degree Kelvin'))
r=8.314
n=(P*V)/(r*T)
print('The amount of gas in moles is ',n)