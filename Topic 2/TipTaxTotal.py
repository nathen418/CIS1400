# Name:  Nate Goldsvorough
# Date: 2/6/2021
# Descr: Design a program that calculates the total amount of a meal purchased at a restaurant. The program
#           should ask the user to enter the charge for the food, and then calculate the amount of a 15 percent tip
#           and 7 percent sales tax. Display each of these amounts and the total.

#const tax rate and tip rate
TAX_RATE = 0.07
TIP_RATE = 0.15

#get input from user`
foodCost = float(input("Enter the cost of the food ordered before tax as a number: "))

#calculate tipCost taxCost and totalCost
tipCost = TIP_RATE* foodCost
taxCost = TAX_RATE * foodCost
totalCost = taxCost + tipCost + foodCost


#display all the data to the user
print("The food cost is $", format(foodCost, '.2f'))
print("The tip cost is $", format(tipCost, '.2f'))
print("The tax cost is $", format(taxCost, '.2f'))
print("The total cost after tip and tax is $", format(totalCost, '.2f'))

# Sample output
# Enter the cost of the food ordered before tax as a number: 30
# The food cost is $ 30.00
# The tip cost is $ 4.50  
# The tax cost is $ 2.10  
# The total cost after tip and tax is $ 36.60
