#making a function
def func():
    print("This is a function.")

func()

#making a parameterized function

def add(a,b):
    print("The sum =", (a+b))

add(6,4)


#return function

def mult(x,y,z):
    return x*y*z

m = mult(2,3,4)

print("The product=", m)

#factorial
def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

f2 = fact(3)
print("The factorial =", f2)

#factorial using recursion
def recur(n):
    if n==1:
        return 1
    else:
        return n*recur(n-1)

print("The factorial using recursion=", recur(6))
