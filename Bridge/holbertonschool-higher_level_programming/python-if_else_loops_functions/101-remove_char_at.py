#!/usr/bin/python3
# Define the function to remove a character at a specific index
def remove_char_at(str, n):
    # Return a new string with the character at index 'n' removed
    return "".join(x for i, x in enumerate(str) if i != n)
