# Menu and resources.
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
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#report machine resources
def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return f"""Water: {water}ml
Milk: {milk}ml
Coffee: {coffee}g"""

#payment
def process_coins(drink, cost):
  """Financial transactions."""
  
    print("Please insert coins.")
    quarters = 0.25 * int(input("How many quarters?: "))
    dimes = 0.10 * int(input("How many dimes?: "))
    nickels = 0.05 * int(input("How many nickels?: "))
    pennies = 0.01 * int(input("How many pennies?: "))

    total_payment = quarters + dimes + nickels + pennies

    if total_payment >= cost:
        remainder_amount = total_payment - cost
        print(f"Here is ${remainder_amount} in change.")
        print(f"Here is your {drink} ☕️. Enjoy!")
    else:
        print("Sorry, that's not enough money. Money refunded.")


def check_resources(drink):
    ingredients_drink = MENU[drink]["ingredients"]

    for ingredient, amount in ingredients_drink.items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False

    for ingredient, amount in ingredients_drink.items():
        resources[ingredient] -= amount

    return True


def order_service(resources):
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink == "report":
        print(report())
    elif drink == "off":
        return False
    else:
        if check_resources(drink):
            cost = MENU[drink]["cost"]
            process_coins(drink, cost)

    return True


should_continue = True
while should_continue:
    should_continue = order_service(resources)
