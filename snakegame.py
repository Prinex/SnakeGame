import turtle

def window():

	window = turtle.Screen()
	window.title("Snake.exe")
	window.bgcolor("#85ff40")
	window.setup(width = 640, height = 480, startx = None, starty = None)
	window.tracer(0)
	window.mainloop()

