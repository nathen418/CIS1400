# Name: Nate Goldsborough
# Date: 2/22/2021
# Class: CIS-1400
# Desc: This program is a cool new program that will take a sequence of user input numbers and compares them to get
# the largest and smallest numbers from the list and display's them

# A function that displays a welcome message to the user and tells them what the program will do
def welcome():
    print("\n\n\n\n\nWelcome to a new cool program that will display the largest and smallest value that you, the user, have entered.")
    print("It will run in a loop and not exit until you send \'-99\'")
# A function that displays the largest and the smallest number the user entered once the program is over
def output(smallest, largest):
    print('The smallest number you entered is: ', smallest)
    print('The largest number you entered is: ', largest)
# um Main? It runs the whole program
def main():
    # Send the welcome message
    welcome()
    # Set our vairables to 0. Not needed but it helpes with readability
    inputNum = 0
    smallest = 0
    largest = 0
    # Check if the inputNumber is '-99' and if it is not then run a loop
    while(inputNum != -99):
        # Validate that the user actually entered an int. If they did not exit with an error and tell them to run the program again
        try:
            # get the input from the user
            inputNum = int(input('Please enter a whole number: '))
        except ValueError:
            # Display the error message to the user
            print('Please enter a whole number as an integer. Do not enter anything else. Please re-run the program')
            # Exit the program
            return
        # Check the input number against the highest and the lowest numbers, and update those variables accordingly
        if inputNum < smallest:
            smallest = inputNum
        elif inputNum > largest:
            largest = inputNum
    # Call the function to display the smallest and largest numbers in the set the user provided. Pass the largest and smallest variables to the function
    output(smallest, largest)

# Call the main function and actually run everything
main()

# Sample output with valid input:
# Welcome to a new cool program that will display the largest and smallest value that you, the user, have entered.
# It will run in a loop and not exit until you send '99'
# NOTE --- If you enter the number '99', the program will exit and display its output.
# Please enter a whole number: 101010101011111
# Please enter a whole number: 2
# Please enter a whole number: 5
# Please enter a whole number: -70
# Please enter a whole number: -200
# Please enter a whole number: -99
# The smallest number you entered is:  -200
# The largest number you entered is:  101010101011111

# Sample output where a string was entered by accident:
# Welcome to a new cool program that will display the largest and smallest value that you, the user, have entered.      
# It will run in a loop and not exit until you send '99'
# NOTE --- If you enter the number '99', the program will exit and display its output.
# Please enter a whole number: This class is AWESOME!
# Please enter a whole number as an integer. Do not enter anything else. Please re-run the program
