class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        
        total = 0
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))        
        nickels = int(input("How many nickels?: "))    
        pennies = int(input("How many pennies?: "))

    total += quarter * 0.25
    total += dimes * 0.10
    total += nickels * 0.05
    total += pennies * 0.01

    return total


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        return coins >= cost
