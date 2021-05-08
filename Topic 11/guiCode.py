from tkinter import *

class PropertyTaxGUI():

    def __init__(self):
        self.mainwindow = Tk()
        self.textSide = 'left'

        self.topFrame = Frame()
        self.midFrame = Frame()
        self.thirdFrame = Frame()
        self.bottomFrame = Frame()
        self.value = StringVar()

        #create widgets for the top frame
        self.propertyValueLabel = Label(self.topFrame, text='Enter the property value: $')
        self.propertyValue = Entry(self.topFrame, width=10)
        self.assessmentValue = Label(self.midFrame, text='Assessment Value: $')
        self.assessValueLabel = Label(self.midFrame, textvariable=self.value)
        self.prop_tax = Label(self.thirdFrame, text='Property Tax: $')
        self.prop_tax_val = Label(self.thirdFrame, textvariable=self.value)
        self.calculateButton = Button(self.bottomFrame, text='Calculate', command=self.calculate)
        self.quitButton = Button(self.bottomFrame, text='Quit', command=self.mainwindow.destroy)
        
        
        #pack the top frame's widgets
        self.propertyValueLabel.pack(side=self.textSide)
        self.propertyValue.pack(side=self.textSide)
        self.assessmentValue.pack(side=self.textSide)
        self.assessValueLabel.pack(side=self.textSide)
        self.prop_tax.pack(side=self.textSide)
        self.prop_tax_val.pack(side=self.textSide)
        self.calculateButton.pack(side=self.textSide)
        self.quitButton.pack(side=self.textSide)

        #pack the frames
        self.topFrame.pack()
        self.midFrame.pack()
        self.thirdFrame.pack()
        self.bottomFrame.pack()

        #enter the tkinter main loop
        self.mainwindow.mainloop()

    def calculate(self):
       self.propVal = float(self.propertyValue.get())

       self.assessVal = self.propVal*0.6

       self.property_tax = (self.propVal//100) * 0.74
       self.value.set(self.property_tax+self.assessVal)



#create an instance of the class
my_gui = PropertyTaxGUI()