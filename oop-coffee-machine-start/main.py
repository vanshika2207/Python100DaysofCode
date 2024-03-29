from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Latte=MenuItem('latte',200,150,24,2.5)
Cappuccino=MenuItem('cappuccino',250,100,24,3.0)
Espresso=MenuItem('espresso',50,0,18,1.5)

# TODO 1. Print report
money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()

coffee_maker.report()
money_machine.report()

# TODO 2. CHECK RESOURCE SUFFICIENT
is_on=True
while is_on:
    options=menu.get_items()
    choice=input(f"What would you like ?{options}")
    if choice=='off':
        is_on=False
    elif choice=='report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost) :
                coffee_maker.make_coffee(drink)


