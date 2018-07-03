'''
Coded by: Harley Ehrman
Date: June 9, 2018

From book:
Introduction to Programming Using Python
By Y Daniel Liang

Instructions (Page 60, Exercise 2.20):
(Financial application: calculate interest) If you know the balance and the
annual percentage interest rate, you can compute the interest on the next
monthly payment using the following formula:

interest = balance * (annualInterestRate / 1200)
 
Write a program that reads the balance and the annual percentage interest
rate and displays the interest for the next month. Here is a sample run:

   Enter balance and interest rate (e.g., 3 for 3%): 1000, 3.5 [Enter]
   The interest is 2.91667
'''
# Enter investment amount
balance, annualInterestRate = eval(input("Enter balance and interest rate (e.g., 3 for 3%): "))

# Calculate interest
interest = balance * (annualInterestRate / 1200)

# Display results
print("The interest is: ", round(interest, 5))
