'''
Coded by: Harley Ehrman
Date: June 9, 2018

From book:
Introduction to Programming Using Python
By Y Daniel Liang

Instructions (Page 60, Exercise 2.21):
Financial application: compound value) Suppose you save $100 each month into a
savings account with an annual interest rate of 5%. Therefore, the monthly
interest rate is 0.05/12 = 0.00417. After the first month, the value in the
account becomes

100 * (1 + 0.00417) = 100.417

After the second month, the value in the account becomes

(100 + 100.417) * (1 + 0.00417) = 201.252

After the third month, the value in the account becomes

(100 + 201.252) * (1 + 0.00417) = 302.507
and so on.

Write a program that prompts the user to enter a monthly saving amount
and displays the account value after the sixth month. Here is a sample run of
the program:
   Enter the monthly saving amount: 100 [Enter]
   After the sixth month, the account value is 608.81
'''
# Enter  amount
monthlyAmount = eval(input("Enter the monthly saving amount: "))

MONTHLY_INTEREST_RATE = 0.00417 #Constant

# Calculate interest
accountValueOneMonth = monthlyAmount * (1 + MONTHLY_INTEREST_RATE)
accountValueTwoMonth = (monthlyAmount + accountValueOneMonth) * (1 + MONTHLY_INTEREST_RATE)
accountValueThreeMonth = (monthlyAmount + accountValueTwoMonth) * (1 + MONTHLY_INTEREST_RATE)
accountValueFourMonth = (monthlyAmount + accountValueThreeMonth) * (1 + MONTHLY_INTEREST_RATE)
accountValueFiveMonth = (monthlyAmount + accountValueFourMonth) * (1 + MONTHLY_INTEREST_RATE)
accountValueSixMonth = (monthlyAmount + accountValueFiveMonth) * (1 + MONTHLY_INTEREST_RATE)

# Display results
print("After the sixth month, the account value is: ", float("%0.2f"%accountValueSixMonth))
