# Name:  Nate Goldsborough
# Date: 2/16/2021
# Class: CIS-1400
#! Desc: This program will allow a user to enter the weight of a package they wish to ship and will calculate the shipping cost of the package
#! then print the output

def calcAndDisplay(packageWeight):
    # CONSTANT array of shipping costs per weight class
    RATES = [1.1, 2.2, 3.7, 3.8]
    # local variable to store the correct shiping rate
    rate = 0
    # figure out what class of package is being shipped and select the correct rate
    if(packageWeight <= 2):
        rate = RATES[0]
    elif(packageWeight <= 6):
        rate = RATES[1]
    elif(packageWeight <= 10):
        rate = RATES[2]
    elif(packageWeight > 10):
        rate = RATES[3]
    # calculate the correct rate
    totalCost = packageWeight * rate
    # Print the total weight and total cost to ship the package
    print("The total weight of the package is:", packageWeight)
    print("The total cost to ship the package is: $" + format(totalCost, '.2f'))

def main():
    # validate the input to make sure that the user entered a float and not a string or something else
    try:
        # Get the package weight from the user as a float
        packageWeight = float(
            input('Please input the weight of your package in pounds: '))
    except ValueError:
        # if the user entered a data type that is not a float tell them and exit the program
        print('You have not entered a number. Please re-run the program and try again.')
        return
    # calculate the package rate and display the answer
    calcAndDisplay(packageWeight)

main()


# Sample output where the user enters a float:
    # Please input the weight of your package in pounds: 8
    # The total weight of the package is: 8.0
    # The total cost to ship the package is: $29.60

# Sample output where the user does not enter a float:
    # Please input the weight of your package in pounds: Nate
    # You have not entered a number. Please re-run the program and try again.