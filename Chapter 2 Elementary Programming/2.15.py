'''
Coded by: Harley Ehrman
Date: June 9, 2018

From book:
Introduction to Programming Using Python
By Y Daniel Liang

Instructions (Page 58, Exercise 2.15):
(Geometry: area of a hexagon) Write a program that prompts the user to
enter the side of a hexagon and displays its area. The formula for
computing the area of a hexagon is Area = Area = 3√3/2 * s^2 where s is
the length of a side. Here is a sample run:
  Enter the side: 5.5 [Enter]
  The area of the hexagon is 78.5895
'''
import math

side = eval(input("Enter the side: "))
area = ((3 * math.sqrt(3)) / 2) * side ** 2
print("The area of the hexagon is ", round(area, 4))
