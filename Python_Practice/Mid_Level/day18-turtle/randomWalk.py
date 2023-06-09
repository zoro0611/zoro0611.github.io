import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
# tim.shape("turtle")
tim.pensize(10)
tim.speed("fastest")
#array of 10 colors
colors = ["red","blue","green","yellow","orange","purple","pink","brown","black","gray"]
#speed array turtle
speeds = ["fastest","fast","normal","slow","slowest"]

directions = [0,90,180,270]

def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    color = (r,b,g)
    return color

for i in range(200):
    tim.speed(random.choice(speeds))
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

my_screen = t.Screen()
my_screen.exitonclick()
