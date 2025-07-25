num = int(input("Enter a number: "))
sum = 0
num2 = num

while num2 > 0:
    digit = num2 % 10
    sum += digit ** 3 
    num2 //= 10  

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
