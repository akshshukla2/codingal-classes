import os
if os.path.exists("sample.txt"):
    print("File exists and removing it.")
    os.remove("sample.txt")
else:
    print("Does not exists.")