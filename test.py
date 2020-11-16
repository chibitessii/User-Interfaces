import webbrowser
import tkinter
from tkinter import *
from selenium import webdriver

root = Tk()
root.url = ""             # creates a variable "url" to pass 

def open_browser():       # opens the browser

	browser = "Firefox"
	location = "/bin/firefox"
	webbrowser.register(browser,None, webbrowser.BackgroundBrowser(location))
	webbrowser.get(browser).open(root.url)

def select_url(event):    # obtains chosen url from the drop-down list
	root.url = event

variable = StringVar(root)                            # sets default website
website_list =     sorted({"https://www.google.com",  # stored list of websites in menu
						   "https://www.youtube.com",
						   "https://www.uccs.edu",
						   "https://www.yahoo.com",
						   "https://www.duckduckgo.com"})

variable.set("https://www.google.com")  # default website

option_menu = OptionMenu(root, variable, *website_list, command=select_url).pack()  # creates menu to select url
Button1 = Button(root, text="Open", command=open_browser).pack() # allows selection from website menu

display = tkinter.Label(root).pack() # displays the webpage

root.mainloop()