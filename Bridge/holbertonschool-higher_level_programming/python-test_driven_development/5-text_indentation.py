#!/usr/bin/python3
"""
4. Text indentation

This module defines the `text_indentation` function, which formats a given
text string by adding two newlines after specific punctuation marks (., :, ?).
"""


def text_indentation(text):
    """
    Adds two newlines after each occurrence of `.`, `:`, or `?` in a text.

    Args:
        text (str): The text to format. Must be a string.

    Raises:
        TypeError: If `text` is not a string.

    Examples:
        >>> text_indentation("Hello. How are you? Fine:")
        Hello.

        How are you?

        Fine:

        >>> text_indentation("No punctuation")
        No punctuation
    """
    # Validate that `text` is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize variables for processing the text
    result = ""
    temp = ""

    # Iterate through each character in the text
    for char in text:
        temp += char
        if char in ".:?":  # Check for punctuation marks
            result += temp.strip() + "\n\n"  # Add the sentence with 2 newlines
            temp = ""  # Reset the temporary storage

    # Add any remaining text that doesn't end with `.`, `:`, or `?`
    if temp.strip():
        result += temp.strip()

    # Print the formatted text without adding an extra newline at the end
    print(result, end="")
