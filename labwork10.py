'''write a python program to convert seconds to day hour minute and second'''
second=int(input("Enter the second"))

day=(((second//60)//60)//24)
print("The day for given second is",day)

hour=((second//60)//60)
print("the hour for given second is",hour)

minute=(second//60)
print("the minute for the given second is",minute)