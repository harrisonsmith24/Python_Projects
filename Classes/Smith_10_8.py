# Harrison Smith
# Professor Carman CPT 187 Y01
# 4/19/2021
# This program should allow the user to select from a list of items for purchase. The program should allow the user to
# Place these items in their cart, review their items for purchase, confirm whether they want to checkout, and give them
# a total price.

# Importing the retailItem class
import retailItem
# Import the cashRegister class
import cashRegister


# Defining the main function
def main():

    # Setting a variable for each retail item that is for sale according to the parameters set by the retailItem class
    thePants = retailItem.RetailItem("Pants", 10, 29.95)
    theShirt = retailItem.RetailItem("Shirts", 10, 15.99)
    theShoes = retailItem.RetailItem("Shoes", 20, 40.95)
    theBelt = retailItem.RetailItem("Belts", 15, 8.95)

    # Setting the calling of the class to a variable to condense the amount of code needed to write to make the program
    # easier to read
    cashReg = cashRegister.CashRegister()
    # Setting a variable for the while loop to run
    checkOut = "N"

    # Using a while loop to add items that the user chooses to the cart.
    while checkOut == "N":
        # Printing a menu prompt so the user knows how to operate the program
        print("Enter 1 for Pants")
        print("Enter 2 for Shirts")
        print("Enter 3 for Shoes")
        print("Enter 4 for Belts")
        print()

        # Prompting the user choose if the want to checkout or to continue shopping.
        userChoice = int(input("Please enter an item number: "))

        # Using an if statement for thePants item and setting the input to 1
        if userChoice == 1:
            # Using an if statement to check the inventory for the given retail item
            if thePants.getInv() >= 1:
                # Using the cashRegister class to confirm that the user wants to purchase pants
                cashReg.purchaseItems(thePants)
                # Using the retailItems class to get the inventory of the pants
                tempInvPants = thePants.getInv()
                # For each item purchased, subtract one from the inventory
                thePants.setInv(tempInvPants-1)
            # If the temporary inventory drops below 1 then execute the else statement
            else:
                print("This item is out of stock!")
        # Using an if statement for theShirts item and setting the input to 2
        elif userChoice == 2:
            # Using an if statement to check the inventory for the given retail item
            if theShirt.getInv() >= 1:
                # Using the casRegister class to confirm that the user wants to purchase shirts
                cashReg.purchaseItems(theShirt)
                # Using the retailItems class to get the inventory of the shirts
                tempInvShirt = theShirt.getInv()
                # For each item purchased, subtract one from the inventory
                thePants.setInv(tempInvShirt - 1)
            # If the temporary inventory drops below 1 then execute the else statement
            else:
                print("This item is out of stock!")
        # Using an if statement for theShoes item and setting the input to 3
        elif userChoice == 3:
            # Using an if statement to check the inventory for the given retail item
            if theShoes.getInv() >= 1:
                # Using the casRegister class to confirm that the user wants to purchase Shoes
                cashReg.purchaseItems(theShoes)
                # Using the retailItems class to get the inventory of the shoes
                tempInvShoes = theShoes.getInv()
                # For each item purchased, subtract one from the inventory
                thePants.setInv(tempInvShoes - 1)
            # If the temporary inventory drops below 1 then execute the else statement
            else:
                print("This item is out of stock!")
        # Using an if statement for theBelt item and setting the input to 4
        elif userChoice == 4:
            # Using an if statement to check the inventory for the given retail item
            if theBelt.getInv() >= 1:
                # Using the casRegister class to confirm that the user wants to purchase belts
                cashReg.purchaseItems(theBelt)
                # Using the retailItems class to get the inventory of the belts
                tempInvBelt = theBelt.getInv()
                # For each item purchased, subtract one from the inventory
                thePants.setInv(tempInvBelt - 1)
            # If the temporary inventory drops below 1 then execute the else statement
            else:
                print("This item is out of stock!")
        # Setting a catch all for any entry that was not given.
        else:
            print("Incorrect Entry")

        # Give the user a prompt to checkout
        checkOut = input("Checkout? Enter N to continue: ")
        print()

    # Show the items in the cart
    cashReg.showItems()

    # Print the final total
    print("The final total is: " + format(cashReg.getTotal(), '.2f'))


# Call the main function
main()