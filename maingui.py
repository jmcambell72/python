# /usr/bin/python

# python program that builds a root window and then a child window widget. 

# import Tkinter lib
from Tkinter import * 
import ttk

# import operating system module 

import os

# import subprocess lib

import subprocess

# app = Frame(mainmenu)


# check docker status

#def dockerfunc():

	# check the docker status function

	
#	print retvalue 

def showprogress():

	showprogress = Tk()

	showpbar = ttk.Progressbar(showprogress, orient=HORIZONTAL, length=200, mode="determinate")
	showpbar.pack()
	showpbar["maximum"] = 100
	showpbar["value"] = 50
	showpbar.mainloop()
	
# function defines a list menu 

def listmenu():
	
	listmenu = Tk()
	
	text = Text(listmenu)
	scroll = Scrollbar(listmenu)
	scroll.pack( side = LEFT, fill=Y)

	bashcmd="ping -c 5 www.bbc.co.uk"
	retvalue = subprocess.check_output(bashcmd, shell=True)
	
	# label = Message( listmenu,textvariable=retvalue, relief=RAISED)
	listmenu.title("Ping Results")
	listmenu.geometry("500x250-500+200")
	text.insert(INSERT, retvalue)
	text.pack()
	


# function contains a submenu built from Tkinter lib
def submenu():

# this creates the basic frame for a screen/widget 
	submenu = Tk()
	submenu.title("sub menu")
	submenu.geometry("400x400")

# this setups a message box 
	messagex = Message(submenu, text = "Hello", bg="RED")
	messagex.pack()

# this adds a list box to the sub menu object 

	w = Listbox(submenu, selectmode=MULTIPLE, bg="GREY")
	w.insert(1, "Python")
	w.insert(2, "Perl")
	w.insert(3, "C")
	w.insert(4, "PHP")
	w.insert(5, "JSP")
	w.insert(6, "Ruby")

	# setups a button on the submenu	
	r = Button(submenu, text="Return")

	#pack the submenu window widget with the button 
	w.pack()
	r.pack()

# this builds the widget on the screen, anything you want in the basic window place before main loop execution 

	submenu.mainloop()

# end of sub menu function


# setup the root window widget 

mainmenu = Tk()
mainmenu.title("Simple GUI")
mainmenu.geometry("800x400")


# place a button on the root window widget 
y = Button(mainmenu, text="Display", command = submenu)

#h = Button(mainmenu, text="Display", command = listmenu)

o = Button(mainmenu, text="Check Docker Status", command = listmenu)

#app.grid()

#lbl1 = Label(app, text = "I am a Label 1")
#lbl2 = Label(app, text = "I am a Label 2")
#lbl3 = Label(app, text = "I am a Label 3")

#lbl1.grid()
#lbl2.grid()
#lbl3.grid()

# pack the window widget with the button
y.pack()
# h.pack()
o.pack()

# run the main loop to display root window widget and keep it running until user break.
mainmenu.mainloop()
