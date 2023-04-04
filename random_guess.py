# Random guess
import random
import sys

number = random.randint(1, 20)
print("Hi, please choose random number between 1-20")
user_number = int(input())

if user_number > 20:
    print("The number is too high, choose a number between 1-20.")
elif user_number == 0:
    print("You can't choose 0, choose a number between 1-20.")
elif user_number > number:
    print("Almost, bit too high. Choose one more time.")
elif user_number < number:
    print("Almost, too low. Choose one more time.")
else:
    sys.exit(print("Good guess."))

print("You have 2 more tries.")
user_number = int(input())

if user_number > 20:
    print("The number is too high, choose a number between 1-20.")
elif user_number == 0:
    print("You can't choose 0, choose a number between 1-20.")
elif user_number > number:
    print("Almost, bit too high. Choose one more time.")
elif user_number < number:
    print("Almost, too low. Choose one more time.")
else:
    sys.exit(print("Good guess."))

print("Last try.")
user_number = int(input())
if user_number > 20:
    print("The number is too high, choose a number between 1-20.")
elif user_number == 0:
    print("You can't choose 0, choose a number between 1-20.")
elif user_number > number:
    print("Almost, bit too high. Maybe next time.")
elif user_number < number:
    print("Almost, too low. Maybe next time")
else:
    sys.exit(print("Good guess.")) # Best option

# else:
#   raise Exception("Good guess")

# can't use break in loop
# last time I used exit()
