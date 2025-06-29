#if else
num = 50

if num>60:
    print("Greater that 60.")
elif num==50:
    print("The number is 50.")
else:
    print("Less than 60.")

num2 = float(input("Enter your age."))

#nested if else
if num2>0:
    if num2>18:
        print("Adult")
    else:
        print("Minor")
else:
    print("Invalid Input.")

#odd even

num3=int(input("Enter a number."))

if num3%2==0:
    print("It is even.")
else:
    print("It is odd.")

#BMI Calculator.

h= int(input("Enter your height(cm)."))
w= int(input("Enter your weight(kg)."))

bmi = w / ( h/100)**2

print("The BMI of the user is", bmi)


if bmi<=18.4:
    print("Underweight.")
elif bmi<=24.9:
    print("Healthy.")
elif bmi<=29.9:
    print("Overweight.")
elif bmi<=34.9:
    print("Highlt overweight.")
elif bmi<=39.9:
    print("Obese.")
else:
    print("Highly obese.")

#date time calender

import datetime

current_time = datetime.datetime.now()
print(current_time)

import calendar
print(calender.calendar(2025))

