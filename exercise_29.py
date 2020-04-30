ta=float(input('Enter the air temperature '))
v=float(input('Enter the Speed of thne wind'))
if(ta<=10 and  v<4.8):
    print('air temperature should be greater than 10 degree celsius and speed greater than 4.8 kph')

else :
    from math import pow
    wci=13.12+0.6215*ta-11.37*pow(v,0.16)+0.3965*ta*pow(v,0.16)
    print('The wind Chill Index is ',wci)