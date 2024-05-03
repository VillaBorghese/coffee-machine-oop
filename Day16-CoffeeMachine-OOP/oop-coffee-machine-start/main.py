from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
machine = CoffeeMaker()
account = MoneyMachine()
switch = True


while switch :
    # ask and display the menu
    print("What would you like to drink ?")
    print(menu.get_items())
    drink=input("->").lower()

    if drink == "report":
        machine.report()
        account.report()
        print("\n")

    elif drink == "off":
        switch = False

    else:
        beverage = menu.find_drink(drink)
        if machine.is_resource_sufficient(beverage):
            if account.make_payment(beverage.cost):
                machine.make_coffee(beverage)
