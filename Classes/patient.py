# Declaring the class
class PatientClass:

    # Initializing the constructor for the patients
    def __init__(self, patientFirst, patientMiddle, patientLast, patientAddress, patientCity, patientState, patientZip,
                 patientPhone, patientEmContact, patientEmPhone):
        # Setting each argument to the corresponding attribute with the same name.
        self.__patientFirst = patientFirst
        self.__patientMiddle = patientMiddle
        self.__patientLast = patientLast
        self.__patientAddress = patientAddress
        self.__patientCity = patientCity
        self.__patientState = patientState
        self.__patientZip = patientZip
        self.__patientPhone = patientPhone
        self.__patientEmContact = patientEmContact
        self.__patientEmPhone = patientEmPhone

    # Using the __str__ method to return a string indicating the objects state.
    def __str__(self):
        # Printing a line of information for each attribute.
        return  'First Name: ' + self.__patientFirst + \
                '\nMiddle Name: ' + self.__patientMiddle + \
                '\nLast Name: ' + self.__patientLast + \
                '\nAddress: ' + self.__patientAddress + \
                '\nCity: ' + self.__patientCity + \
                '\nState: ' + self.__patientState + \
                '\nZip: ' + self.__patientZip + \
                '\nPhone: ' + self.__patientPhone + \
                '\nEmergency Contact: ' + self.__patientEmContact + \
                '\nEmergency Phone: ' + self.__patientEmPhone

    # Setting the patient's first name
    def setFirst(self, patientFirst):
        self.__patientFirst = patientFirst

    # Setting the patient's middle name
    def setMiddle(self, patientMiddle):
        self.__patientMiddle = patientMiddle

    # Setting the patients last name
    def setLast(self, patientLast):
        self.__patientLast = patientLast

    # Setting the patient's address
    def setAddress(self, patientAddress):
        self.__patientAddress = patientAddress

    # Setting the patient's city
    def setCity(self, patientCity):
        self.__patientCity = patientCity

    # Setting the patient's state
    def setState(self, patientState):
        self.__patientState = patientState

    # Setting the patient's Zip
    def setZip(self, patientZip):
        self.__patientZip = patientZip

    # Setting the patient's phone number
    def setPhone(self, patientPhone):
        self.__patientPhone = patientPhone

    # Setting the patient's Emergency contact
    def setEmContact(self, patientEmContact):
        self.__patientEmContact = patientEmContact

    # Setting the patient's emergency phone
    def setEmPhone(self, patientEmPhone):
        self.__patientEmPhone = patientEmPhone

    # Getting the patient's first name
    def getFirst(self):
        return self.__patientFirst

    # Getting the patient's middle name
    def getMiddle(self):
        return self.__patientMiddle

    # Getting the patient's last name
    def getLast(self):
        return self.__patientLast

    # Getting the patient's address
    def getAddress(self):
        return self.__patientAddress

    # Getting the patient's city
    def getCity(self):
        return self.__patientCity

    # Getting the patient's state
    def getState(self):
        return self.__patientState

    # Getting the patient's zip code
    def getZip(self):
        return self.__patientZip

    # Getting the patient's phone number
    def getPhone(self):
        return self.__patientPhone

    # Getting the patient's emergency contact
    def getEmContact(self):
        return self.__patientEmContact

    # Getting the patient's emergency phone number
    def getEmPhone(self):
        return self.__patientEmPhone

