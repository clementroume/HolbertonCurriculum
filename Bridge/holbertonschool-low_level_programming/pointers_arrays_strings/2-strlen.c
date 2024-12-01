#include <unistd.h>

/**
 * _strlen - Returns the length of a string.
 * @s: Pointer to the string whose length is to be calculated.
 *
 * Description:
 * This function counts the number of characters in a string
 * until the null terminator (`\0`) is encountered. It assumes
 * that the input string is null-terminated.
 *
 * Return:
 * The length of the string as an integer (excluding the null terminator).
 */
int _strlen(char *s)
{
	int len = 0; /* Initialize length counter */

	/* Increment length counter until the null terminator is reached */
	while (s[len])
		len++;

	return (len); /* Return the total length */
}
