...
Coded by: Harley Ehrman
Date: June 9, 2018

From book:
Introduction to Programming Using Python
By Y Daniel Liang

Instructions (Page 55, Exercise 2.6):
(Sum the digits in an integer) Write a program that reads an integer 
between 0 and 1000 and adds all the digits in the integer. For example, 
if an integer is 932 , the sum of all its digits is 14 . (Hint: Use 
the % operator to extract digits, and use the // operator to remove 
the extracted digit. For instance, 932 % 10 = 2 and 932 // 10 = 93 .)
'''
userInput = eval(input("Enter a number between 0 and 1000: "))
less10 = userInput % 10
userInput /= 10
tens = userInput % 10
userInput /= 10
hundreds = userInput % 10
userInput /= 10
sum = hundreds + tens + less10

print("The sum of the digits is ", int(sum))
