#!/usr/bin/python3
# Loop through numbers from 0 to 99
for i in range(0, 100):
    # If it's not the last number (99), format with two digits and add a comma
    if i < 99:
        print("{:02d}".format(i), end=", ")
    else:
        # For the last number (99), format and move to the next line
        print("{:02d}".format(i), end="\n")
