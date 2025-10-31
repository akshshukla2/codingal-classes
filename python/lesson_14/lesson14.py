file = open('python\lesson_14\sample2.txt','r')

#firstline = file.readline()
#secondline = file.readline()
#print(firstline)
#print(secondline)

alllines = file.readlines()

#print(alllines)

for line in alllines:
    print(line)

file.close()