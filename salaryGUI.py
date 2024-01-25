"""
Program: salaryGUI.py
Chapter 8 Example (Pg 251)
01/25/2024

**NOTE: The module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!
"""

from breezypythongui import EasyFrame
from tkinter.font import Font

# Class header
class SalaryGUI(EasyFrame):

	# Definition of out classes' constructor method
	def __init__(self):
		# Call to the Easy Frame Class constructor
		EasyFrame.__init__(self, title = 'Salary Calculator 2.0', background = 'lightgreen')
		# Variable to store a Font design for multiple labels
		myTitle = Font(family='Gorgia', size=14)
		myLabel = Font(family='Verdana', size=10)

		# Add the widgets to the window
		self.addLabel(text='Salary Calculator', row=0, column=0, columnspan=2, sticky='NSEW', font=myTitle, background = 'lightgreen')

		self.addLabel(text='Hourly Wage:', row=1, column=0, background = 'lightgreen', foreground = 'darkgreen', font = myLabel)
		self.wageField = self.addFloatField(value=0.0, row=1, column=1, width=10)

		self.addLabel(text='# of Hours Worked', row=2, column=0, background = 'lightgreen', foreground = 'darkgreen', font = myLabel)
		self.hoursField = self.addIntegerField(value=0, row=2, column=1, width=10)

		self.button = self.addButton(text='Compute', row=3, column=0, columnspan=2, command = self.compute)
		self.button['background'] = 'palegoldenrod'
		self.button['width'] = 15

		self.addLabel(text="The Employee's Salary is:", row=4, column=0, background = 'lightgreen', foreground = 'darkgreen', font = myLabel)
		self.salaryField = self.addFloatField(value=0.0, row=4, column=1, precision = 2, state = 'readonly')

	# Definition of the compute() function which is the event handler
	def compute(self):
	    wage = self.wageField.getNumber()
	    hours = self.hoursField.getNumber()
	    salary = wage * hours
	    self.salaryField.setNumber(salary)
		
# Global definition of the main() method
def main():
	# instantiate an object from the class into mainloop()
	SalaryGUI().mainloop()

if __name__ == '__main__':
	main()