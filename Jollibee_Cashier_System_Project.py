#Mar Louis Go
#Emmanuel Panong
#Mark Jason Gomez
cashier = input("Cashier: ")
main_menu = ["Burgers", "Rice Meals", "Jolly Hotdog", "Jolly Spaghetti", "Chickenjoy", "Chicken Joy Bucket", "Family Super Meals", "Sides & Soup", "Jollibee Kiddie Meals", "Breakfast Menu", "Desserts and Floats", "Stop Ordering"]
menu_1 = ["Yum Burger Value Meal [Y1]", "Yum Burger Cheese Value Meal [Y2]", "Bacon Cheese Yumburger Meal [Y3]", "Yumburger Cheese Deluxe Meal [Y4]", "Bacon Deluxe Cheese Yumburger Meal [Y5]", "Amazing Aloha Yumburger Value Meal [Y6]", "Yum Burger Champ Value Meal [Y7]", "Bacon Champ Value Meal [Y8]", "Amazing Aloha Champ Value Meal [Y9]"]
price_1 = [86.00, 96.00, 110.00, 120.00, 130.00, 135.00, 195.00, 230.00, 245.00]
menu_2 = ["1 pc Burger Steak w/ Drink [B1]", "2 pc Burger Steak w/ Drink [B2]", "1 pc Burger Steak with 3 pcs Shanghai w/ Drink [B3]", "1 pc Burger Steak w/ Fries & Drink [B4]", "Ultimate Burger Steak w/ Egg Meal & Drink", "Ultimate Burger Steak w/o Egg Meal & Drink", "Burger Steak Family Pan 6pcs [B7]", "Burger Steak Family Pan 8pcs [B8]"]
price_2 = [65.00, 90.00, 109.00, 79.0, 190.00, 175.00, 255.00, 339.00]
menu_3 = ["Jolly Hotdog Cheesy Classic w/ Drink [H1]", "Jolly Hotdog Cheesy Classic w/ Fries & Drink [H2]", "Jolly Hotdog Cheesy Classic w/ Fries & Float [H3]"]
price_3 = [80.00, 120.00, 125.00]
menu_4 = ["Jolly Spaghetti w/ Drink [S1]", "Jolly Spaghetti w/ Fries & Drink [S2]", "Jolly Spaghetti w/ Yumburger & Drink [S3]", "Jolly Spaghetti w/ Cheesy Yumburger & Drink [S4]", "Jolly Spaghetti w/ Burger Steak & Drink [S5]"]
price_4 = [65.00, 95.00, 95.00, 110.00, 99.00]
menu_5 = ["1 pc Chickenjoy w/ Rice & Drink [C1]", "1 pc Chickenjoy w/ Double Rice & Drink [C2]", "1 pc Chickenjoy w/ Jolly Spaghetti & Drink [C3]", "1 pc Chickenjoy w/ Palabok & Drink [C4]", "2 pcs Chickenjoy w/ Rice & Drink [C5]", "1 pc Chickenjoy w/ Rice, Fries & Drink [C6]"]
price_5 = [95.00, 99.00, 125.00, 175.00, 170.00, 105.00]
menu_6 = ["6 pc Chickenjoy Bucket", "8 pc Chickenjoy Bucket"]
price_6 = [399.00, 499.00]
menu_7 = ["Family Meal A – 6 pieces Chickenjoy Bucket, 3 rice, 3 sides, 3 sundaes, 3 drinks", "Family Meal A – 8 pieces Chickenjoy Bucket, 4 rice, 4 sides, 4 sundaes, 4 drinks", "Family Meal B – 6 pieces Chickenjoy Bucket, 3 spaghetti, 3 rice, 3 drinks", "Family Meal B – 8 pieces Chickenjoy Bucket, 4 spaghetti, 4 rice, 4 drinks"]
price_7 = [599.00, 799.00, 550.00, 799.00]
menu_8 = ["Jolly Crispy Fries (Regular)", "Jolly Crispy Fries (Large)", "Jolly Crispy Fries (Jumbo)", "1 pc Original Tuna Pie w/ Fries & Drink [P2]", "1pc Peach Mango Pie (Solo)", "1pc Buko Pie (Solo)", "1pc Ube Macapuno Pie (Solo)"]
price_8 = [42.00, 60.00, 75.00, 89.00, 30.00, 30.00, 30.00]
menu_9 = ["Yum Burger with Reg. Pineapple Juice + Toy", "Jolly Spaghetti with Reg. Pineapple Juice + Toy", "1 pc Chickenjoy with Reg. Pineapple Juice + Toy", "Burger Steak with Reg. Pineapple Juice + Toy"]
price_9 = [110.00, 116.00, 157.00, 116.00]
menu_10 = ["2 pc Pancake w/ Drink", "Hotdog w/ Garlic Rice, Fried Egg & Drink", "Breakfast Burger Steak w/ Garlic Rice, Fried Egg & Drink", "Beef Tapa w/ Garlic Rice, Fried Egg & Drink", "Corned Beef w/ Garlic Rice, Fried Egg & Drink", "Longganisa w/ Garlic Rice, Fried Egg & Drink", "Bacon, Egg & Cheese Pancake Sandwich w/ Drink", "Egg & Cheese Pancake Sandwich w/ Drink", "Egg & Cheese Sandwich w/ Drink"]
price_10 = [83.00, 109.00, 109.00, 142.00, 142.00, 142.00, 88.00, 77.00, 72.00]
menu_11 = ["Chocolate Sundae Twirl", "Coke, Sarsi or Royal Floats", "Vanilla Cone Twirl", "Chocolate Cone Twirl", "Mini Sundae Twirl"]
price_11 = [30.00, 37.00, 10.00, 15.00, 26.00]

