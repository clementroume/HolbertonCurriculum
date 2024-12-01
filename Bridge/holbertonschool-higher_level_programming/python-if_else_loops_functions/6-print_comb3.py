#!/usr/bin/python3
# Initialize 'a' to 0
a = 0
# Outer loop: a goes from 0 to 8
while a <= 8:
    # Initialize 'b' to 'a + 1'
    b = a + 1
    # Inner loop: b goes from a+1 to 9
    while b <= 9:
        # Print pair (a, b) with appropriate formatting
        if a < 8:
            print("{}{}".format(a, b), end=", ")
        else:
            print("{}{}".format(a, b), end="\n")
        b += 1
    a += 1
