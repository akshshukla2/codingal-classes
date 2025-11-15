with open("sample.txt" , "w") as file:
    file.write("Today's class was interesting.")

with open("sample.txt", "r") as file:
    print(file.read())

with open("sample.txt", "r") as file:
    r = file.readlines()
    for line in r:
        w = line.split()
        print(w)


