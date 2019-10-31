import turtle
import time

# movement functions

delay = 0.1

def move(head, direction):
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def game():

    # window game
    window = turtle.Screen()
    window.title("Snake.exe")
    window.bgcolor("#7FB300")
    window.setup(width=640, height=480, startx=None, starty=None)
    window.tracer(0)

    
    # snake body 
    turtleAvatar = "snakehead.gif"
    head = turtle.Turtle()
    head.speed(0)
    window.addshape(turtleAvatar)
    head.shape(turtleAvatar) 
    head.penup()
    head.color("#303324")
    head.goto(0, 0)
    head.direction = "right"

    while True:
        window.update()
        move(head, head.direction)
        time.sleep(delay)

    window.mainloop()


