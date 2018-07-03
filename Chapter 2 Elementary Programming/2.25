'''
Coded by: Harley Ehrman
Date: June 9, 2018

From book:
Introduction to Programming Using Python
By Y Daniel Liang

Instructions (Page 61, Exercise 2.25):
(Turtle: draw a rectangle) Write a program that prompts the user to enter the
center of a rectangle, width, and height, and displays the rectangle, as
shown in Figure 2.4c
'''
import turtle

x, y = eval(input("Enter x, y coordinates: "))
width, height = eval(input("Enter the width and height: "))

turtle.penup()
turtle.goto(x, y)
turtle.pendown()

turtle.goto(x + width, y)
turtle.goto(width, height)
turtle.goto(x, height)
turtle.goto(x, y)

turtle.done()
