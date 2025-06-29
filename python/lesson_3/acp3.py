name= input("Enter your name.")
age= int(input("Enter your age."))
clss= int(input("Enter your class."))
percentage= int(input("Enter your percentage."))

print("Name=",name)
print("Age=",age)
print("Class=",clss)
print("Percentage=",percentage)
print("Decision:")
if percentage<75:
    print("You cannot sit for the exam.")
else:
    print("You can sit for the exam.")