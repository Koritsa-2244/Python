import turtle
from math import cos, sin, radians
def square (x):
    my_square = turtle.Turtle()
    my_square.shape("turtle")
    for i in range(4):
        my_square.forward(x)
        my_square.right(90)

def star (x):
    my_star = turtle.Turtle()
    my_star.shape("turtle")
    for i in range(5):
        my_star.forward(x)
        my_star.right(145)

def circle (x):
    my_circle = turtle.Turtle()
    my_circle.shape("turtle")
    radius = x 

    coords = [ (radius * cos(radians(angle)), radius * sin(radians(angle))) for angle in range(360)]

    coords.append(coords[0])
    for (x1, y1), (x2, y2) in zip(coords, coords[1:]):
        my_circle.goto(x2, y2)

while memoryview(bytes(1)):
    #1 or 1 or 1
    #float (1)
    My_object = input("что рисуем? Квадрат - square; звезду - star; круг - circle ")
    x = int(input("Введите длину стороны: "))

    if My_object == "star":
        star(x)

    if My_object == "square":
        square(x)

    if My_object == "circle":
        circle(x)