# Odd & even numbers

print("Hi, please provide a number: ")

number_check = int(input())

if number_check % 2 == 0:
    print(f"{number_check} is even.")
else:
    print(f"{number_check} is odd.")
# or
# elif number_check % 2 != 0:
#     print(f"{number_check} is odd.")
