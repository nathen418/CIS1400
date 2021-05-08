# Author:  <Your Name Here>
# Date:    MM/DD/YYYY
# Program: Prog9_2.py
# Descr:
# In-class exercise to create the Python implementation
# of Bubble Sort Program 9-2 in Gaddis.

def main():
    # Constant for the array size
    SIZE = 6
    # Array to hold test scores
    testScores = [0] * SIZE
    # Get the test scores
    getTestScores(testScores, SIZE)
    # Sort the test scores
    bubbleSort(testScores, SIZE)
    # Display the test scores
    print('Here are the test scores sorted from lowest to highest.')
    showTestScores(testScores, SIZE)

# The getTestScores module prompts the user
# to enter test scores into the array that is
# passed as an argument.
def getTestScores(array, arraySize):
    # Counter variables
    index = 0
    # Get the test scores
    for index in range (0, arraySize):
        array[index] = int(input('Enter score number ' + str(index + 1) + ' '))

# The showTestScores module displays the contents
# of the array that is passed as an argument.
def showTestScores(array, arraySize):
    # Counter variables
    index = 0
    # Display the test scores
    for index in range (0, arraySize):
        print(array[index])

# The bubbleSort module accepts an array of Integers
# and the array's size as arguments.  When the module
# is finished, the values in the array will be sorted
# in ascending order.
def bubbleSort(array, arraySize):
    for i in range(len(array)):
        # loop through the list
        for j in range(len(array) - 1):
            # Loop through the sub loop until an element needs to be swapped
            if array[j] > array[j+1]:
                # this swaps the 2 indexes
                array[j], array[j+1] = array[j+1], array[j]
    return

# start program
main()
