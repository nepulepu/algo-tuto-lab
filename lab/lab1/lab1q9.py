import random


randomnum=random.randint(1,9)

guess=eval(input("Guess number from 1 to 9: "))

if guess<randomnum:
    print("TOO LOW")
elif guess>randomnum:
    print("TOO HIGH")
else:
    print("EXACTLY RIGHT")