order = []
quantity = []
order_price = []

print("Welcome to Jollibee!")
print("Jollibee Menu")


while True:
    for i in range(len(main_menu)):
        print(str(i + 1) + "." + main_menu[i])
    selection_num = int(input("Select Menu: "))
    if selection_num == 1:
        for i in range(len(menu_1)):
            print(str(i + 1) + "." + menu_1[i])

        while True:
            try:
                order_num = int(input("What would you like to order?: "))
                if order_num > 0 and order_num <= len(menu_1):
                    order.append(menu_1[order_num - 1])
                    order_price.append(price_1[order_num - 1])
                    print("Added " + menu_1[order_num - 1] + " to your order.")
                    print("Your order: " + str(order))
                    print("Your order price: " + str(order_price))
                    quantity_item = int(input("How much do you want to buy?: "))
                    quantity.append(quantity_item)
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")
            if input("Would you like to order more? (y/n) ") == "n":
                break

    elif selection_num == 2:
        for i in range(len(menu_2)):
            print(str(i + 1) + "." + menu_2[i])

        while True:
            try:
                order_num = int(input("What would you like to order?: "))
                if order_num > 0 and order_num <= len(menu_2):
                    order.append(menu_2[order_num - 1])
                    order_price.append(price_2[order_num - 1])
                    print("Added " + menu_2[order_num - 1] + " to your order.")
                    print("Your order: " + str(order))
                    print("Your order price: " + str(order_price))
                    quantity_item = int(input("How much do you want to buy?: "))
                    quantity.append(quantity_item)
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")
            if input("Would you like to order more? (y/n) ") == "n":
                break

    elif selection_num == 3:
        for i in range(len(menu_3)):
            print(str(i + 1) + "." + menu_3[i])

        while True:
            try:
                order_num = int(input("What would you like to order?: "))
                if order_num > 0 and order_num <= len(menu_3):
                    order.append(menu_3[order_num - 1])
                    order_price.append(price_3[order_num - 1])
                    print("Added " + menu_3[order_num - 1] + " to your order.")
                    print("Your order: " + str(order))
                    print("Your order price: " + str(order_price))
                    quantity_item = int(input("How much do you want to buy?: "))
                    quantity.append(quantity_item)
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")
            if input("Would you like to order more? (y/n) ") == "n":
                break

    elif selection_num == 4:
        for i in range(len(menu_4)):
            print(str(i + 1) + "." + menu_4[i])

        while True:
            try:
                order_num = int(input("What would you like to order?: "))
                if order_num > 0 and order_num <= len(menu_4):
                    order.append(menu_4[order_num - 1])
                    order_price.append(price_4[order_num - 1])
                    print("Added " + menu_4[order_num - 1] + " to your order.")
                    print("Your order: " + str(order))
                    print("Your order price: " + str(order_price))
                    quantity_item = int(input("How much do you want to buy?: "))
                    quantity.append(quantity_item)
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")
            if input("Would you like to order more? (y/n) ") == "n":
                break

    elif selection_num == 4:
        for i in range(len(menu_4)):
            print(str(i + 1) + "." + menu_4[i])

        while True:
            try:
                order_num = int(input("What would you like to order?: "))
                if order_num > 0 and order_num <= len(menu_4):
                    order.append(menu_4[order_num - 1])
                    order_price.append(price_4[order_num - 1])
                    print("Added " + menu_4[order_num - 1] + " to your order.")
                    print("Your order: " + str(order))
                    print("Your order price: " + str(order_price))
                    quantity_item = int(input("How much do you want to buy?: "))
                    quantity.append(quantity_item)
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")
            if input("Would you like to order more? (y/n) ") == "n":
                break

    elif selection_num == 5:
        for i in range(len(menu_5)):
            print(str(i + 1) + "." + menu_5[i])

        while True:
            try:
                order_num = int(input("What would you like to order?: "))
                if order_num > 0 and order_num <= len(menu_5):
                    order.append(menu_5[order_num - 1])
                    order_price.append(price_5[order_num - 1])
                    print("Added " + menu_5[order_num - 1] + " to your order.")
                    print("Your order: " + str(order))
                    print("Your order price: " + str(order_price))
                    quantity_item = int(input("How much do you want to buy?: "))
                    quantity.append(quantity_item)
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")
            if input("Would you like to order more? (y/n) ") == "n":
                break

    elif selection_num == 6:
        for i in range(len(menu_6)):
            print(str(i + 1) + "." + menu_6[i])

        while True:
            try:
                order_num = int(input("What would you like to order?: "))
                if order_num > 0 and order_num <= len(menu_6):
                    order.append(menu_6[order_num - 1])
                    order_price.append(price_6[order_num - 1])
                    print("Added " + menu_6[order_num - 1] + " to your order.")
                    print("Your order: " + str(order))
                    print("Your order price: " + str(order_price))
                    quantity_item = int(input("How much do you want to buy?: "))
                    quantity.append(quantity_item)
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")
            if input("Would you like to order more? (y/n) ") == "n":
                break

    elif selection_num == 7:
        for i in range(len(menu_7)):
            print(str(i + 1) + "." + menu_7[i])

        while True:
            try:
                order_num = int(input("What would you like to order?: "))
                if order_num > 0 and order_num <= len(menu_7):
                    order.append(menu_7[order_num - 1])
                    order_price.append(price_7[order_num - 1])
                    print("Added " + menu_7[order_num - 1] + " to your order.")
                    print("Your order: " + str(order))
                    print("Your order price: " + str(order_price))
                    quantity_item = int(input("How much do you want to buy?: "))
                    quantity.append(quantity_item)
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")
            if input("Would you like to order more? (y/n) ") == "n":
                break

    elif selection_num == 8:
        for i in range(len(menu_8)):
            print(str(i + 1) + "." + menu_8[i])

        while True:
            try:
                order_num = int(input("What would you like to order?: "))
                if order_num > 0 and order_num <= len(menu_8):
                    order.append(menu_8[order_num - 1])
                    order_price.append(price_8[order_num - 1])
                    print("Added " + menu_8[order_num - 1] + " to your order.")
                    print("Your order: " + str(order))
                    print("Your order price: " + str(order_price))
                    quantity_item = int(input("How much do you want to buy?: "))
                    quantity.append(quantity_item)
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")
            if input("Would you like to order more? (y/n) ") == "n":
                break

    elif selection_num == 9:
        for i in range(len(menu_9)):
            print(str(i + 1) + "." + menu_9[i])

        while True:
            try:
                order_num = int(input("What would you like to order?: "))
                if order_num > 0 and order_num <= len(menu_9):
                    order.append(menu_9[order_num - 1])
                    order_price.append(price_9[order_num - 1])
                    print("Added " + menu_9[order_num - 1] + " to your order.")
                    print("Your order: " + str(order))
                    print("Your order price: " + str(order_price))
                    quantity_item = int(input("How much do you want to buy?: "))
                    quantity.append(quantity_item)
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")
            if input("Would you like to order more? (y/n) ") == "n":
                break

    elif selection_num == 10:
        for i in range(len(menu_10)):
            print(str(i + 1) + "." + menu_10[i])

        while True:
            try:
                order_num = int(input("What would you like to order?: "))
                if order_num > 0 and order_num <= len(menu_10):
                    order.append(menu_10[order_num - 1])
                    order_price.append(price_10[order_num - 1])
                    print("Added " + menu_10[order_num - 1] + " to your order.")
                    print("Your order: " + str(order))
                    print("Your order price: " + str(order_price))
                    quantity_item = int(input("How much do you want to buy?: "))
                    quantity.append(quantity_item)
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")
            if input("Would you like to order more? (y/n) ") == "n":
                break

    elif selection_num == 11:
        for i in range(len(menu_11)):
            print(str(i + 1) + "." + menu_11[i])

        while True:
            try:
                order_num = int(input("What would you like to order?: "))
                if order_num > 0 and order_num <= len(menu_11):
                    order.append(menu_11[order_num - 1])
                    order_price.append(price_11[order_num - 1])
                    print("Added " + menu_11[order_num - 1] + " to your order.")
                    print("Your order: " + str(order))
                    print("Your order price: " + str(order_price))
                    quantity_item = int(input("How much do you want to buy?: "))
                    quantity.append(quantity_item)
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")
            if input("Would you like to order more? (y/n) ") == "n":
                break

    elif selection_num == 12:
        break

    else:
        print("Error")

total = 0

from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

print("")
print("-" * 80)
print("JBO766")
print("CUSTOMER COPY")
print("Cashier: ", cashier)
print("-" * 80)
print(dt_string)
print("-" * 80)
for i in range(len(order)):
    print(f"{quantity[i]} {order[i]} for {order_price[i]} each")
    total += quantity[i] * order_price[i]

print("")
print(f"Total: {total}")
print("*" * 80)