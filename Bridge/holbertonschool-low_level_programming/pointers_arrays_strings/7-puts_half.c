#include <unistd.h>
#include "main.h"

/**
 * puts_half - function that prints half of a string
 * @str: The string
 */

void puts_half(char *str)
{
	int len = 0; /* Initialize a variable to store the string length */
	int i;

	/* Calculate the length of the string manually */
	while (str[len] != '\0') /* Loop until the null terminator is found */
		len++;				 /* Increment the length counter for each character */

	/* Calculate the starting point of the second half */
	i = len / 2 + (len % 2 == 0 ? 0 : 1); /* Skip middle character */

	/* Print the second half of the string */
	while (str[i] != '\0')
		_putchar(str[i++]); /* Print the character and increment the index */

	_putchar('\n'); /* Print a newline after printing the second half */
}
