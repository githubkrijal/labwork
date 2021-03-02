#given the integer N - the number of minute that is passed since midnight
#how many hours and minutes are displayed on the 24h digit clock
#the program should print two number: the number of hiurs(between 0 and 23)
#and the number of minutes (between 0 and 59)
#for example, if N=150 then 150 minutes have passed since midnight - i.e. now is 2:30 am
#so the program should print2 30.
n= int(input("Enter the minutes passed since midnight"))
hours=(n//60)
minutes=(n%60)
print("the hours is",hours)
print("the minutes is",minutes)


print("It's "+str(hours)+":"+str(minutes)+" now")