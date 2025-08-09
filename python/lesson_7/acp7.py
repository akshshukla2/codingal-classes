import random

s = random.randint(1, 100)

while True:
    g = int(input("Guess the number (1-100): "))
    if g == s:
        print("Correct!")
        break
    elif g < s:
        print("Too low!")
    else:
        print("Too high!")
