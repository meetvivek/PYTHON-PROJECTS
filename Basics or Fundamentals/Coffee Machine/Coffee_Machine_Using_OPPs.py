from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_execute = True
CoffeeMaker = CoffeeMaker()
MoneyMachine = MoneyMachine()
Menu = Menu()

while is_execute:
    options = Menu.get_items()
    user_choice = input(f"What would you like? {options}: ").lower()
    if user_choice == 'off':
        is_execute = False
    elif user_choice == 'report':
        CoffeeMaker.report()
        MoneyMachine.report()
    else:
        drink = Menu.find_drink(user_choice)
        if CoffeeMaker.is_resource_sufficient(drink) and MoneyMachine.make_payment(drink.cost):
            CoffeeMaker.make_coffee(drink)


