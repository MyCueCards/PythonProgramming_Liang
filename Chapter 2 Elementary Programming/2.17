'''
Coded by: Harley Ehrman
Date: June 9, 2018

From book:
Introduction to Programming Using Python
By Y Daniel Liang

Instructions (Page 59, Exercise 2.17):
(Health application: compute BMI) Body mass index (BMI) is a measure of health
based on weight. It can be calculated by taking your weight in kilograms and
dividing it by the square of your height in meters. Write a program that prompts
the user to enter a weight in pounds and height in inches and displays the BMI.
Note that one pound is 0.45359237 kilograms and one inch is 0.0254 meters. Here
is a sample run:
   Enter weight in pounds: 95.5 [Enter]
   Enter height in inches: 50 [Enter]
   BMI is 26.8573
'''
import math

# Prompt the user to enter weight in pounds
weight = eval(input("Enter weight in pounds: "))

# Prompt the user to enter height in inches
height = eval(input("Enter height in inches: "))

onePound = 0.45359237 # Constant
oneInch = 0.0254 # Constant

weight = weight * onePound
height = height * oneInch
bmi = weight / math.pow(height, 2)

print("BMI is ", round(bmi, 4))
