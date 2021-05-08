# Author:  Carolyn England
# Date:    11/23/2020
# Prog:    TestAvgGUI.py
# Descr:
#     In class example to implement the Test Average Calculator
#     graphical user interface in Python using the tkinter
#     module.
   
# import tkinter module and allow
# direct references to all contained
# classes
from tkinter import *

# class representation for Test Average GUI
class TestAvg_GUI:
    # create the constructor (aka Python initializer)
    def __init__(self):
        # create window and set title
        self.mainWindow = Tk()
        self.mainWindow.title('Test Average')
        self.mainWindow.geometry('200x110')

        self.label = Label(self.mainWindow, text='Distance:')
        self.text = Entry(self.mainWindow, width = 15)


        self.button1 = Button(self.mainWindow, text = "Click Me", command = self.aFunction)
        

        self.label.pack(side = 'left')
        self.text.pack(side = 'left')

        self.button1.pack()
        # enter the main window loop
        self.mainWindow.mainloop()
    
    def aFunction(self):
        print(self.text.get())
        
def main():
    myTestAvg = TestAvg_GUI()
    

# start program by calling main
main()

