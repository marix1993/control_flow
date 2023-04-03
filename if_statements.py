# if, elif and else (set a criteria and check if they are...)

age = 12

# if age >= 18:
#     print("You can buy a ticket")
# if age < 18:
#     print("Sorry, you are too young.")

# if age >= 18:
#     print("You can buy a ticket")
# elif age < 18:
#     print("Sorry, you are too young.")

# elif and else

film_rating = "ee"

if film_rating.lower() == "universal":
    print("All ages can watch this movie.")
elif film_rating.lower() == "pg":
    print("Parental guidance")
elif film_rating.lower() == "12":
    print("You must be at least 12 years old to watch it.")
elif film_rating.lower() == "15":
    print("You must be at least 15 to watch.")
elif film_rating.lower() == "18":
    print("You must be at least 18 to watch.")
else:
    print("Sorry, wrong input")

# THERE ARE NO SWITCH OR CASE STATEMENTS IN PYTHON


