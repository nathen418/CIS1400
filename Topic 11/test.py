from tkinter import *

class PropertyTaxGUI():

    def __init__(self):
        # create main window
        self.mainWindow = Tk()
        self.mainWindow.title('Property Tax Value')
        self.mainWindow.geometry('300x100')

        self.taxValue = StringVar()
        self.assessmentValue = StringVar()

        # Create 3 separate frames
        self.frame1 = Frame()
        self.frame2 = Frame()
        self.frame3 = Frame()
        self.frame4 = Frame()

        # Create contents for frame 1
        self.valuePrompt = Label(self.frame1, text = 'Enter the property value: $')
        self.inputValue = Entry(self.frame1, width = 10)

        # pack frame 1
        self.valuePrompt.pack(side = 'left')
        self.inputValue.pack(side = 'left')
        self.frame1.pack(side = 'top')


        # Create contents for frame 2
        self.assessmentLabel = Label(self.frame2, text='Assessment Value: $')
        self.assmentOutput = Label(self.frame2, textvariable = self.assessmentValue)

        # pack frame 2
        self.assessmentLabel.pack(side = 'left')
        self.assmentOutput.pack(side = 'left')
        self.frame2.pack(side = 'top')

        # create contents for frame 3
        self.propertyTaxLabel = Label(self.frame3, text='Property Tax: $')
        self.propertyTaxOutput = Label(self.frame3, textvariable = self.taxValue)

        # Pack frame 3
        self.propertyTaxLabel.pack(side = 'left')
        self.propertyTaxOutput.pack(side = 'left')
        self.frame3.pack(side = 'top')
        



        # create contents for frame 3
        self.calculateButton = Button(self.frame4, text = 'Calculate', command = self.calculate)
        self.quitButton = Button(self.frame4, text='Quit', command=self.mainWindow.destroy)

        # pack frame 3
        self.calculateButton.pack(side = 'left')
        self.quitButton.pack(side = 'left')
        self.frame4.pack(side = 'top')

        #enter the tkinter main loop
        self.mainWindow.mainloop()



    def calculate(self):
        propertyValue = float(self.inputValue.get())

        assessmentValue = propertyValue * 0.6
        propertyTax = assessmentValue * 0.0064

        self.assessmentValue.set(assessmentValue)
        self.taxValue.set(format(propertyTax, '.2f'))



    #enter the tkinter main loop



def main():
    newWindow = PropertyTaxGUI()

main()