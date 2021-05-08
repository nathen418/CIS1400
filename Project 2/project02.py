# Nate Goldsborough
# Date: 3/13/2021
# Class: CIS 1400 VCM01
# Desc: Design and implement a function to calculate and return the area of a circle given its radius.
# Group Project 2


# A function to calc the area of a circle given a radius
def calcArea(radius):
    pi = 3.14159
    # Calculate the area of the circle
    area = pi * ((float(radius) ** 2.0))
    return area

# Main function  
def main():
    # Get user input
    radius = input('Please input a radius: ')
    # call the radius function and then print the output
    print('The area of the circle of radius ' + str(radius) + ' is ' + str(calcArea(radius)))

# Call the main function
main()