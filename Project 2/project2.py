# Nate Goldsborough
# Date: 3/13/2021
# Class: CIS 1400 VCM01
# Desc: Design and implement a function to calculate and return the area of a circle given its radius.
# Group Project 2
import math

# A function to calc the area of a circle given a radius
def calcArea(radius):
    # Calculate the area of the circle
    area = math.pi * (radius ** 2.0)
    return area

# Main function  
def main():
    # Get user input
    userInput = input('Please input a radius: ')
    radius = userInput
    # remove all . in the input to check if they entered a string or a number
    while '.' in userInput:
        userInput = userInput.replace('.', '')

    # If the modified string evaluates to be a number, then continue and calculate the area
    if userInput.isdigit():
        # convert the now validated radius to a float
        radius = float(radius)
        # do the calculation and display the output
        print('The area of the circle of radius ' + str(radius) + ' is ' + str(calcArea(radius)))
    else:
        # if the input was not valid let the user know and halt the program
        print('The radius you entered is invalid. Please re-run the program and enter a valid radius')
        return


# Call the main function
main()