## Cody Walker
## 3/15/2021
## CIS 1400 VCM01


def isValidRate(userData):
    hourlyRate = userData
    while '.' in userData:
        userData = userData.replace('.', '')
    if userData.isdigit():
        hourlyRate = float(hourlyRate)
        if hourlyRate >= 0 and hourlyRate <= 40:
            return True
        else:
            print('Value must be between 7.50 and 18.25')
            return False
    else:
        print('You did not enter a valid number. Please only use numbers.')
        
def isValidHours(userData):
    hoursWorked = userData
    
    while '.' in userData:
        userData = userData.replace('.', '')
    if userData.isdigit():
        hoursWorked = float(hoursWorked)
        if hoursWorked >= 0 and hoursWorked <= 40:
            return True
        else:
            print('Hours must be between 0 and 40. Please Try again.')
            return False
def calcGrossPay(hourlyRate, hoursWorked):
    return float(hourlyRate) * float(hoursWorked)
def main():
    
    hourlyRate = input('Please enter your hourly pay rate: ')
    
    if not isValidRate(hourlyRate):
        return
    hoursWorked = input('Please enter the hours worked: ')
    
    if not isValidHours(hoursWorked):
        return
    
    print('Gross pay: ')
main()