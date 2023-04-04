### Make a loop with a range that says hello 10 times
x = 0
while x < 10:
    print("Hello.")
    x += 1

### Create another loop with a range that asks for names and appends to list_names
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

### Make a loop that iterates over each name in list_name
### and format's it into lowercase in a new variable
### called list_names_lower

list_names_lower = True

while list_names_lower:
    print(str(list_names).lower())
    list_names_lower = False

## Make a list of numbers, iterate over
### the list of values to find if the are even

# number_list = [1, 2, 3, 4, 5] - dunno how to do that one