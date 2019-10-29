import turtle



def game():

    # window game
    window = turtle.Screen()
    window.title("Snake.exe")
    window.bgcolor("#7FB300")
    window.setup(width=640, height=480, startx=None, starty=None)
    window.tracer(0)

    # https://inventwithscratch.com/book/chapter6.html for sprite
    # https://blog.trinket.io/using-images-in-turtle-programs/
    # snake body
    # ex: turtleAvatar = "image.png"
    body = turtle.Turtle()
    body.speed(0)
    body.shape("square") #turtle_avatar
    body.penup()
    body.color("#303324")
    body.goto(0, 0)
    body.shapesize(0.75, 0.75, 0.75)

    while True:
        window.update()

    window.mainloop()
