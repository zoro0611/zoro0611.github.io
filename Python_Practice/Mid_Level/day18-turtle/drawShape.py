from turtle import Turtle as t, Screen
import random
tim = t()
tim.shape("turtle")
tim.penup()
tim.goto(0,100)
tim.pendown()
num_sides = 5
colors = ["red","blue","green","yellow","orange","purple"]
def draw_shape(num_sides):
    tim.color(random.choice(colors))
    for i in range(num_sides):
        tim.right(360/num_sides)
        tim.forward(100)


for i in range(3,10):
    draw_shape(i)

my_screen = Screen()
my_screen.exitonclick()