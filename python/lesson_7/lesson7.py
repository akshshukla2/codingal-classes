a= ['word1','word2','word3','word4','word5','word6']

print(type(a)) #class type
print(a[2])#index print
print(a[1:4:1]) #subsring
print(len(a)) #length
a.append('word7')
print(a) #added a word
a.remove('word3')
print(a) # removed a word
a.pop()
print(a)# the last word got removed
a.reverse()
print(a)#whole list got reversed
a.sort()
print(a)# sorted alphabetical order
a.clear()
print(a) # list cleared so empty
print(type(a))

dict = { 'a' : "AKSHITA", 'b' : "CLASS 12" , 'c' : "19" , 'd' : "SCIENCE"}
print(dict)
print(type(dict))
print(dict['b'])
dict['e']='FEMALE'
print(dict)
dict.pop('c')
print(dict)
print(dict.get('d'))
dict.clear()
print(dict) 