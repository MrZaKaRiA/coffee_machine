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


# Repurort function for machin resources.
def report():
  water = resources["water"]
  milk = resources["milk"]
  coffee = resources["coffee"]
  return f"""Water: {water}ml
Milk: {milk}ml
Coffee: {coffee}g"""

# Payment function for our coffee machine
def process_coins():
  """Financial transactions."""
  # Enter coins.
  print("Please insert coins.")
  quaters = 0.25 * int(input("How many quaters?: "))
  dimes = 0.10 * int(input("How many dimes?: "))
  nickles = 0.05 * int(input("How many nickles?: "))
  pennies = 0.01 * int(input("How many pennies?: "))

  # Check if the amount is enough or not , and give the client remainder or refunde.
  global profit
  profit = max([quaters, dimes, nickles, pennies])
  cost = MENU[drink]["cost"]

  if profit >= cost:
    remainder_amount = profit - cost
    print(f"Here is ${remainder_amount} in change.")
    print(f"Here is your {drink} ☕️ . Enjoy!")
  else:
    print("Sorry that's not enough money. Money refunded.")
  profit = 0


def order_service(resources, drink):
  """Prepare coffee and check resources."""
  if drink == "report":
    print(report())
  elif drink == "off":
    return False
  else:
    # Check resources sufficient .
    ingredients_drink = MENU[drink]["ingredients"]
    for key in ingredients_drink:
      if resources[key] < ingredients_drink[key]:
        print(f"Sorry there is not enough {key}")
        return True

    # Take the content we need from resources.
    for key in ingredients_drink:
      resources[key] -= ingredients_drink[key]

    process_coins()



# Repeatability steps.
should_continue = True
while should_continue:
  # Drinks we have for clients, would drink.
  drink = input(" What would you like? (espresso/latte/cappuccino): ").lower()

  # Prepare drink for clinte
  should_continue = order_service(resources, drink)
