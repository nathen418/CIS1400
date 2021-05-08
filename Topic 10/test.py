import Movie

def getInfo():
    # get information about the movie
    print("Enter the following information about a movie: ")
    name = input("Name of the movie: ")
    prod_co = input("Name of prodiction company: ")
    runtime = float(input("Runtime in minutes: "))
    year = int(input("Year of publication: "))
    # return an array with all the entered information
    return [name, prod_co, runtime, year]


def createObject():
    # unpack the array returned by getInfo() into seperate vars
    name, prod_co, runtime, year = getInfo()


    # create a new instance of the Movie class
    movie = Movie(name, prod_co, runtime, year)
    # return the object
    return movie

def writeToFile(movie, objectNumber):
    # create the string to be writen from a formated string using the getter methods of the passed in object movie
    inputStr = f'Movie {objectNumber}: {movie.getName()}, {movie.getProd_Co()}, {movie.getRuntime()}, {movie.getYear()}\n'
    # open or create a file to store the data in
    with open('Movie_Inventory.dat', 'a') as file:
        # write the inputStr
        file.write(inputStr)


def TotalTime():
    totalTime = 0
    with open('Movie_Inventory.dat', 'r') as file:
        for line in file:
            totalTime += float(line.split(',')[2])
        print(f"The total watchtime of all the movies in the file is {totalTime} minutes.")

