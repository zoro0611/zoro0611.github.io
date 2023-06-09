# import colorgram
# colors = colorgram.extract('C:\\Users\\zoro0\\OneDrive\\桌面\\zoro0611.github.io\\Python_Practice\\Mid_Level\\dot_color\\myimg.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list =[ (254, 84, 4), (254, 193, 55), (4, 115, 184), (244, 254, 252), (253, 244, 249), (91, 38, 82), (2, 176, 158), (2, 56, 78), (249, 82, 1), (236, 246, 251), (248, 153, 68), (84, 32, 75), (114, 74, 106), (115, 174, 199), (175, 148, 170), (35, 161, 187), (250, 171, 142), (126, 227, 216), (74, 206, 191), (3, 157, 144), (144, 210, 224), (23, 77, 95), (148, 116, 141), (209, 180, 200), (57, 128, 203), (246, 128, 4), (0, 70, 155), (146, 192, 247)]

import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")

tim.penup()
tim.hideturtle()
tim.left(225)
tim.forward(300)
tim.left(135)

number_of_dots = 100

for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.left(180)

my_screen = t.Screen()
my_screen.exitonclick()