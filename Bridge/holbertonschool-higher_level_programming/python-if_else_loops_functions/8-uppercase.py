#!/usr/bin/python3
# Define the function to convert all lowercase letters to uppercase
def uppercase(str):
    i = 0
    # Loop through each character in the string
    while i < len(str):
        char = str[i]
        # Convert to uppercase if it's a lowercase letter,
        # otherwise print the character as is
        print(chr(ord(char) - 32) if "a" <= char <= "z" else char, end="")
        i += 1
    # Print an empty string to move to a new line after the loop
    print("")
