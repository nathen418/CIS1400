from tkinter import *

class PropertyTaxGUI():

    def __init__(self):
        self.mainwindow = Tk()
        self.assessvalue = StringVar()
        self.taxvalue = StringVar()
        self.textSide = 'left'

        # Create line one and add the value prompt
        self.line1 = Frame()
        self.propertyValueLabel = Label(self.line1, text='Enter the property value: $')
        self.propertyValue = Entry(self.line1, width=10)

        # Create line two and display the assessment value
        self.line2 = Frame()
        self.assessmentValue = Label(self.line2, text='Assessment Value: $')
        self.assessValueData = Label(self.line2, textvariable=self.assessvalue)

        # Create line 3 and display the property tax value
        self.line3 = Frame()
        self.prop_tax = Label(self.line3, text='Property Tax: $')
        self.prop_tax_val = Label(self.line3, textvariable=self.taxvalue)

        # Create line 4 and display the calculate and quit buttons
        self.line4 = Frame()
        self.calculateButton = Button(self.line4, text='Calculate', command=self.calculate)
        self.quitButton = Button(self.line4, text='Quit', command=self.mainwindow.destroy)

        
        #pack all of the widgets to the left side of their respective frames
        self.propertyValueLabel.pack(side=self.textSide)
        self.propertyValue.pack(side=self.textSide)
        self.assessmentValue.pack(side=self.textSide)
        self.assessValueData.pack(side=self.textSide)
        self.prop_tax.pack(side=self.textSide)
        self.prop_tax_val.pack(side=self.textSide)
        self.calculateButton.pack(side=self.textSide)
        self.quitButton.pack(side=self.textSide)

        #pack the frames into the window one under
        self.line1.pack()
        self.line2.pack()
        self.line3.pack()
        self.line4.pack()

        #enter the tkinter main loop
        self.mainwindow.mainloop()

    def calculate(self):
       self.propertyValue = float(self.propertyValue.get())

       self.assessmentValue = self.propertyValue*0.6
       self.property_tax = self.propertyValue * 0.0064

       self.assessvalue.set(self.assessmentValue)
       self.taxvalue.set(self.property_tax)


#create an instance of the class
my_gui = PropertyTaxGUI()