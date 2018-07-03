...
Coded by: Harley Ehrman
Date: June 9, 2018

From book:
Introduction to Programming Using Python
By Y Daniel Liang

Instructions (Page 55, Exercise 2.2):
(Compute the volume of a cylinder) Write a program that reads in the 
radius and length of a cylinder and computes the area and volume using 
the following formulas:
area = radius * radius * π
volume = area * length
'''
import math

radius, length = eval(input("Enter the radius and length of a cylinder (seperated by a comma): "))

area = radius * radius * math.pi
volume = area * length

print("The area is ", area)
print("The volume is ", volume)
