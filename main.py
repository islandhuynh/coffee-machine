resources = {
  "water" : 300,
  "milk" : 200,
  "coffee" : 100,
  "money": 0
}

coffees = {
  "expresso" : {
    "water" : 50,
    "milk" : 0,
    "coffee" : 18,
    "cost": 150
  },
  "latte" : {
    "water" : 200,
    "milk" : 150,
    "coffee" : 24,
    "cost": 250
  },
  "cappuccino" : {
    "water" : 250,
    "milk" : 100,
    "coffee" : 24,
    "cost": 300
  }
}

def print_report():
  print(f'Water: {resources["water"]}ml')
  print(f'Milk: {resources["milk"]}ml')
  print(f'Coffee: {resources["coffee"]}g')
  print(f'Money: ${resources["money"]/ 100 }')

def check_inventory(coffee):
  if resources["water"] < coffees[coffee]["water"]:
    print("Sorry there is not enough water.")
    return False
  if resources["milk"] < coffees[coffee]["milk"]:
    print("Sorry there is not enough milk.")
    return False
  if resources["milk"] < coffees[coffee]["milk"]:
    print("Sorry there is not enough milk.")
    return False
  return True

def make_coffee(coffee):
  resources["water"] -= coffees[coffee]["water"]
  resources["milk"] -= coffees[coffee]["milk"]
  resources["coffee"] -= coffees[coffee]["coffee"]

while True:
  user_choice = input("What would you like? (expresso/ latte/ cappuccino): ").lower()
  if user_choice == "report":
    print_report()
  elif user_choice == "off":
    break
  elif not user_choice in coffees:
    print("Please provide a valid input")
  else:
    enough_resource = check_inventory(user_choice)
    if enough_resource:
      print("Please insert coins.")
      quarters = int(input("How many quarters?: "))
      dimes = int(input("How many dimes?: "))
      nickels = int(input("How many nickels?: "))
      pennies = int(input("How many pennies?: "))
      total = quarters * 25 + dimes * 10 + nickels * 5 + pennies
      if coffees[user_choice]["cost"] > total:
        print("Sorry that's not enough money. Money refunded.")
      else:
        resources["money"] += coffees[user_choice]["cost"]
        change = (total - coffees[user_choice]["cost"]) / 100
        print(f"Here is ${change} in change.")
        make_coffee(user_choice)
        print(f"Here is your {user_choice}. Enjoy!")
  
  