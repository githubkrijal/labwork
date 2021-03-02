student1=int(input("Enter the number of students"))
student2=int(input("Enter the number of students"))
student3=int(input("Enter the number of students"))
desk1=student1//2
print("the required number of desk is",desk1)
desk2=student2//2
print("the required number of desk is",desk2)
desk3=student3//2
print("the required number of desk is",desk3)
remaining1=student1%2
print("remaining student",remaining1)
remaining2=student2%2
print("remaining student",remaining2)
remaining3=student3%2
print("remaining student",remaining3)
totaldesk=desk1+desk2+desk3+remaining1+remaining2+remaining3
print("the total number of desk",totaldesk)