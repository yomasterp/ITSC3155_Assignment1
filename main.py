### Data ###
from idlelib.configdialog import changes

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        """Commit #1"""
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry, not enough resources for {item}.")
                return False
            return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        """Commit #2"""

        print("Please insert coins.")
        total_coins = 0
        total_coins += int(input("How many large dollars?: ")) * 1.00
        total_coins += int(input("How many half dollars?: ")) * 0.50
        total_coins += int(input("How many quarters?: ")) * 0.25
        total_coins += int(input("How many nickels?: ")) * 0.05
        return total_coins


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        """Commit #3"""

        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is {change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        """Commit #4"""

        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]

            print(f"{sandwich_size} sandwich is ready! Bon appetit!")

### Make an instance of SandwichMachine class and write the rest of the codes ###

### This is a test comment! ###

sandwich_machine = SandwichMachine(resources)

while True:
    choice = input("Would you like? (small/medium/large/off/report): ").lower()
    if choice == "off":
        break

    elif choice == "report":
        print(f"Bread: {sandwich_machine.machine_resources['bread']} slice(s) available.")
        print(f"Ham: {sandwich_machine.machine_resources['ham']} slice(s) available.")
        print(f"Cheese: {sandwich_machine.machine_resources['cheese']} ounce(s) available.")

    elif choice in recipes:
        sandwich = recipes[choice]
        if sandwich_machine.check_resources(sandwich["ingredients"]):
            payment = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(payment, sandwich["cost"]):
                sandwich_machine.make_sandwich(choice, sandwich["ingredients"])

    else:
        print(f"Invalid Selection. Please choose another option.")