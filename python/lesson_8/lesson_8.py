a= ['word1','word2','word3','word4','word5','word6']

print(type(a)) #class type
print(a[2])#index print
print(a[1:4:1]) #subsring
print(len(a)) #length

for i in a:
    print(i)

a2= ['word1','word2',('word3','word4','word5'),'word6']
print(a2[2][1])

#set

a3= { 1,2,2,2,2,3,4,5,6,7,8,9,10 }
print(a3)

a3.add(11)
print(a3)

a4={4,5,6,7,8,9,10,11}

print(a3.difference(a4))
print(a3.symmetric_difference(a4))
print(a3.union(a4))
print(a3.intersection(a4))