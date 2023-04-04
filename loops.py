##### Loops
# for loops and foreach loops
# for (you have to state how many times you want to do it)
# for each (for each element do sth)
# In Python just for loops that you can specify how you want to loop

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {
    1: {"name": "Bronson",
        "money": "$0.05"},
    2: {"name": "Masha",
        "money": "$3.66"},
    3: {"name": "Roscoe",
        "money": "$1.14"}
}
### Basic loop
# for num in list_data:
#     print(num * 2)


### Nested loop
# for data in embedded_lists:
#     print(data)
#     for num in data:
#         print(num)


### Looping for dictionaries
# for value in dict_data:
#     print(value)

# for item in dict_data.values():
#     print(item)

# for item in dict_data.values():
#     for embed_value in item.values():
#         print(embed_value)

# for items in dict_data.values():
#     print(items["money"])

# for num in list_data:
#     if num == 3:
#         print("I found three")
#     elif num > 3:
#         print("I've gone too far")
#     else:
#         print("Too soon")


### While loops (monitors the condition)
# x = 0
#
# while x < 10:
#     print(f"It's working -> {x}")
#     if x == 4:
#         break
#     x += 1

# Using while loops to verify user input

# age = input("What is your age?")
# print(f"Your age is {age}")

# user_prompt = True

# while user_prompt:
#     age = input("What is your age?")
#     if age.isdigit() and int(age) < 117:
#         user_prompt = False
#     else:
#         print("Please provide your age in digits, below 117")
#
# print(f"Your age is {age}")
