import turtle
import time
import random
# movement function

delay = 0.1

# window game
window = turtle.Screen()
window.title("Snake.exe")
window.bgcolor("#7FB300")
window.setup(width=640, height=480, startx=None, starty=None)
window.tracer(0)
    
# snake head 
turtleAvatar = "headright.gif"  
head = turtle.Turtle() 
head.speed(0) 
window.addshape(turtleAvatar)  
head.shape(turtleAvatar) 
head.penup()
head.color("#303324")
head.goto(0, 0)
head.direction = "stop"


# snake bonus 
turtleBonus = "bonusg.gif"
bonus = turtle.Turtle()
bonus.speed(0)
window.addshape(turtleBonus)
bonus.shape(turtleBonus) 
bonus.penup()
bonus.color("#303324")
bonus.goto(0, 100)

# body segments
segments = []

# movement functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right" 

def move():
    # switching the head and body direction to up
    if head.direction == "up":
        turtleAvatar = "headup.gif"
        window.addshape(turtleAvatar) 
        head.shape(turtleAvatar)

        seg = "bg12.gif"

        y = head.ycor()
        head.sety(y + 20)


    # switching the head and body direction to up
    if head.direction == "down":
        turtleAvatar = "headdown.gif"
        window.addshape(turtleAvatar) 
        head.shape(turtleAvatar)
        y = head.ycor()
        head.sety(y - 20)


    # switching the head and body direction to up
    if head.direction == "left":
        turtleAvatar = "headleft.gif"
        window.addshape(turtleAvatar) 
        head.shape(turtleAvatar) 
        x = head.xcor()
        head.setx(x - 20)


    # switching the head and body direction to up
    if head.direction == "right":
        turtleAvatar = "headright.gif"
        window.addshape(turtleAvatar) 
        head.shape(turtleAvatar) 
        x = head.xcor()
        head.setx(x + 20)


# key bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

# main loop game
while True:
    window.update()

    # Collision with segment
    if head.distance(bonus) < 20:
        # randomize the bonus on the screen
        x = random.randint(-310, 310)
        y = random.randint(-205, 205)
        bonus.goto(x, y)

        # Adding segments
        seg = "bg12.gif"
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        window.addshape(seg)
        new_segment.shape(seg)
        new_segment.color("#303324")
        new_segment.penup()
        segments.append(new_segment)
    

    # Body incresing
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Incresing with the first segment
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


    move()
    time.sleep(delay)

window.mainloop()