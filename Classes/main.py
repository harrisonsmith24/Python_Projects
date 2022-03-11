# Harrison Smith
# Professor Carman CPT 187 Y01
# 4/19/2021
# This program is designed to use the procedures and patient class to store information about three different patients
# that are undergoing three different procedures. The program should use the classes to distinguish between the patients
# and the procedures and print each patient to the console with their corresponding procedure.

# Import the patient class
import patient
# Import the procedures class
import procedures
# Import the datetime class
import datetime


# Defining the main function
def main():
    # Creating a variable that will have the exact date
    theNow = datetime.datetime.now().strftime('%m/%d/%y')

    # Storing the information for the first patient into a variable
    patientOne = patient.PatientClass("Harold", "George", "Wattson", "310 Heartway Dr", "Clinton", "SC", "29567",
                                      "843-424-0965", "Mrs. Wattson", "843-555-6666")

    # Storing the information for the first procedure into a variable
    procedureOne = procedures.Procedure("Physical Exam", theNow, 'Dr.Irvine', 250.00)

    # # Storing the information for the second patient into a variable
    patientTwo = patient.PatientClass("Martin", "Frank", "Hartman", "400 Laneway Dr", "Clinton", "SC", "29567",
                                      "843-999-888", "Mrs. Hartman", "843-989-9898")

    # Storing the information for the second procedure into a variable
    procedureTwo = procedures.Procedure("X-ray", theNow, "Dr. Jamison", 500.00)

    # # Storing the information for the third patient into a variable
    patientThree = patient.PatientClass("Patricia", "Mary", "Leeman", "455 Copler Street", "Clinton", "SC", "29567",
                                      "444-983-2765", "Mr. Leeman", "843-434-0276")

    # Storing the information for the third procedure into a variable
    procedureThree = procedures.Procedure("Blood Test", theNow, "Dr. Smith", 200.00)

    # Calling the printOut function to print out the stored information to the console for patient one
    printOut(patientOne, procedureOne)
    print('')
    # Calling the printOut function to print out the stored information to the console for patient two
    printOut(patientTwo, procedureTwo)
    print('')
    # Calling the printOut function to print out the stored information to the console for patient three
    printOut(patientThree, procedureThree)


# Defining the printOut function
def printOut(patient, procedure):
    # print the information of the selected patient
    print(patient)
    # print the information of the selected procedure
    print(procedure)


# Call the main function
main()
