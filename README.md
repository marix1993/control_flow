# Task one
- Movie rating program
```
print("Could you please provide me your age?")

age_of_user = int(input())
if age_of_user >= 118 or age_of_user == 0:
    print("Please provide the right age.")
elif age_of_user >= 18:
    print("You can watch any movie.")
elif age_of_user >= 13:
    print("You can watch U movies.")
elif age_of_user <= 12:
    print("You can watch PG movies")
else:
    print("Wrong input.")
```
# Task two
- Odd & even numbers
```
print("Hi, please provide a number: ")

number_check = int(input())

if number_check % 2 == 0:
    print(f"{number_check} is even.")
else:
    print(f"{number_check} is odd.")
# or
# elif number_check % 2 != 0:
#     print(f"{number_check} is odd.")
```
- Random guess
```
import random

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
    print("Good guess.")
    exit()

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
    print("Good guess.")
    exit()

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
    print("Good guess.")
    exit()
```
- Random fizz buzz
```
import random

random_number = random.randint(1, 100)

if random_number % 3 == 0 and random_number % 5 == 0:
    print(f"{random_number} FizzBuzz")
elif random_number % 3 == 0:
    print(f"{random_number} Fizz")
elif random_number % 5 == 0:
    print(f"{random_number} Buzz")
else:
    print(random_number)
```

