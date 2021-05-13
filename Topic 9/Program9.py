# Nate Goldsborough
# Date: 4/18/2021
# Class: CIS 1400 VCM01
# Desc: Make a program to sort a list of names and allow a user to search thru the list to determine if a name appears in it and what position in the list it appears in

def bubbleSort(names):
    for i in range(len(names)):
        # loop through the list
        for j in range(len(names) - 1):
            # Loop through the sub loop until an element needs to be swapped
            if names[j] > names[j+1]:
                # this swaps the 2 indexes
                names[j], names[j+1] = names[j+1], names[j]

def displaySorted(names):
    for i in range(len(names)):
        print(f"Name {i+1}: {names[i]}")

def search(value, names):
    for i in range(len(names)):
        if value == names[i]:
            return i
    return -1



def main():
    names = ["Ross Harrison",
     "Hannah Beauregard",
     "Bob White",
     "Ava Fischer",
     "Chris Rich",
     "Xavier Adams",
     "Sasha Ricci",
     "Danielle Porter",
     "Gordon Pike",
     "Matt Hoyle"]
    bubbleSort(names)
    displaySorted(names)

    value = input("Please enter a name to check if it is in the list: ")

    location = search(value, names)
    
    if (location != -1):
        print(f"The name you entered, {value}, was found at position {location + 1} in the ordered list")
    else:
        print("The name you entered does not exist in the list")




main()
