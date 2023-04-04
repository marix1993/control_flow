# Random fizz buzz
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
