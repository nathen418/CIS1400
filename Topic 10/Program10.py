# Nate Goldsborough
# Date: 4/19/2021
# Class: CIS 1400 VCM01
# Desc: Make a program to take information from the user about a movie and store it to a .dat file and show the total runtime of all movies entered

import Movie

def main():
    # define the total number of movies to be entered
    movieTotal = 2
    # loop through each movie
    for i in range(movieTotal):
        # get call createObject() and send its data to writeToFile()
        writeToFile(createObject(), i+1)
    displayTotal()

def createObject():
    # unpack the array returned by getInfo() into seperate vars
    name, prod_co, runtime, year = getInfo()
    # create a new instance of the Movie class
    movie = Movie(name, prod_co, runtime, year)
    # return the object
    return movie

def getInfo():
    # get information about the movie
    print("Enter the following information about a movie: ")
    name = input("Name of the movie: ")
    prod_co = input("Name of prodiction company: ")

    # error handling for minutes type
    try:
        runtime = float(input("Runtime in minutes: "))
    except (ValueError, TypeError):
        print("You did not enter a valid runtime. Re-run the program and try again.")
        return
    # error handling for year type
    try:
        year = int(input("Year of publication: "))
    except (ValueError, TypeError):
        print("You did not enter a valid year. Re-run the program and try again.")
        return
    # return an array with all the entered information
    return [name, prod_co, runtime, year]

def writeToFile(movie, objectNumber):
    # create the string to be writen from a formated string using the getter methods of the passed in object movie
    inputStr = f'Movie {objectNumber}: {movie.getName()}, {movie.getProd_Co()}, {movie.getRuntime()}, {movie.getYear()}\n'
    # try to open the file and handle any errors that might appear
    try:
        # open or create a file to store the data in
        with open('Movie_Inventory.dat', 'a') as file:
            # write the inputStr
            file.write(inputStr)
    except OSError:
        print("Could not open or write to file. Is the directory locked by another program? Re-run the program and try again.")

def displayTotal():
    totalTime = 0
    try:
        with open('Movie_Inventory.dat', 'r') as file:
            for line in file:
                totalTime += float(line.split(',')[2])
            print(f"The total watchtime of all the movies in the file is {totalTime} minutes.")
    except OSError:
        print("Could not open or read from file. Is the directory locked by another program? Re-run the program and try again.")


# call main function
main()


# Sample output
# Enter the following information about a movie: 
# Name of the movie: Shrek
# Name of prodiction company: Dreamworks
# Runtime in minutes: 107
# Year of publication: 2001
# Enter the following information about a movie: 
# Name of the movie: Harry potter
# Name of prodiction company: Warner Bros
# Runtime in minutes: 98
# Year of publication: 200 
# The total watchtime of all the movies in the file is 205.0 minutes.