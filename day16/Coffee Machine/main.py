from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()

state = True
while state:
    choice = input(f"What would you like ({menu.get_items()[:-1]}): ").lower()
    if choice == "report":
        coffee_machine.report()
        money_machine.report()
    elif choice == "off":
        state = False
    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
