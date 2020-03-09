n=int(input('Enter the total number of containers'))
s=float(input('Enter the size of each container in litres '))
i=n*s
if i<=1:
	cost= 0.10
	print('The amount that will be refunded  is $',cost)
elif i>=1 :
	cost=0.25
	print('The amount that will be refunded  is $',cost)

