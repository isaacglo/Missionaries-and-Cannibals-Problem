# import package
import turtle
import numpy as np
import Blind_search as BS

# make screen object
# and set size
sc = turtle.Screen()
sc.setup(width=800,height=800, startx=0, starty=0)
sc.bgcolor("#35682d")
sc.tracer(0)

# create the river
river = turtle.Turtle()
river.shape('square')
river.shapesize(40, 15)
river.color("#256d7b")

# make the boat
boat = turtle.Turtle(visible=False)
boat.speed(10)
boat.shape('square')
boat.color("#804000")
boat.shapesize(stretch_wid=2, stretch_len=5)
boat.penup()
boat.goto(-100, 0)
boat.showturtle()



# create the missionarie
m11 = turtle.Turtle(shape='circle', visible=False)
m11.speed(10)
m11.penup()
m11.color("blue")
m11.goto(-230,30)
m11.showturtle()
# create the missionarie
m21 = turtle.Turtle(shape='circle', visible=False)
m21.speed(10)
m21.penup()
m21.color("blue")
m21.goto(-205,30)
m21.showturtle()
# create the missionarie
m31 = turtle.Turtle(shape='circle', visible=False)
m31.speed(10)
m31.penup()
m31.color("blue")
m31.goto(-180,30)
m31.showturtle()

# create the missionarie
m10 = turtle.Turtle(shape='circle', visible=False)
m10.speed(10)
m10.penup()
m10.color("blue")
m10.goto(230,30)
# create the missionarie
m20 = turtle.Turtle(shape='circle', visible=False)
m20.speed(10)
m20.penup()
m20.color("blue")
m20.goto(205,30)
# create the missionarie
m30 = turtle.Turtle(shape='circle', visible=False)
m30.speed(10)
m30.penup()
m30.color("blue")
m30.goto(180,30)

# create the missionarie
c11 = turtle.Turtle(shape='circle', visible=False)
c11.speed(10)
c11.penup()
c11.color("red")
c11.goto(-230,-30)
c11.showturtle()
# create the missionarie
c21 = turtle.Turtle(shape='circle', visible=False)
c21.speed(10)
c21.penup()
c21.color("red")
c21.goto(-205,-30)
c21.showturtle()
# create the missionarie
c31 = turtle.Turtle(shape='circle', visible=False)
c31.speed(10)
c31.penup()
c31.color("red")
c31.goto(-180,-30)
c31.showturtle()

# create the missionarie
c10 = turtle.Turtle(shape='circle', visible=False)
c10.speed(10)
c10.penup()
c10.color("red")
c10.goto(230,-30)
# create the missionarie
c20 = turtle.Turtle(shape='circle', visible=False)
c20.speed(10)
c20.penup()
c20.color("red")
c20.goto(205,-30)
# create the missionarie
c30 = turtle.Turtle(shape='circle', visible=False)
c30.speed(10)
c30.penup()
c30.color("red")
c30.goto(180,-30)


list_m = np.array([[m11,m10],[m21,m20],[m31,m30]])
list_c = np.array([[c11,c10],[c21,c20],[c31,c30]])

# animation of the boat
def move_boat(state):
    boat.speed(5)
    if state[2] == 0:
        boat.goto(100,0)
    else:
        boat.goto(-100,0)

def move_m(state):
    #sc.tracer(0)
    for i in range(3):
        list_m[i,0].hideturtle()
        list_m[i,1].hideturtle()
    for i in range(3):
        list_c[i,0].hideturtle()
        list_c[i,1].hideturtle()

    if state[0] == 3:
        for i in range(3):
            list_m[i,0].showturtle()
    if state[0] == 2:
        for i in range(2):
            list_m[i,0].showturtle()

        list_m[0,1].showturtle()
    if state[0] == 1:
        list_m[0,0].showturtle()
        for i in range(2):
            list_m[i,1].showturtle()
    if state[0] == 0:
        for i in range(3):
            list_m[i,1].showturtle()



    if state[1] == 3:
        for i in range(3):
            list_c[i,0].showturtle()
    if state[1] == 2:
        for i in range(2):
            list_c[i,0].showturtle()

        list_c[0,1].showturtle()
    if state[1] == 1:
        list_c[0,0].showturtle()
        for i in range(2):
            list_c[i,1].showturtle()
    if state[1] == 0:
        for i in range(3):
            list_c[i,1].showturtle()

        


# function for the movement of the boat with passangers
def move(state):
    #if state[2] == 1:
    move_m(state)
    sc.ontimer(move_boat(state), t=1000)
    sc.update()
    
        


nodes = np.array(BS.solver('bfs'))

sc.update()
for i in range(len(nodes)-1):
    
    move( nodes[i+1])
    #sc.update()



sc.exitonclick()