import turtle
import time
import random

# snake's speed
delay = 0.1

score_count = 0

highest_score = 0

# window game
window = turtle.Screen()
window.title("Snake.exe")
window.bgcolor("#7FB300")
window.setup(width=800, height=600, startx=None, starty=None)
window.tracer(0)
    
# snake head 
turtleAvatar = "./sprites/headright.gif"  
head = turtle.Turtle() 
head.speed(0) 
window.addshape(turtleAvatar)  
head.shape(turtleAvatar) 
head.penup()
head.color("#303324")
head.goto(0, 0)
head.direction = "stop"


# snake bonus 
turtleBonus = "./sprites/bonusg.gif"
bonus = turtle.Turtle()
bonus.speed(0)
window.addshape(turtleBonus)
bonus.shape(turtleBonus) 
bonus.penup()
bonus.color("#303324")
bonus.goto(0, 100)

# body segments
segments = []


# Score counter
score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 268)
score.write("Score: 0   Highest Score: 0", align = "center", font = ("Slab Serif", 22, "normal"))

# movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right" 
def exit():
    head.direction = "e"

def move():
    # switching the head and body direction to up
    if head.direction == "up":
        turtleAvatar = "./sprites/headup.gif"
        window.addshape(turtleAvatar) 
        head.shape(turtleAvatar)
        y = head.ycor()
        head.sety(y + 20)


    # switching the head and body direction to up
    if head.direction == "down":
        turtleAvatar = "./sprites/headdown.gif"
        window.addshape(turtleAvatar) 
        head.shape(turtleAvatar)
        y = head.ycor()
        head.sety(y - 20)


    # switching the head and body direction to up
    if head.direction == "left":
        turtleAvatar = "./sprites/headleft.gif"
        window.addshape(turtleAvatar) 
        head.shape(turtleAvatar) 
        x = head.xcor()
        head.setx(x - 20)


    # switching the head and body direction to up
    if head.direction == "right":
        turtleAvatar = "./sprites/headright.gif"
        window.addshape(turtleAvatar) 
        head.shape(turtleAvatar) 
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "e":
        window.bye()


# key bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")
window.onkeypress(exit, "e")

# main loop game
while True:
    window.update()

    # Collision with the borders
    if head.xcor() > 370 or head.xcor() < -380 or head.ycor()  > 285.5 or head.ycor() < -265:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

    

        # Move an clear the list when the snake hits the borders
        for segment in segments:
            segment.goto(2000, 2000)
        segments.clear()


        # score reset
        score_count = 0
        score.clear()
        score.write("Score: {}    Highest Score: {}".format(score_count, highest_score), align = "center", font = ("Slab Serif", 22, "normal"))
    

    # Collision with segment
    if head.distance(bonus) < 20:
        # randomize the bonus on the screen
        x = random.randint(-375, 375)
        y = random.randint(-285, 285)
        bonus.goto(x, y)

        # Adding segments
        seg = "./sprites/bg123.gif"
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        window.addshape(seg)
        new_segment.shape(seg)
        new_segment.color("#303324")
        new_segment.penup()
        segments.append(new_segment)


        # incresing the score
        score_count += 5

        if score_count > highest_score:
            highest_score = score_count
        score.clear()
        score.write("Score: {}    Highest Score: {}".format(score_count, highest_score), align = "center", font = ("Slab Serif", 22, "normal"))
    
    # Body incresing an score
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

      # Checking for body collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Game interrupting
            for segment in segments:
                segment.goto(2000, 2000)

            segments.clear()

             # score reset
            score_count = 0
           
    time.sleep(delay)

window.mainloop()
    
