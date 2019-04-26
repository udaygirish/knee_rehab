#IMPORT LIBRARIES
import os
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox
import serial
from PIL import Image,ImageTk
from tkinter import ttk
from itertools import count
import sys
import threading
import time
from resizeimage import resizeimage
LARGE_FONT = ("Verdana",18)
CONNECT TO PORT AT REQ. BAUD RATE
ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate = 9600
#ser.open()
#ser.is_open
ser1= serial.Serial('/dev/ttyACM0')
ser1.baudrate =115200	

i=0
class nitc(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)
		container.pack(side="top",fill="both",expand=True)
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=2)
		self.frames ={}
		for F in (PageFour, PageOne, PageTwo, PageThree, StartPage):
			frame = F(container,self)
			self.frames[F]= frame
			frame.grid(row=0,column=0,sticky='nsew')
		self.show_frame(F)
	def show_frame(self,cont):
		frame=self.frames[cont]
		frame.tkraise()

class StartPage(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self,text="DEPARTMENT OF MECHANICAL ENGINEERING",font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		label = tk.Label(self,text="StartPage",font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		button7 = tk.Button(self,text="Knee Rehabilitation System",command = lambda: intro(self),foreground="YELLOW",background= "RED",height =2 , width = 20)
		button7.pack()
		button1 = ttk.Button(self,text="Exercise1",command = lambda :controller.show_frame(PageOne),cursor ='hand1')
		button1.pack()
		button2 = ttk.Button(self,text="Exercise2",command = lambda : controller.show_frame(PageTwo),cursor ='hand1')
		button2.pack()
		button3 = ttk.Button(self,text="Exercise3",command = lambda : controller.show_frame(PageThree),cursor ='hand1')
		button3.pack()
		button4 = ttk.Button(self,text="Exercise4",command = lambda : controller.show_frame(PageFour),cursor ='hand1')
		button4.pack()
		button5 = ttk.Button(self,text="About",command = lambda : about(self),cursor ='man')
		button5.pack()
		button6 = ttk.Button(self,text="Exit",command = lambda : exit(self),cursor ='pirate')
		button6.pack()
		button25 = ttk.Button(self,text="HELP",command = lambda: customer_care(self),cursor ='man')
		button25.pack(side = BOTTOM)
		button26 = ttk.Button(self,text="CREDITS",command = lambda: credits(self),cursor ='man')
		button26.pack(side = RIGHT, pady=5)


class PageOne(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self,text="DEPARTMENT OF MECHANICAL ENGINEERING",font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		label = ttk.Label(self,text="Exercise1",font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		button8 = tk.Button(self,text="Knee Rehabilitation System",command = lambda: intro(self),foreground="YELLOW",background= "RED",height =2 , width = 20)
		button8.pack()
		button9 = ttk.Button(self,text="Home",command = lambda : controller.show_frame(StartPage),cursor ='hand1')
		button9.pack()
		button16= ttk.Button(self,text="Start",command = lambda: press1(self),cursor ='hand1')
		button16.pack()
		button17= ttk.Button(self,text="Stop",command = lambda: press2(self),cursor ='hand1')
		button17.pack()

class PageTwo(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self,text="DEPARTMENT OF MECHANICAL ENGINEERING",font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		label = ttk.Label(self,text="Exercise2",font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		button10 = tk.Button(self,text="Knee Rehabilitation System",command = lambda: intro(self),foreground="YELLOW",background= "RED",height =2 , width = 20)
		button10.pack()
		button11 = ttk.Button(self,text="Home",command = lambda : controller.show_frame(StartPage),cursor ='hand1')
		button11.pack()
		button18= ttk.Button(self,text="Start",command = lambda: press3(self),cursor ='hand1')
		button18.pack()
		button19= ttk.Button(self,text="Stop",command = lambda: press4(self),cursor ='hand1')
		button19.pack()

class PageThree(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self,text="DEPARTMENT OF MECHANICAL ENGINEERING",font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		label = ttk.Label(self,text="Exercise3",font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		button12 = tk.Button(self,text="Knee Rehabilitation System",command = lambda: intro(self),foreground="YELLOW",background= "RED",height =2 , width = 20)
		button12.pack()
		button13 = ttk.Button(self,text="Home",command = lambda : controller.show_frame(StartPage),cursor ='hand1')
		button13.pack()
		button20= ttk.Button(self,text="Start",command = lambda: press5(self),cursor ='hand1')
		button20.pack()
		button21= ttk.Button(self,text="Stop",command = lambda: press6(self),cursor ='hand1')
		button21.pack()


class PageFour(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self,text="DEPARTMENT OF MECHANICAL ENGINEERING",font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		label = ttk.Label(self,text="Exercise4",font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		button14 = tk.Button(self,text="Knee Rehabilitation System",command = lambda: intro(self),foreground="YELLOW",background= "RED",height =2 , width = 20)
		button14.pack()
		button15 = ttk.Button(self,text="Home",command = lambda : controller.show_frame(StartPage),cursor ='hand1')
		button15.pack()
		button22= ttk.Button(self,text="Start",command = lambda: press7(self),cursor ='hand1')
		button22.pack()
		button23= ttk.Button(self,text="Stop",command = lambda: press8(self),cursor ='hand1')
		button23.pack()
		button24= ttk.Button(self,text="Set Knee Pos",command = lambda: press9(self),cursor ='hand1')
		button24.pack()
		slider = Scale(self,from_=0,to=200,orient=VERTICAL)
		slider.pack()


def press1(self):
	#ser.write(b'1')
	messagebox.showinfo("START","Please place your leg on the machine")
def press2(self):
	#ser.write(b'2')
	messagebox.showinfo("STOP","Please remove your leg from the machine")
def press3(self):
	#ser.write(b'3')
	messagebox.showinfo("START","Please place your leg on the machine")
def press4(self):
	#ser.write(b'2')
	messagebox.showinfo("STOP","Please remove your leg from the machine")
def press5(self):
	#while True:
		#a= ser1.read()
		#print(a)
		#if a==b'1':
		##if a==b'2':
			#ser.write(b'2')
		#ser.write(b'4')
	messagebox.showinfo("START","Please place your leg on the machine")
def press6(self):
	#ser.write(b'2')
	messagebox.showinfo("STOP","Please remove your leg from the machine")
def press7(self):
	#ser.write(b'5')
	messagebox.showinfo("START","PLease place your leg on the machine")
def press8(self):
	#ser.write(b'2')
	messagebox.showinfo("STOP","Please remove your leg from the machine")
def press9(self):
	#while (i<10):
	#	ser.write(b'8')
	messagebox.showinfo("INSTRUCTION","Now please press Start button")

def about(self):
	messagebox.showinfo("ABOUT KNEE REHABILITATION SYSTEM", "KNEE REHABILITATION SYSTEM WAS DEVELOPED BY A GROUP OF MECHANICAL ENGINEERING STUDENTS. \n NAMES: \n M.UDAY GIRISH \n V.SAI RAMA KRISHNA \n JADAV PRASAD \n G.B.S.R KRISHNA \n SAGAR ELIGAR \n V.MUKESH")
	#ser.write(b'9')
def intro(self):
	messagebox.showinfo("INTRO","Knee Rehab Project NITC")
	#ser.write(b'9')
def exit(self):
	answer = messagebox.askquestion("EXIT","ARE YOU SURE ABOUT QUITTING THE SYSTEM",icon="warning")
	if answer == 'yes':
		messagebox.showinfo("...","THANK YOU")
		messagebox.showinfo("FEEDBACK","Please provide your feedback")
		#ser.write(b'9')
		root.destroy()
	if answer == 'no':
		messagebox.showinfo("...","RESUMING THE OPERATION")
		#ser.write(b'9')
		root.destroy()
		os.system("python3 ~/Desktop/test.py")

def customer_care(self):
	messagebox.showinfo("Contact Number","Please contact +918137080271 for support and assistance.")
	messagebox.showinfo("Mail id","Otherwise drop a mail to support_btechprojB15@gmail.com")
	messagebox.showinfo("Customer Care","THANK YOU")
	#ser.write(b'9')

def credits(self):
	messagebox.showinfo("CREDITS","GUIDES \n Department of Mechanical Engineering \n Dr.M.L.Joy \n Dr.Ashesh Saha")
	#ser.write(b'9')
root = nitc()
root.title("KNEE REHABILITATION SYSTEM : NATIONAL INSTITUTE OF TECHNOLOGY, CALICUT")
root.geometry('800x480')
myFont1 = font.Font(family = 'Helvetica', size = 16, weight = 'bold')
myFont = font.Font(family = 'Helvetica', size = 10, weight = 'bold')
photo = PhotoImage(file = "~/Music/nitl.png")
image = Image.open("/home/udaygirish/Music/nitl.png")
#cover= resizeimage.resize_cover(image,[150,150],validate=False)
#cover.save('/home/udaygirish/photo.png',image.format)
photo = Image.open("/home/udaygirish/Music/nitl.png")
nx,ny= photo.size
image = photo.resize((int(nx/2),int(ny/2.3)),Image.BICUBIC)
photo2= Image.open("/home/udaygirish/Desktop/cpm.jpg")
nx,ny = photo2.size
image1 = photo2.resize((int(nx/20),int(ny/22)),Image.BICUBIC)
image.save("/home/udaygirish/photo.png")
image1.save("/home/udaygirish/photo1.png") 
status = Label(root, text = "Press the respective number for selecting the exercise" , font = myFont ,bd =1 , relief = SUNKEN, anchor = S)
status.pack(side = BOTTOM)
status = Label(root, text = "In case of Emergency Please press the RED SWITCH(EMERGENCY STOP)" , font = myFont ,bd =1 , relief = SUNKEN, anchor = S,bg="RED")
status.pack(side = BOTTOM)
photo1 = PhotoImage(file = "/home/udaygirish/photo.png")
photo2 = PhotoImage(file = "/home/udaygirish/photo1.png")
label1 = Label(root,image=photo2)
label1.pack()
label1.place(x=0,y=0)
label = Label(root,image=photo1)
label.pack()
label.place(x=700,y=0)
root.mainloop()

