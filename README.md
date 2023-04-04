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

# Make a loop with a range that says hello 10 times

```
x = 0
while x < 10:
    print("Hello.")
    x += 1
```

# Create another loop with a range that asks for names and appends to list_names

```
list_names = ["Mark", "Bob", "Karen"]

user_name = True

while user_name:
    name = input("What's your name?")
    if name.isdigit():
        user_name = False
    else:
        list_names.append(name)
        break

print(f"Thank you {name}")
print(list_names)
```

# Make a loop that iterates over each name in list_name and format's it into lowercase in a new variable called list_names_lower

```
list_names_lower = True

while list_names_lower:
    print(str(list_names).lower())
    list_names_lower = False
```

# Take 10 integers from the user and print their average value once you have them all

```
print("Hi, today I'm going to provide you the average number of your inputs.\n"
      "Could you give me your numbers?")
number1 = int(input())
number2 = int(input())
number3 = int(input())
number4 = int(input())
number5 = int(input())
number6 = int(input())
number7 = int(input())
number8 = int(input())
number9 = int(input())
number10 = int(input())

numbers_list = [number1, number2, number3, number4, number5, number6, number7, number8, number9, number10]

print(numbers_list)

average_from_numbers = sum(numbers_list) / len(numbers_list)
print(f"Your average is: {average_from_numbers}")
```

# Write a while loop to print the following series:10, 20 ,30, 40 etc. up to 300

```
number = 10

while number <= 300:
    print(number)
    number += 10
```