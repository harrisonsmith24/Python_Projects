# Declaring the procedures class
class Procedure:

    # Initialize the constructor for the procedures class
    def __init__(self, procName, procDate, procPract, procCharge):
        # Setting each argument for the __init__ method to the attribute with the corresponding name.
        self.__procName = procName
        self.__procDate = procDate
        self.__procPract = procPract
        self.__procCharge = procCharge

    # Using the __str__ method to return a string indicating the objects state.
    def __str__(self):
        # Printing a line of information for each attribute.
        return "Procedure: " + self.__procName + \
               "\nDate: " + self.__procDate + \
               "\nPractitioner: " + self.__procPract + \
               "\nCharge: " + format(self.__procCharge, '.2f') + '\n'

    # Setting the procedure's name
    def setName(self, procName):
        self.__procName = procName

    # Setting the procedure's date
    def setDate(self, procDate):
        self.__procDate = procDate

    # Setting the procedure's practitioner
    def setPract(self, procPract):
        self.__procPract = procPract

    # Setting the procedure's charge
    def setCharge(self, procCharge):
        self.__procCharge = procCharge

    # Getting the procedure's name
    def getName(self):
        return self.__procName

    # Getting the procedure's date
    def getDate(self):
        return self.__procDate

    # Getting the procedure's practitioner
    def getPract(self):
        return self.__procPract

    # Getting the procedure's Charge
    def getCharge(self):
        return self.__procCharge