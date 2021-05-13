# Name:  Nate Goldsborough
# Date: 2/10/2021
# Desc: A county collects property taxes on the assessment value of property, which is 60 percent of the property’s actual value. 
#           For example, if an acre of land is valued at $10,000, its assessment value is $6,000. 
#           The property tax is then 64¢ for each $100 of the assessment value. The tax for the acre assessed at $6,000 will be $38.40. 
#           Design a modular program that asks for the actual value of a piece of 
#           property and displays the assessment value and property tax.

#const tax rate and assessment percentage
TAX_RATE = 0.0064
ASSESSMENT_PERCENTAGE = 0.6


def main():


    #get input from user
    try:
        propertyValue = float(input("Enter the property value as a number: "))
    except ValueError: 
        print("You did not enter a number. \nPlease run the program again")
        exit()
    calcAndDisplay(propertyValue)

def calcAndDisplay(propertyValue):
    #calculate assessmentValue and taxValue
    assessmentValue = ASSESSMENT_PERCENTAGE * propertyValue
    taxValue = assessmentValue * TAX_RATE


    #display AssessmentValue and Amount due in taxes
    print("The property value is $", format(propertyValue, '.2f'))
    print("The assessment value is $", format(assessmentValue, '.2f'))
    print("The total taxes due are $", format(taxValue, '.2f'))

main()
# Sample output
# Enter the property value as a number: 10000
# The property value is $ 10000.00 
# The assessment value is $ 6000.00
# The total taxes due are $ 38.40  
