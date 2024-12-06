from turtle import *
tracer(50)
setposition(0,25)
bgcolor("white")
colors=["yellow",'red',"green","black"]
hideturtle
for i in range(180):
    for c in colors:
        circle(175-i,100)
        left(90)
        circle(175-i,100)
        right(60)