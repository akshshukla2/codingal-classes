num = int(input("Enter a number: "))
sum = 0
num2 = num

while num2 > 0:
    digit = num2 % 10
<<<<<<< HEAD
    sum += digit ** 3 
=======
    sum += digit ** 3  
>>>>>>> da07418d3eb1012855c3dc01e9f7c01e4afabcec
    num2 //= 10  

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
