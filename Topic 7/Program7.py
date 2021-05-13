# Nate Goldsborough
# Date: 3/31/2021
# Class: CIS 1400 VCM01
# Desc: Make a program to calculate the max, min, average, and total rainfall for a year.


# Create a function to return the index of the largest value sent in rainfallStats
def getLargestRainfall(rainfallStats):
    return rainfallStats.index(max(rainfallStats))


# Create a function to return the index of the smallest value sent in rainfallStats
def getSmallestRainfall(rainfallStats):
    return rainfallStats.index(min(rainfallStats))



def main():

    # create arrays for months and rainfall stats
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    rainfallStats = [0] * 12

    # loop through the rainfall stats array and assign the rainfall for each month to its correct index
    for i in range(0,12):
        print("Please enter the rainfall for the month of ", end = '') # use this end = '' to make the print not happen with a newline char
        rainfallStats[i] = float(input(str(months[i]) +  ": ")) # Use str() so that the months[i] plays nicely with concatinating with a string

    # Send the rainfall numbers to the largest and smallest functions to get the array of the largest and smallest value
    maxRainfallIndex = getLargestRainfall(rainfallStats)
    minRainfallIndex = getSmallestRainfall(rainfallStats)

    # Print the data we got from those functions
    print("The max rainfall was", rainfallStats[maxRainfallIndex], "inches and happened in", months[maxRainfallIndex])
    print("The min rainfall was", rainfallStats[minRainfallIndex], "inches and happened in", months[minRainfallIndex])

    # do some extra math to find out the average and total rainfall stats
    print("The average rainfall was ", format(sum(rainfallStats)/len(rainfallStats), '.2f'), "inches")
    print("The total rainfall for the year was", format(sum(rainfallStats), '.2f'), "inches")


# Call the main function
main()



# -------------------- Sample output --------------------
# Please enter the rainfall for the month of January: 1
# Please enter the rainfall for the month of February: 2
# Please enter the rainfall for the month of March: 3
# Please enter the rainfall for the month of April: 4
# Please enter the rainfall for the month of May: 5
# Please enter the rainfall for the month of June: 6
# Please enter the rainfall for the month of July: 77
# Please enter the rainfall for the month of August: 8
# Please enter the rainfall for the month of September: 9
# Please enter the rainfall for the month of October: 10
# Please enter the rainfall for the month of November: 0.2
# Please enter the rainfall for the month of December: 3
# The max rainfall was 77.0 inches and happened in July
# The min rainfall was 0.2 inches and happened in November
# The average rainfall was  10.683333333333332 inches
# The total rainfall for the year was 128.2 inches