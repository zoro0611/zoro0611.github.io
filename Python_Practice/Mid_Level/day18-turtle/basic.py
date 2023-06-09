from turtle import Turtle as t, Screen

sherry = t()
sherry.shape("turtle")
sherry.color("red")

for i in range(4):
    sherry.forward(100)
    sherry.right(90)

my_screen = Screen()
my_screen.exitonclick()

# import heroes
# print(heroes.gen())