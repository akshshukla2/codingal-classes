a = 60 #int
b = "Akshita" #string
c = 125.5 #float 

print(type(c)) # prints the type of var

d = int(c) #typecasting
print(d) 

print(2**4) #to the power 
print ( 66 // 7) # the ans will be floored.

e= " wow yay lovely"
print(len(e)) #prints length of e
print (e[4]) #index num
print (e[4:7]) #only yay will print

print(e*2) #will print 2 times

f = input("Enter your age.")
print(f)
print(type(f)) #string
g = int(input("Enter you age."))
print(type(g)) #will now print int type

h = a*4 + c + c/5 #follows BODMAS.
print(h)