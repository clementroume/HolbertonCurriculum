#!/usr/bin/python3
# Define the function to check if a character is lowercase
def islower(c):
    # Check if the Unicode value of 'c' is within the range
    # for lowercase letters
    if ord(c) >= ord("a") and ord(c) <= ord("z"):
        return True
    return False
