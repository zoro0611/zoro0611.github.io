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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
moneyEarned = 0
# coinObject = {
#     "quarters": 0,
#     "dimes":0,
#     "nickles":0,
#     "pennies":0
# }
def AskAction():
    action = input("What would you like? (espresso/latte/cappuccino):")
    return action
def CompareInsertCoins(coinObj, drink):
    global moneyEarned
    total = coinObj["quarters"] * 0.25 + coinObj["dimes"] * 0.1 + coinObj["nickles"] * 0.05 + coinObj["pennies"] * 0.01
    if total < MENU[drink]["cost"]:
        return "Sorry that's not enough money. Money refunded."
    elif total == MENU[drink]["cost"]:
        moneyEarned += MENU[drink]["cost"]
        return "Here is your " + drink + ". Enjoy!"
    else:
        moneyEarned += MENU[drink]["cost"]
        return "Here is your " + drink + " and " + str(round(total - MENU[drink]["cost"], 2)) + " dollars in change."
def AskInsertCoins():
    coinObj = {
        "quarters": int(input("How many quarters?:")),
        "dimes": int(input("How many dimes?:")),
        "nickles": int(input("How many nickles?:")),
        "pennies": int(input("How many pennies?:"))
    }
    return coinObj
def CheckResources(drink):
    #if drink doesnt need milk, then milk is not in the ingredients
    if "milk" not in MENU[drink]["ingredients"]:
        if resources["water"] < MENU[drink]["ingredients"]["water"]:
            return "Sorry there is not enough water."
        elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
            return "Sorry there is not enough coffee."
        else:
            return "True"
    else:
        if resources["water"] < MENU[drink]["ingredients"]["water"]:
            return "Sorry there is not enough water."
        elif resources["milk"] < MENU[drink]["ingredients"]["milk"]:
            return "Sorry there is not enough milk."
        elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
            return "Sorry there is not enough coffee."
        else:
            return "True"
def DeductResources(drink):
    if "milk" not in MENU[drink]["ingredients"]:
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
def PrintReport():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money Earned: $" + str(moneyEarned))

continueFlag = True
while continueFlag:
    action = AskAction()
    if action == "report":
        PrintReport()
    elif action == "off":
        continueFlag = False
    elif action == "espresso" or action == "latte" or action == "cappuccino":
        #get action's cost
        actionCost = MENU[action]["cost"]
        print(f"{action} costs ${actionCost}")
        if CheckResources(action) == "True":
            coinObj = AskInsertCoins()
            print(CompareInsertCoins(coinObj, action))
            DeductResources(action)
        else:
            print(CheckResources(action))
    else:
        print("Invalid input. Please try again.")