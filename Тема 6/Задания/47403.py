from turtle import *

tracer(0)
koef = 30

for i in range(4):
    forward(koef * 12)
    right(90)
right(30)
for i in range(3):
    forward(koef * 8)
    right(60)
    forward(koef * 8)
    right(120)

up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()