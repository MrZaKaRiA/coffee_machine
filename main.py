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
Coffee: {coffee}g
Money: ${profit}"""

# Payment function for our coffee machine
def process_coins():
  """Financial transactions."""
  # Enter coins.
  print("Please insert coins.")
  total = 0.25 * int(input("How many quaters?: "))
  total += 0.10 * int(input("How many dimes?: "))
  total += 0.05 * int(input("How many nickles?: "))
  total += 0.01 * int(input("How many pennies?: "))

  # Check if the amount is enough or not , and give the client remainder or refunde.
  global profit
  cost = MENU[choice]["cost"]

  if total >= cost:
    profit += cost
    remainder_amount = total - cost
    print(f"Here is ${remainder_amount} in change.")
    print(f"Here is your {choice} ☕️ . Enjoy!")
  else:
    print("Sorry that's not enough money. Money refunded.")


def is_resource_sufficient(order_ingredients):
  for key in order_ingredients:
    if resources[key] < order_ingredients[key]:
      print(f"Sorry there is not enough {key}")
      return True
  return True

def order_service(resources, choice):
  """Prepare coffee and check resources."""
  if choice == "off":
    return False

  elif choice == "report":
    print(report())
    return True
  else:
    # Check resources sufficient .
    if not is_resource_sufficient(MENU[choice]['ingredients']):
      return True

    process_coins()

    # Take the content we need from resources.
    for key in MENU[choice]['ingredients']:
      resources[key] -= MENU[choice]['ingredients'][key]




# Repeatability steps.
is_on = True
while is_on:
  # Drinks we have for clients, would drink.
  choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()

  # Prepare drink for clinte
  is_on = order_service(resources, choice)
