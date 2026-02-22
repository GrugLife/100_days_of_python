MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def report(resources):
    return resources


def turn_off(off):
    if off == "off":
        return False
    else:
        return True


def menu():
    return input("What would you like? (espresso/latte/cappuccino): ")


def check_resources(MENU, resources, item):
    for key, value in MENU[item]["ingredients"].items():
        if value <= resources[key]:
            print(f"There is enough {key} remaining for this order")
        else:
            print(f"not enough {key} for this order")
            return False
    return True


def transaction(item, MENU, resources):
    q = int(input("How many quarters: "))
    d = int(input("How many dimes: "))
    n = int(input("How many nickles: "))
    p = int(input("You are seriously paying with pennies: "))
    total_paid = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)
    price_coffee = MENU[item]["cost"]
    if total_paid >= price_coffee:
        print(
            f"Successful Transaction: your change is ${total_paid - price_coffee:.2f}"
        )
        resources["money"] += MENU[item]["cost"]
        print(resources)
        return True
    else:
        print("not enough monies")
        return False


def make_coffee(item, MENU, resources):
    print("Makeing your coffee...........\n")
    for key, value in MENU[item]["ingredients"].items():
        resources[key] -= value
    print("your coffee is ready")
    print(f"remaining resources: {resources}")


def main():
    is_on = True
    while is_on:
        choice = menu()

        if choice == "off":
            print("shutting down...Goodbye!")
            is_on = False
        elif choice == "report":
            resource_report = report(resources)
            print("--- Current Status ---")
            for key, value in resource_report.items():
                print(f"{key}: {value}")
            print("----------------------")
        else:
            if choice in MENU:
                if check_resources(MENU, resources, choice):
                    if transaction(choice, MENU, resources):
                        make_coffee(choice, MENU, resources)
                    else:
                        print("You did not pay enough monies")
                else:
                    print("Not enough resources to make your coffee")


if __name__ == "__main__":
    main()
