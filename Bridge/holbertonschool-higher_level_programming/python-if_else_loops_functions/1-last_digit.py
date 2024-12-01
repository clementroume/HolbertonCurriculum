#!/usr/bin/python3
# Importing the random module to generate random numbers
import random

# Generate a random integer between -10000 and 10000
number = random.randint(-10000, 10000)

# Get the last digit of the number
digit = abs(number) % 10

# Adjust the digit to be negative if the number is negative
if number < 0:
    digit = -digit

# Check the value of the last digit and print the appropriate message
if digit > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5")
elif digit == 0:
    print(f"Last digit of {number} is {digit} and is 0")
else:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
