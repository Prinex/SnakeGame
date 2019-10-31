import turtle
from tkinter import PhotoImage




def game():

    # window game
    window = turtle.Screen()
    window.title("Snake.exe")
    window.bgcolor("#7FB300")
    window.setup(width=640, height=480, startx=None, starty=None)
    window.tracer(0)

    
    # snake body 
    turtleAvatar = "snakebody.gif"
    head = turtle.Turtle()
    head.speed(0)
    window.addshape(turtleAvatar)
    head.shape(turtleAvatar) 
    head.penup()
    head.color("#303324")
    head.goto(0, 0)
    head.direction = "stop"

    while True:
        window.update()

    window.mainloop()


