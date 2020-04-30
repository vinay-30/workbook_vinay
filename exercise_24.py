days=int(input('Enter the No of days :'))
hours=int(input('Enter no of hours '))
min=int(input('Enter No of minutes'))
sec=int(input('Enter the seconds'))
sec1=days*86400+hours*3600+min*60+sec
print('Total number of seconds is ',sec1)
