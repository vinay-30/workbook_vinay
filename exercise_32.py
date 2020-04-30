n=int(input('Enter a 4 digit integer number '))
n1=int(n/1000)
n2=int(n%1000)
n3=int(n2/100)
n4=int(n2%100)
n5=int(n4/10)
n6=int(n4%10)7890
total=n1+n3+n5+n6
print('The sum of the digits is ',total)