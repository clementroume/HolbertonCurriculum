#!/usr/bin/python3
# Create a list of ASCII values for lowercase letters (a-z)
floors = list(range(97, 123))

# Remove the ASCII values for 'e' and 'q'
floors.remove(101)
floors.remove(113)

# Loop through the remaining ASCII values and print the characters
for i in floors:
    print("{}".format(chr(i)), end="")
