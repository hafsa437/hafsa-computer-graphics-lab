import turtle
import random
import time

s = turtle.Screen()
s.setup(800, 600)
s.bgcolor("#071b45")
s.tracer(0)

# Drawing turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# Moon
t.penup()
t.goto(250, 180)
t.dot(100, "lightyellow")

# Mountains
def mountain(x, y, size):
    t.penup()
    t.goto(x, y)
    t.color("#173c58")
    t.begin_fill()
    t.goto(x+size/2, y+size)
    t.goto(x+size, y)
    t.goto(x, y)
    t.end_fill()

mountain(-400, -150, 300)
mountain(-150, -150, 350)
mountain(150, -150, 300)

# Ground
t.penup()
t.goto(-200, -180)
t.color("darkgreen")
t.begin_fill()
for p in [(-400,-180),(400,-180),(400,-300),(-400,-300)]:
    t.goto(p)
t.end_fill()

# Random stars
stars = []
for i in range(45):
    st = turtle.Turtle()
    st.hideturtle()
    st.penup()
    x = random.randint(-380,380)
    y = random.randint(50,280)
    st.goto(x,y)
    stars.append(st)

# Clouds
clouds = []
for x,y in [(-300,200),(10,220),(300,130)]:
    c = turtle.Turtle()
    c.hideturtle()
    c.penup()
    clouds.append([c,x,y])

# Airplane shape
# Airplane shape (Rotated right)
# Airplane shape (Facing right)
plane_shape = (
    (0,35), (6,10), (22,0), (22,-7),
    (6,-4), (10,-25), (7,-30),
    (0,-12), (-7,-30), (-10,-25),
    (-6,-4), (-22,-7), (-22,0),
    (-6,10), (0,35)
)

s.register_shape("plane", plane_shape)

plane = turtle.Turtle()
plane.shape("plane")
plane.color("white")
plane.penup()
plane.goto(-350,100)


# Shooting stars
shoot = turtle.Turtle()
shoot.hideturtle()
shoot.penup()

sx = -400
sy = 250

# Animation
while True:

    # Stars blinking
    for st in stars:
        st.clear()
        st.dot(random.choice([2,3,5]), "white")

    # Moving clouds
    for c,x,y in clouds:
        c.clear()
        c.goto(x,y)
        c.dot(35,"white")
        c.goto(x+20,y+10)
        c.dot(40,"lightgray")
        c.goto(x+40,y)
        c.dot(35,"white")

    # Update cloud position
    for cloud in clouds:
        cloud[1] += 1
        if cloud[1] > 430:
            cloud[1] = -430

    # Flying airplane
    plane.forward(3)
    if plane.xcor() > 420:
        plane.goto(-420, random.randint(70,220))

    # Shooting star
    shoot.clear()
    shoot.goto(sx,sy)
    shoot.dot(6,"yellow")
    shoot.goto(sx-25,sy+15)
    shoot.pendown()
    shoot.pensize(2)
    shoot.color("white")
    shoot.goto(sx,sy)
    shoot.penup()

    sx += 5
    sy -= 2

    if sx > 450:
        sx = -400
        sy = random.randint(150,280)

    s.update()
    time.sleep(0.04)
