'''
Coded by: Harley Ehrman
Date: June 9, 2018

From book:
Introduction to Programming Using Python
By Y Daniel Liang

Instructions (Page 55, Exercise 2.4):
(Convert pounds into kilograms) Write a program that converts pounds 
into kilograms. The program prompts the user to enter a value in 
pounds, converts it to kilograms, and displays the result. One 
pound is 0.454 kilograms.
'''
import math

pounds = eval(input("Enter a value in pounds: "))

kilograms = pounds * 0.454

print(pounds, "pounds is ", kilograms, "kilograms.")
