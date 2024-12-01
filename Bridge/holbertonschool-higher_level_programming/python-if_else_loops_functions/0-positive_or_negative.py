#!/usr/bin/python3
# Importing the random module to generate random numbers
import random

# Generate a random integer between -10 and 10
number = random.randint(-10, 10)

# Check if the number is positive, zero, or negative
if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")
