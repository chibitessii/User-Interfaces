import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
import matplotlib.pyplot as plt
import os
import csv

class Application(ttk.Frame):

	def __init__(self, master):
		ttk.Frame.__init__(self, master)
		self.pack()
		self.location_chooser = ttk.Button(self, text="choose file", command=self.select_file)
		self.location_entry = Entry(self)
		self.open_button = ttk.Button(self, text="Open", command=self.run_program)

		for each in self.children:
			self.children[each].pack()

	def run_program(self):
		def dothework(self):
			reader = csv.DictReader(csvfile)
			for row in reader:
				year, cal, usa = row['Year,'], row['Gallons from Calf.'], row['Gallons from USA']
				percent_produced = (float(cal.replace(',', '')) / float(usa.replace(',', ''))*100)
				print(percent_produced, "%")
				print(year)
				plt.plot(percent_produced)

		plt.xlabel('Time (s)')
		plt.ylabel('V(t)')

		plt.title('Plot of V(t)=V0*(1-e^(-t/tau ))')

		plt.show()

		if str(self.location_entry.get()) is '': 
			with open(self.location, newline='') as csvfile:
				dothework(self)
		else:
			with open(str(self.location_entry.get()), newline='') as csvfile:
				dothework(self)

	def select_file(self):
		my_filetypes = [('all files', '.*'), ('Comma Separated Value', '.csv')]
		self.location = filedialog.askopenfilename(parent=root, initialdir=os.getcwd(),title="Please select a folder:")
   
root = tk.Tk()
app = Application(root)
root.mainloop()


