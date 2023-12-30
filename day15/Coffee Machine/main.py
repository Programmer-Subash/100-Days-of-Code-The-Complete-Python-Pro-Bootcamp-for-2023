from menu import MENU
from resource import resources
from resource import profit


#function that print report
def display_report():
    """Display report """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Profit: ${profit}")


#take coins as input from user and return total amount
def total_amount():
    """take coin from user and return total amount"""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total


#check resources sufficient
def is_sufficient_resource(coffee_name):
    """return True if resources are sufficient to make coffee otherwise return False"""
    for key in MENU[coffee_name]["ingredients"]:
        if resources[key] < MENU[coffee_name]["ingredients"][key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


#check transaction successful
def is_successful_transaction(coffee_name,total_amount:float):
    """return True if user insert enough coin to make coffee otherwise return False"""
    if total_amount >= MENU[coffee_name]["cost"]:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


#add profit
def add_profit(coffee_name):
    """add profit to coffee machine"""
    global profit
    profit += MENU[coffee_name]["cost"]


#update resources
def update_resource(coffee_name):
    """update resources after making coffee"""
    for key in MENU[coffee_name]["ingredients"]:
        resources[key] -= MENU[coffee_name]["ingredients"][key]


#return change
def return_change(coffee_name,total_amount):
    if total_amount > MENU[coffee_name]["cost"]:
        change = total_amount - MENU[coffee_name]["cost"]
        change = round(change,2)
        print(f"Here is ${change} in change.")


def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "report":
            display_report()
        elif choice == "off":
            print(f"Coffee Machine is Turn off.")
            break
        elif choice in MENU:

            #check is there are suffiecient resource
            sufficient_resource = is_sufficient_resource(choice)
            if not sufficient_resource:
                continue

            #ask user to insert coin
            amount = total_amount()

            #check if user insert sufficient coin
            successful_transaction = is_successful_transaction(choice,amount)
            if successful_transaction:

                add_profit(choice)

                # return change
                return_change(choice, amount)

                # update resource
                update_resource(choice)

                print(f"Here is your {choice} ☕ Enjoy!")
            else:
                continue
        else:
            print("Invalid")
            continue

coffee_machine()