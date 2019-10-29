import turtle

def window():

	window = turtle.Screen()
	window.title("Snake.exe")
	window.bgcolor("#85ff40")
	window.setup(width = 640, height = 480, startx = None, starty = None)
	window.tracer(0)

def snake_body():
	body = turtle.Turtle()
	body.shape("square")
	body.penup()
	body.color("black")
	body.goto(0, 0)