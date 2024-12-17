from turtle import *
tracer(2)
setposition(0,25)
bgcolor("white")
for i in range(180):
        color("green")
        circle(175-(i*3),100)
        right(180)

        color("red")
        circle(175-(i*3),100)
        left(180)