# Harrison Smith
# Chapter 8 Programming Exercises
# Chapter 8 Exam
# CPT 187 Prof. Carman
# Feb 27, 2021
# The program is designed to be a Character Analysis of the given statement in the text file. It should list the number
# of uppercase letters, lowercase letters, digits in the file, and the number of white space in the file. All of this
# should output to the console.

def main():

    # Using a variable to have a way to store the text from the file.
    textFile = ""

    # Opening the file
    try:
        inFile = open("TextforExam2.txt", "r")

        # Storing all the text from the file in the variable called earlier
        textFile = inFile.read()

        # Closing the file
        inFile.close()

    # Catch all error
    except IOError:
        print("Error: File Could not be found!")

    # Calling each of the defined functions to print the required information in the proper format. The text file is
    # passed in as the argument.
    CountDigits(textFile)
    CountLowerCase(textFile)
    CountUpperCase(textFile)
    CountWhiteSpace(textFile)
    CountWords(textFile)


# Defining the function
def CountDigits(str):
    # Using a variable to store information
    digitCount = 0

    # Looping through every character in the string from the file
    for char in str:
        # Using if statement to check if the character is a number
        if char.isdigit():
            # Adding 1 to the count if the character is a number
            digitCount += 1

    # Printing the required information
    print("The amount of numbers is:", digitCount)


# Defining the function
def CountLowerCase(str):
    # Using a variable to store information
    lowerCount = 0

    # Looping through every character in the string from the file
    for char in str:
        # Using if statement to check if the character is lower case
        if char.islower():
            # Adding 1 to the count if the character is lower case
            lowerCount += 1

    # Printing the required information
    print("The amount of lower case letters is:", lowerCount)


# Defining the function
def CountUpperCase(str):
    # Using a variable to store information
    upperCount = 0

    # Looping through every character in the string from the file
    for char in str:
        # Using if statement to check if the character is upper case
        if char.isupper():
            # Adding 1 to the count if the character is upper case
            upperCount += 1

    # Printing the required information
    print("The amount of upper case letters is:", upperCount)


# Defining the function
def CountWhiteSpace(str):
    # Using a variable to store information
    whtspCount = 0

    # Looping through every character in the string from the file
    for char in str:
        # Using if statement to check if the character is whitespace
        if char.isspace():
            # Adding 1 to the count if the character is a whitespace
            whtspCount += 1

    # Printing the required information
    print("The amount of white space characters is:", whtspCount)


# Defining the count words function
def CountWords(str):

    # Putting all the words from the text file into a list
    wordCount = str.split()

    # Printing out all the totals in the correct format
    print("The amount of words is:", len(wordCount))


# Calling the main function
main()