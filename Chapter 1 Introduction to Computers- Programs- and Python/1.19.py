'''
Coded by: Harley Ehrman
Date: June 9, 2018

From book:
Introduction to Programming Using Python
By Y Daniel Liang

Instructions (Page 28, Exercise 1.19):
(Turtle: draw a polygon) Write a program that draws a polygon that
connects the points ( 40 , -69.28 ), ( -40 , -69.28 ), ( -80 , -9.8 ),
( -40 , 69 ), ( 40 , 69 ), and ( 80 , 0 ) in this order, as shown
in Figure 1.20a.
'''
import turtle
turtle.showturtle()
turtle.penup()
turtle.goto(40, -69.28)
turtle.pendown()
turtle.goto(40, -69.28)
turtle.goto(-40, -69.28)
turtle.goto(-80, -9.8)
turtle.goto(-40, 69)
turtle.goto(40, 69)
turtle.goto(80, 0)
turtle.goto(40, -69.28)
turtle.done()
