import turtle
import os
import math
import string
import constant

i=j=k=0

# Initialize
def draw(x,y):
	va.setpos(x*25,y*25)

os.system("clear")

# Frame
turtle.screensize(canvwidth=400, canvheight=400)
ax=turtle.Turtle()
ax.ht()
ax.speed(0)
ax.pencolor("Silver")
ax.pensize(1)
ax.penup()
ax.setpos(-300,300)
ax.pendown()
ax.setpos(-300,300)
ax.setpos(-300,-300)
ax.setpos(300,-300)
ax.setpos(300,300)
ax.setpos(-300,300)
for i in range(-300,0,50):
	ax.penup()
	ax.setpos(i,300)
	ax.pendown()
	ax.setpos(i,-300)
	ax.penup()
	ax.setpos(i+25,-300)
	ax.pendown()
	ax.setpos(i+25,300)
for i in range(25,300,50):
	ax.penup()
	ax.setpos(i,300)
	ax.pendown()
	ax.setpos(i,-300)
	ax.penup()
	ax.setpos(i+25,-300)
	ax.pendown()
	ax.setpos(i+25,300)
for i in range(-300,0,50):
	ax.penup()
	ax.setpos(300,i)
	ax.pendown()
	ax.setpos(-300,i)
	ax.penup()
	ax.setpos(-300,i+25)
	ax.pendown()
	ax.setpos(300,i+25)
for i in range(25,300,50):
	ax.penup()
	ax.setpos(300,i)
	ax.pendown()
	ax.setpos(-300,i)
	ax.penup()
	ax.setpos(-300,i+25)
	ax.pendown()
	ax.setpos(300,i+25)
ax.pencolor("Black")
ax.pensize(4)
ax.penup()
ax.setpos(-300,0)
ax.pendown()
ax.setpos(300,0)
ax.setpos(290,10)
ax.penup()
ax.setpos(290,-10)
ax.pendown()
ax.setpos(300,0)
ax.penup()
ax.setpos(0,-300)
ax.pendown()
ax.setpos(0,300)
ax.setpos(-10,290)
ax.penup()
ax.setpos(10,290)
ax.pendown()
ax.setpos(0,300)
ax.penup()
ax.setpos(24,-9)
ax.pensize(2)
ax.pendown()
ax.setpos(26,-7)
ax.setpos(26,-19)
ax.penup()
ax.setpos(24,-19)
ax.pendown()
ax.setpos(28,-19)
ax.penup()
ax.setpos(-13,29)
ax.pendown()
ax.setpos(-11,31)
ax.setpos(-11,19)
ax.penup()
ax.setpos(-13,19)
ax.pendown()
ax.setpos(-9,19)

va=turtle.Turtle()
va.ht()
va.penup()
va.pensize(3)
va.setpos(-300,0)

t=1
d=0

# Start of Main Programme
print("Turtle Mathematic Function Grapher \nVersion Beta 0.2 \n\nPlease strictly obey the format, otherwise problem would be encountered. \nSupported Range and Domain is [-12,12].\n\"Input \"quit\" to quit, input \"help\" for help. \n\nPlease input the function: ")

va.speed(0)
while t!=0:
	d=0
	x=-12.0
	y=0.0
	va.penup()
	va.ht()
	va.pensize(3)
	va.setpos(-300,0)
	va.penup()
	a=input("f"+str(t)+"(x)=")
	if a.find("quit")!=-1:
		os.system("clear")
		break
	if a.find("help")!=-1:
		print("Note for Using \n\nList of supported functions, constants, and operations: \n+ : Plus\n- : Minus\n* : Time\n/ : Divide\n^ : Exponential\nTrigonometric Functions\ne : Eula's Constant\npi\nDifferentiation (Add Single Quotation Mark (\') at the end of the Function) \nAnti-Differentiation(Integration with f(0)=0)(Add \"int \" at the start of the Function)\n")
		break
	if a.find("=")!=-1:
		print("An error occured. ")
		break
	# Replace function in string
	a=a.replace("^","**")
	a=a.replace("sin","math.sin")
	a=a.replace("cos","math.cos")
	a=a.replace("tan","math.tan")
	a=a.replace("cot","1/math.tan")
	a=a.replace("sec","1/math.cos")
	a=a.replace("csc","1/math.sin")
	a=a.replace("e^x","math.exp(x)")
	if a.find("'")!=-1:
		d=1
		a=a.replace("'","")
	if a.find("int ")!=-1:
		d=2
		a=a.replace("int ","")
	# Coloring
	if (t+6)%7==0: 
		va.pencolor("Blue")
	else:
		if (t+5)%7==0:
			va.pencolor("Red")
		else: 
			if (t+4)%7==0:
				va.pencolor("Black")
			else: 
				if (t+3)%7==0:
					va.pencolor("Magenta")
				else: 
					if (t+2)%7==0:
						va.pencolor("Green")
					else: 
						if (t+1)%7==0:
							va.pencolor("Orange")
						else: 
							if t%8==0:
								va.pencolor("Sienna")
	if d==1:
		x=x-0.02
		ad=a.replace("x","(x+0.04)")
		exec("y1="+a)
		exec("y2="+ad)
		yd=y2-y1
		yd=yd/0.04
		va.penup()
		draw(-12,yd)
		va.pendown()
		while x<=12:
			exec("y1="+a)
			exec("y2="+ad)
			yd=y2-y1
			yd=yd/0.04
			if (yd<=-12 or yd>=12) and va.isdown():
				va.penup()
				va.ht()
			if (yd>=-12 and yd<=12) and not(va.isdown()):
				va.pendown()
				va.st()
			draw(x+0.02,yd)
			x=x+0.04
	else:
		if d==2:
			va.penup()
			va.setpos(0,0)
			x=0
			sd=0
			ad=a.replace("x","(x+0.0005)")
			while x<=12:
				for i in range(0,80):
					exec("y1="+a)
					exec("y2="+ad)
					yd=y1+y2
					yd=yd*0.0005/2
					sd+=yd
					x=x+0.0005
				if (sd<=-12 or sd>=12) and va.isdown():
					va.penup()
					va.ht()
				if (sd>=-12 and sd<=12) and not(va.isdown()):
					va.pendown()
					va.st()
				draw(x,sd)
			va.penup()
			va.setpos(0,0)
			va.pendown()
			ad=a.replace("x","(x-0.0005)")
			x=0
			sd=0
			while x>=-12:
				for i in range(0,80):
					exec("y1="+a)
					exec("y2="+ad)
					yd=y1+y2
					yd=yd*0.0005/2
					sd-=yd
					x=x-0.0005
				if (sd<=-12 or sd>=12) and va.isdown():
					va.penup()
					va.ht()
				if (sd>=-12 and sd<=12) and not(va.isdown()):
					va.pendown()
					va.st()
				draw(x,sd)
		else:
			exec("y="+a)
			va.penup()
			draw(-12,y)
			while x<=12:
				exec("y="+a)
				if (y<=-12 or y>=12) and va.isdown():
					va.penup()
					va.ht()
				if (y>=-12 and y<=12) and not(va.isdown()):
					va.pendown()
					va.st()
				draw(x,y)
				x=x+0.04
	t=t+1



