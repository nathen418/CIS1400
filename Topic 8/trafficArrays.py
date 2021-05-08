import os


def main():
    filename = input("Enter the name of the traffic file: ")
    if ".dat" not in filename:
        filename += ".dat"

    try:
        file = open(os.getcwd() + "\\" + filename, 'r')
        trafficArray = file.readlines()
        file.close()
    except OSError:
        print("There was an error opening your file. Please make sure the file you want to use is in your current working directory")
        print("Please re-run this program once you have done the above.")
        return
    except TypeError:
        print("The file you specified is not a '.dat' file. Maybe you entered the wrong file name?")
        print("Please re-run this program with the correct file.")
        return
    largest = 0
    numberOfDays = len(trafficArray)
    totalCars = 0
    for i in range(0,numberOfDays):
        try:
            value = int(trafficArray[i].rstrip())
        except (TypeError, ValueError):
            print("There was a line in your file that could not be converted to an int for processing.")
            print("Please double check that your file is composed of only numeric charecters")
            return
        totalCars += value
        if value > largest:
            largest = value
    averageCars = totalCars / numberOfDays
    print("Number of days monitored: ", numberOfDays)
    print("Maximum number of cars in a day: ", largest)
    print("Average cars per day: ", format(averageCars, '.2f'))


main()