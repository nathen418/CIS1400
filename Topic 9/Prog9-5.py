# Author:  <Your Name Here>
# Date:    MM/DD/YYYY
# Program: Prog9_5.py
# Descr:
# In-class exercise to create the Python implementation
# of Selection Sort Program 9-5 in Gaddis
def main():
    # Constant for the array size
    SIZE = 6
    # An array of Integers
    numbers = [4, 6, 1, 3, 5, 2]
    # Loop counter
    index = int()
    # Display the array in its original order
    print('Original order:')
    for index in range (0, SIZE):
        print(numbers[index])
    # Sort the numbers
    selectionSort(numbers, SIZE)
    # Display the sorted array
    print('Sorted order:')
    for index in range (0, SIZE):
        print(numbers[index])

# The selectionSort module accepts an array of Integers
# and the array's size as arguments.  When the module
# is finished, the values in the array will be sorted
# in ascending order.
def selectionSort(array, arraySize):
    return

# start program
main()
