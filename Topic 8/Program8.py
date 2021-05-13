# Nate Goldsborough
# Date: 4/9/2021
# Class: CIS 1400 VCM01
# Desc: Make a program to calculate the max number of cars per day, average cars per day and total number of days studied from
#        A supplied `.dat` file.


import os

def main():
    # init vars and gc
    maxCars = 0
    totalDays = 0
    totalCars = 0

    # get the filename
    filename = input("Enter the name of the traffic file: ")
    if ".dat" not in filename:
        filename += ".dat"

    try:
        # open the file
        with open(os.getcwd() + "\\" + filename, 'r') as file:
            # loop thru the file lines
            for line in file:
                try:
                    # get the number from the line and record it 
                    num = int(line)
                    if num > maxCars:
                        maxCars = num
                    # increment the days and total cars
                    totalDays +=1
                    totalCars += num
                # do some error checking
                except (TypeError, ValueError):
                    print("There was a line in your file that could not be converted to an int for processing.")
                    print("Please double check that your file is composed of only numeric charecters")
                    return
    # do some more error checking
    except OSError:
        print("There was an error opening your file. Please make sure the file you want to use is in your current working directory")
        print("Please re-run this program once you have done the above.")
        return
    # here too
    except TypeError:
        print("The file you specified is not a '.dat' file. Maybe you entered the wrong file name?")
        print("Please re-run this program with the correct file.")
        return

    # get the average
    averageCars = totalCars / totalDays
    # print the outputs
    print("Number of days monitored: ", totalDays)
    print("Maximum number of cars in a day: ", maxCars)
    print("Average cars per day: ", format(averageCars, '.1f'))


# call main
main()

# Normal filename with .dat

# Enter the name of the traffic file: MainAndState.dat
# Number of days monitored:  320        
# Maximum number of cars in a day:  1998
# Average cars per day:  1018.7

# Invalid filename
# Enter the name of the traffic file: WOOHOO.dat
# There was an error opening your file. Please make sure the file you want to use is in your current working directory
# Please re-run this program once you have done the above.



