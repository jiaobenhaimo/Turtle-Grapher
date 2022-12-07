import turtle
import os
import math
import string
e=math.e
pi=math.pi
# Initialize
def draw(x,y):
	va.setpos(x*25,y*25)

os.system("clear")
turtle.screensize(canvwidth=400, canvheight=400)
ax=turtle.Turtle()
ax.ht()
ax.speed(0)
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
va=turtle.Turtle()
va.penup()
va.pensize(3)
va.setpos(-300,0)
t=1
i=j=k=0
o=0

# Start of Main Programme
print("Turtle Mathematic Function Grapher \nVer Beta 0.1 \nNote: \nList of supported functions, constants, and operations: \n+ : Plus\n- : Minus\n* : Time\n/ : Divide\n^ : Exponential\nTrigonometric Functions\ne : Eula's Constant\npi\n\nPlease strictly obey the format, otherwise problem would be encountered. \nSupported Range and Domain is [-12,12].\nPlease input the function: ")

va.speed(0)
while t!=0:
	x=-12.0
	y=0.0
	va.penup()
	va.pensize(3)
	va.setpos(-300,0)
	va.penup()
	a=input("\nf"+str(t)+"(x)=")
	if a.find("=")!=-1:
		print("An error occured. ")
		break
	a=a.replace("^","**")
	a=a.replace("sin","math.sin")
	a=a.replace("cos","math.cos")
	a=a.replace("tan","math.tan")
	a=a.replace("cot","math.cot")
	a=a.replace("sec","math.sec")
	a=a.replace("csc","math.csc")
	a=a.replace("e^x","math.exp(x)")

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
								va.pencolor("DarkOrange2")
	exec("y="+a)
	va.setpos(x*25,y*25)
	while x<=12:
		exec("y="+a)
		va.pendown()
		if y>=-12 and y<=12:
			draw(x,y)
		x=x+0.04
	
	t=t+1



