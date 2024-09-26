import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    while True:
        print("Welcome to the Sandwich Maker program!")
        choice = input("What size of sandwich would you like? (small, medium, large) or 'exit' to quit: ").lower()
        
        if choice == 'exit':
            print("Thank you for visiting!")
            break
        
        if choice in recipes:
            cost = recipes[choice]['cost']
            print(f"The cost of a {choice} sandwich is ${cost:.2f}.")
            print("Please insert coins.")
            inserted_coins = cashier_instance.process_coins()

            if cashier_instance.transaction_result(inserted_coins, cost):
                if sandwich_maker_instance.make_sandwich(choice, recipes[choice]['ingredients']):
                    print(f"Enjoy your {choice} sandwich!")
                else:
                    print("Sorry, not enough resources to make your sandwich.")
            else:
                print("Insufficient funds. Please try again.")
        else:
            print("Invalid choice. Please select a valid sandwich size.")

if __name__=="__main__":
    main()
