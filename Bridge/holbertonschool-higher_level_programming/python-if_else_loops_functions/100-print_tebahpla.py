#!/usr/bin/python3
# Loop through the ASCII values of lowercase letters from 'z' (122) to 'a' (97)
for i in range(122, 96, -1):
    # If the ASCII value is even, print the lowercase letter
    if i % 2 == 0:
        print("{}".format(chr(i)), end="")
    # If the ASCII value is odd, print the corresponding uppercase letter
    else:
        print("{}".format(chr(i - 32)), end="")
