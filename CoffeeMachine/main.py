from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

is_on = True
while is_on:
    menu_items = menu.get_items()
    user_choice = input(f'What would you like? ({menu_items}): ').lower()
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        coffee_maker.report()
        money.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
