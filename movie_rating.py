# Movie rating program
import sys

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
