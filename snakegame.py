import turtle
import time
import random


class Game:
    delay = 0.1
    score_count = 0
    highest_score = 0

    # sprites
    turtleAvatar = "headright.gif"
    turtleBonus = "bonusg.gif"
    seg = "bg123.gif"

    # objects
    def __init__(self):
        self.window = turtle.Screen()
        self.head = turtle.Turtle()
        self.bonus = turtle.Turtle()
        self.score = turtle.Turtle()
        self.segments = []


    def wn(self):
        self.window.title("Snake.exe")
        self.window.bgcolor("#7FB300")
        self.window.setup(width=800, height=600, startx=None, starty=None)
        self.window.tracer(0)

    def sprites(self):
        # Head
        self.head.speed(0)
        self.window.addshape(Game.turtleAvatar)
        self.head.shape(Game.turtleAvatar)
        self.head.penup()
        self.head.color("#303324")
        self.head.goto(0, 0)
        self.head.direction = "stop"

        # Bonus
        self.bonus.speed(0)
        self.window.addshape(Game.turtleBonus)
        self.bonus.shape(Game.turtleBonus)
        self.bonus.penup()
        self.bonus.color("#303324")
        self.bonus.goto(0, 100)

        # Score
        self.score.speed(0)
        self.score.shape("square")
        self.score.color("white")
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(0, 268)
        self.score.write("Score: 0   Highest Score: 0", align="center", font=("Slab Serif", 22, "normal"))

    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def exit(self):
        self.head.direction = "e"

    def move(self):
        # switching the head and body direction to up
        if self.head.direction == "up":
            Game.turtleAvatar = "headup.gif"
            self.window.addshape(Game.turtleAvatar)
            self.head.shape(Game.turtleAvatar)
            y = self.head.ycor()
            self.head.sety(y + 20)

        # switching the head and body direction to down
        if self.head.direction == "down":
            Game.turtleAvatar = "headdown.gif"
            self.window.addshape(Game.turtleAvatar)
            self.head.shape(Game.turtleAvatar)
            y = self.head.ycor()
            self.head.sety(y - 20)

        # switching the head and body direction to left
        if self.head.direction == "left":
            Game.turtleAvatar = "headleft.gif"
            self.window.addshape(Game.turtleAvatar)
            self.head.shape(Game.turtleAvatar)
            x = self.head.xcor()
            self.head.setx(x - 20)

        # switching the head and body direction to right
        if self.head.direction == "right":
            Game.turtleAvatar = "headright.gif"
            self.window.addshape(Game.turtleAvatar)
            self.head.shape(Game.turtleAvatar)
            x = self.head.xcor()
            self.head.setx(x + 20)

        if self.head.direction == "e":
            self.window.bye()

    # key bindings
    def control(self):
        self.window.listen()
        self.window.onkeypress(self.go_up, "w")
        self.window.onkeypress(self.go_down, "s")
        self.window.onkeypress(self.go_left, "a")
        self.window.onkeypress(self.go_right, "d")
        self.window.onkeypress(self.exit, "e")


    def mainGame(self):
        self.wn()
        self.sprites()

        while True:
            self.window.update()

            # Collision with borders
            if self.head.xcor() > 370 or self.head.xcor() < -380 or self.head.ycor() > 285.5 or self.head.ycor() < -265:
                time.sleep(1)
                self.head.goto(0, 0)
                self.head.direction = "stop"

                # Move and clear the list when the snake hits the borders
                for segment in self.segments:
                    segment.goto(2000, 2000)
                self.segments.clear()

                # score reset
                self.score_count = 0
                self.score.clear()
                self.score.write("Score: {}    Highest Score: {}".format(self.score_count, self.highest_score), align="center",
                            font=("Slab Serif", 22, "normal"))

            # Collision with segment
            if self.head.distance(self.bonus) < 20:
                # randomize the bonus on the screen
                x = random.randint(-375, 375)
                y = random.randint(-285, 285)
                self.bonus.goto(x, y)

                # Adding segments
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                self.window.addshape(Game.seg)
                new_segment.shape(Game.seg)
                new_segment.penup()
                self.segments.append(new_segment)

                # incresing the score
                Game.score_count += 5

                if Game.score_count > Game.highest_score:
                    Game.highest_score = Game.score_count
                self.score.clear()
                self.score.write("Score: {}    Highest Score: {}".format(Game.score_count, Game.highest_score), align="center",
                            font=("Slab Serif", 22, "normal"))

            # Body incresing
            for index in range(len(self.segments) - 1, 0, -1):
                x = self.segments[index - 1].xcor()
                y = self.segments[index - 1].ycor()
                self.segments[index].goto(x, y)

            # Incresing with the first segment
            if len(self.segments) > 0:
                x = self.head.xcor()
                y = self.head.ycor()
                self.segments[0].goto(x, y)

            self.control()
            self.move()

            # Checking for body collision
            for segment in self.segments:
                if segment.distance(self.head) < 20:
                    time.sleep(1)
                    self.head.goto(0, 0)
                    self.head.direction = "stop"

                    # Game interrupting
                    for segment in self.segments:
                        segment.goto(2000, 2000)
                    self.segments.clear()
                    Game.score_count = 0

            time.sleep(Game.delay)
        init.window.mainloop()

init = Game()
init.mainGame()

