# imports
import random

Colors = ["Blue", "Red", "Yellow", "Green"]
pick = random.choice(Colors)
print(pick)
print("Please guess the color out of this list: " + str(Colors))
user_pick = input()
count = 1
user = False

while count < 3:
    if user_pick.upper() == pick.upper():
        count = count + 1
        user = True
        print("Success")
        break
    else:
        user_pick = input()
        count = count + 1
        user = False
        print("Error")


print("Ygal")