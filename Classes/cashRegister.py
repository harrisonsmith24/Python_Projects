# Declaring the CashRegister class
class CashRegister:

    # Initialize the constructor for the CashRegister class
    def __init__(self):
        # defining the itemToPurchase attribute as a list
        self.__itemsToPurchase = []

    # Defining a method to clear the items to purchase list
    def clearList(self):
        # Resetting the information in the list to be nothing
        self.__itemsToPurchase = []

    # Defining a method to append the items the user chooses to purchase to the list
    def purchaseItems(self, retailItem):
        # Appending the items to the itemsToPurchase list
        self.__itemsToPurchase.append(retailItem)
        # Confirmation print
        print("Item added to cart!")

    # Defining a method to get the total price for the items the user wants to purchase
    def getTotal(self):
        # Declaring a final total variable to store the information
        finalTotal = 0

        # Using a for loop to loop through the items the user wants to purchase and adding them together.
        for item in self.__itemsToPurchase:
            # Adding the price of each item together and setting it to the final total
            finalTotal += item.getPrice()

        # Return the final total
        return finalTotal

    # Defining a function to show the items that are placed in the cart.
    def showItems(self):
        # Printing the items to the console.
        print('The items in the cart are: ')

        # Using a for loop to iterate through the list.
        for item in self.__itemsToPurchase:
            # Printing the selected item.
            print(item)
            print()
