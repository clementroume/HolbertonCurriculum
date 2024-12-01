#!/usr/bin/python3
# Define the function to print and return the last digit of a number
def print_last_digit(number):
    # Calculate the absolute value of the number
    # and get the last digit using modulo
    digit = abs(number) % 10
    # Print the last digit without a newline
    print(digit, end="")
    # Return the last digit
    return digit
