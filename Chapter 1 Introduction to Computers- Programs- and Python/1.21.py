'''
Coded by: Harley Ehrman
Date: June 9, 2018

From book:
Introduction to Programming Using Python
By Y Daniel Liang

Instructions (Page 29, Exercise 1.21):
(Turtle: display a clock) Write a program that displays a
clock to show the time 9:15:00, as shown in Figure 1.20c
'''
import turtle
turtle.showturtle()
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.goto(0, 0)
turtle.circle(100)

turtle.penup()
turtle.goto(-10, -15)
turtle.pendown()
turtle.write("9:15:00")

turtle.penup()
turtle.goto(0, 5)
turtle.pendown()
turtle.write("6")

turtle.penup()
turtle.goto(0, 185)
turtle.pendown()
turtle.write("12")

turtle.penup()
turtle.goto(90, 100)
turtle.pendown()
turtle.write("3")

turtle.penup()
turtle.goto(-90, 100)
turtle.pendown()
turtle.write("9")

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.goto(0, 175)

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.goto(75, 100)

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.color("gray")
turtle.goto(-50, 100)

turtle.done()
