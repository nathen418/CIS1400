# Nate Goldsborough
# Date: 4/19/2021
# Class: CIS 1400 VCM01
# Desc: Movie class for movies.py

class Movie:
    def __init__(self, name, prod_co, runtime, year):
        self.__name = name
        self.__prod_co = prod_co
        self.__runtime = runtime
        self.__year = year
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    def getProd_Co(self):
        return self.__prod_co
    def setProd_Co(self, prod_co):
        self.__prod_co = prod_co
    def getRuntime(self):
        return self.__runtime
    def setRuntime(self, runtime):
        self.__runtime = runtime
    def getYear(self):
        return self.__year
    def setYear(self, year):
        self.__year = year
