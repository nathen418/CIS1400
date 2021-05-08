# Name:  Nate Goldsborough
# Date: 3/13/2021
# Class: CIS 1400 VCM01
# Desc: A program to calculate a users payroll from the number of hours they worked and their pay rate. It will also validate the input
# and then display the gross pay to the user at the end of the program

# A function to decide if the pay rate entered is in a valid range
def isValidRate(userInput):
    rate = userInput

    while '.' in userInput:
        userInput = userInput.replace(".", "")
    if userInput.isdigit():
        rate = float(rate)
        if rate >= 7.50 and rate <= 18.25:
            return True
        # check if payRate is in the valid range
        else:
            print("Please re-run the program and enter your pay rate, between $7.50 and $18.25")
            return False
    else:
        print("You did not enter a number. Please only enter numeric char\'s and \'.\'s. Please re-run this program")
        return False
        # check if hours is in the valid range


# A function to decide if the hours entered are in a valid range
def isValidHours(userInput):
    hours = userInput

    while '.' in userInput:
        userInput = userInput.replace(".", "")
    if userInput.isdigit():
        hours = float(hours)
        if hours >= 0 and hours <= 40:
            return True
        # check if payRate is in the valid range
        else:
            print("Please re-run the program and enter your number of hours, between 0 and 40")
            return False
    else:
        print("You did not enter a number. Please only enter numeric char\'s and \'.\'s. Please re-run this program")
        return False
        # check if hours is in the valid range

# A function to calculate the user's gross pay
def calcGrossPay(hours, payRate):
    return float(hours) * float(payRate)

# The main function
def main():
    # Get user input
    payRate = input("Please enter you\'re hourly pay rate: ")
    # Check if the input is in the correct range. (call isValidRate)
    if not isValidRate(payRate):
        # Exit the program if it was invalid
        return
    # Get user input
    hours = input("Please enter the number of hours that you worked this week: ")
    # Check if the input is in the correct range. (call isValidHours)
    if not isValidHours(hours):
        # Exit the program if it was invalid
        return
    # Print the final gross pay of the user and end the program
    print("Your gross pay for this week is: $" + format(calcGrossPay(hours, payRate), '.2f'))
    

# Call the main function to start the program
main()


# ----------------Sample output's---------------------

# Sample output with both input parameters being valid:
    # Please enter you're hourly pay rate: 15
    # Please enter the number of hours that you worked this week: 35
    # Your gross pay for this week is: $525.00

# Sample output with a value being out of range:
    # Please enter you're hourly pay rate: 18
    # Please enter the number of hours that you worked this week: 50
    # Please re-run the program and enter your number of hours, between 0 and 40

# Sample output where the user entered a string:
    # Please enter you're hourly pay rate: 15.50
    # Please enter the number of hours that you worked this week: thirteen
    # You did not enter a number. Please only enter numeric char's and '.'s. Please re-run this program