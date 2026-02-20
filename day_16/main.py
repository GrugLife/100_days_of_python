from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
moneyMachine = MoneyMachine()


def main():
    is_on = True
    while is_on:
        coffee = coffee_menu.get_items()
        choice = input(f"What would you like {coffee}: ")

        if choice == "off":
            print("shutting down...Goodbye!")
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            moneyMachine.report()
        else:
            drink = coffee_menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink):
                # moneyMachine.process_coins()
                if moneyMachine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)


main()
