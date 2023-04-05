# Starters
starters = ["nuggets", "ribs", "fish_fingers"]
# Main
mains = ["steak", "fish", "lamb"]
# Dessert
dessert = ["icecream", "cookie", "cake"]

print("Hi, how can I help? This is our menu: \n"
      + "Starters: \n" + str(starters)
      + "\nMains: \n" + str(mains)
      + "\nDesserts: \n" + str(dessert))

order_list = []

ordering = True

while ordering:
    # Ordering starter:
    starters_order = input("What starter from the menu would you like?")
    if starters_order in starters:
        order_list.append(starters_order)
        print(f"{order_list[0]} added")
    else:
        print("Choose something from the menu")
        continue
    # Ordering main:
    while ordering:
        main_order = input("What main from the menu would you like?")
        if main_order in mains:
            order_list.append(main_order)
            print(f"{order_list[1]} added")
        else:
            print("Choose something from the menu")
            continue
        # Ordering dessert:
        while ordering:
            dessert_order = input("What dessert from the menu would you like?")
            if dessert_order in dessert:
                order_list.append(dessert_order)
                print(f"{order_list[2]} added")
                ordering = False
            else:
                print("Choose something from the menu")
                continue

print(f"This is your order: {order_list}")
