'''
Coded by: Harley Ehrman
Date: June 9, 2018

From book:
Introduction to Programming Using Python
By Y Daniel Liang

Instructions (Page 59, Exercise 2.18):
(Current time) Listing 2.7, ShowCurrentTime.py, gives a program that displays
the current time in GMT. Revise the program so that it prompts the user to
enter the time zone in hours away from (offset to) GMT and displays the time
in the specified time zone. Here is a sample run:
   Enter the time zone offset to GMT: -5 [Enter]
   The current time is 4:50:34
'''
import time

timeOffset = eval(input("Enter the time zone offset to GMT: "))

# Get current time
currentTime = time.time()

# Obtain the total seconds since midnight, June 10, 2018
totalSeconds = int(currentTime)

# Get the current second 
currentSecond = totalSeconds % 60 

# Obtain the total minutes
totalMinutes = totalSeconds // 60 

# Compute the current minute in the hour
currentMinute = totalMinutes % 60

# Obtain the total hours
totalHours = totalMinutes // 60

# Compute the current hour
currentHour = totalHours % 24

# Display results
print("Current time is " + str(currentHour + timeOffset) + ":"
    + str(currentMinute) + ":" + str(currentSecond) + " GMT")
