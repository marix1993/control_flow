# Write a program that takes user input until the user enters 0.
# Once they do, sum all the positive numbers they entered
# and all of the negative numbers they entered and print the result back to them.

import sys

user_input_list = []

user_numbers = True

while user_numbers:
    user_input = int(input("Please provide a number, if you're ready type 0 and I'll sum your numbers: "))
    if user_input != 0:
        user_input_list.append(user_input)
    else:
        sum1 = sum(user_input_list) / len(user_input_list)
        print(f"Sum of your numbers: {sum1}")
        sys.exit()
