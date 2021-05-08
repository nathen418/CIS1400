# Name:  Nate Goldsborough
# Date: 2/2/2021
# Desc: class example to implement the python code for the Pay calculator design (flowchart and pseudocode).

#global const tax rate     
TAX_RATE = 0.25

def main():

    #get input from user`
    try:
        hours = float(input("Enter the number of hours worked: "))
        payRate = float(input("Enter the hourly pay rate as a number: "))
    except ValueError: 
        print("You did not enter a number. \nPlease run the program again")
        exit()
    calcAndDisplay(hours, payRate)

def calcAndDisplay(hours, payRate):
    #calculate gross pay , taxes, and net pay
    grossPay = hours * payRate
    taxes = grossPay * TAX_RATE
    netPay = grossPay - taxes


    #display gross pay
    grossPay = hours * payRate
    print("The gross pay for the user is $", format(grossPay, '.2f'))
    print("The taxes for the user are $", format(taxes, '.2f'))
    print("The net pay for the user is $", format(netPay, '.2f'))

main()

# Sample output
# Enter the number of hours worked: 10.5
# Enter the hourly pay rate as a number: 12.25
# The gross pay for the user is $ 128.62
# The taxes for the user are $ 32.16
# The net pay for the user is $ 96.47
