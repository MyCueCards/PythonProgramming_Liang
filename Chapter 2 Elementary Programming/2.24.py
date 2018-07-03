'''
Coded by: Harley Ehrman
Date: June 9, 2018

From book:
Introduction to Programming Using Python
By Y Daniel Liang

Instructions (Page 61, Exercise 2.24):
(Turtle: draw four hexagons) Write a program that draws four hexagons in the
center of the screen, as shown in Figure 2.4b
'''
import turtle

turtle.penup()
turtle.goto(-40, 0)
turtle.pendown()
turtle.circle(40, steps = 6)

turtle.penup()
turtle.goto(40, 0)
turtle.pendown()
turtle.circle(40, steps = 6)

turtle.penup()
turtle.goto(-40, -80)
turtle.pendown()
turtle.circle(40, steps = 6)

turtle.penup()
turtle.goto(40, -80)
turtle.pendown()
turtle.circle(40, steps = 6)

turtle.done()
