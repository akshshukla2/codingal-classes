#23 table
for i in range(1, 11):
    print(23*i)

#star pattern
n=6
for i in range(1,n+1):
    for j in range(n+1,i,-1):
        print("*", end=" ")
    print(" ")