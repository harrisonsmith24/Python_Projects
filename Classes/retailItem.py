# Declaring the RetailItem class
class RetailItem:

    # Initialize the constructor for the RetailItem class
    def __init__(self, itemDescription, itemInv, itemPrice):
        # Setting each argument for the __init__ method to the attribute with the corresponding name.
        self.__itemDescription = itemDescription
        self.__itemInv = itemInv
        self.__itemPrice = itemPrice

    # Using the __str__ method to return a string indicating the objects state.
    def __str__(self):
        # Printing a line of information for each attribute.
        theOutput = 'Decription: ' + str(self.getDescription()) + \
                    '\nInventory: ' + str(self.getInv()) + \
                    '\nPrice: \t' + str(self.getPrice())
        # return the output to be printed to the console
        return theOutput

    # Setting the item's description
    def setDescription(self, itemDescription):
        self.__itemDescription = itemDescription

    # Setting the item's inventory
    def setInv(self, itemInv):
        self.__itemInv = itemInv

    # Setting the item's price
    def setPrice(self, itemPrice):
        self.__itemPrice = itemPrice

    # Getting the item's description
    def getDescription(self):
        return self.__itemDescription

    # Getting the item's inventory
    def getInv(self):
        return self.__itemInv

    # Getting the item's price
    def getPrice(self):
        return self.__itemPrice
