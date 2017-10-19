import turtle, random

colors  = ["red","green","blue","orange","purple","pink","navyblue","black","lime","cyan","magenta","violet","indigo"]

turtle.width(3)

length = 3

for count in range(100):
	color = random.choice(colors)
	turtle.forward(100)
	turtle.right(30)
	turtle.forward(20)
	turtle.left(60)
	turtle.forward(50)
	turtle.right(30)
	turtle.forward(25)
	turtle.left(50)
	turtle.backward(25)
	turtle.right(60)
	turtle.left(35)
	turtle.forward(60)
	turtle.backward(60)
	turtle.left(30)
	turtle.backward(70)
	turtle.right(30)
	turtle.backward(100)
	turtle.right(100)
	turtle.right(25)
	turtle.left(50)
	turtle.penup()
	turtle.setposition(0, 0)
	turtle.pendown()
	turtle.right(2)
	turtle.left(3)
	turtle.right(4)
	turtle.forward(65)
	turtle.backward(70)
	turtle.left(186)
	turtle.forward(7)
	turtle.right(168)
	turtle.left(3.5)
	turtle.color(color)
	
def Graphic():

	painter = turtle.Turtle()

	painter.pencolor("red")

	ninja = turtle.Turtle()

	ninja.speed(1100)
	turtle.done()        
	win.close()
