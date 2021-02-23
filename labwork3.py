#N student takes K apples and distribute thm among each other evenly.
#the undivisible part remains
apples=int(input("Enter the numbers of apples"))
people=int(input("Entter the number of poeple"))
basket=apples/people
inbasket=apples%people
print("distributed apple to each person", basket)
print("Remaining in basket",inbasket)