'''
Coded by: Harley Ehrman
Date: June 9, 2018

From book:
Introduction to Programming Using Python
By Y Daniel Liang

Instructions (Page 59, Exercise 2.19):
(Financial application: calculate future investment value) Write a program that
reads in an investment amount, the annual interest rate, and the number of years,
and displays the future investment value using the following formula:
futureInvestmentValue = investmentAmount × (1 + monthlyInterestRate)^numberOfMonths
For example, if you enter the amount 1000 , an annual interest rate of 4.25% , and
the number of years as 1 , the future investment value is 1043.33 . Here is a
sample run:
   Enter investment amount: 1000 [Enter]
   Enter annual interest rate: 4.25 [Enter]
   Enter number of years: 1 [Enter]
   Accumulated value is 1043.33
'''
# Enter investment amount
investmentAmount = eval(input("Enter the invest amount: "))

# Enter interest rate
monthlyInterestRate = eval(input("Enter annual interest rate: "))
monthlyInterestRate /= 1200

# Enter number of years
numberOfYears = eval(input("Enter number of years: "))

# Calculate value
accumValue = investmentAmount * (1 + monthlyInterestRate) ** (numberOfYears * 12)

# Display results
print("Accumulated value is: ", float("%0.2f"%accumValue))
