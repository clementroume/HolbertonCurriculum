#include <unistd.h>
#include "main.h"

/**
 * puts2 - function that prints every other character of a string
 * @str: The string
 */

void puts2(char *str)
{
	int i;

	i = 0; /* Initialize the index variable to 0 */

	/* Loop through the string until the null terminator is reached */
	while (str[i] != '\0')
	{
		if (i % 2 == 0) /* Check if the index is even */
		{
			_putchar(str[i]); /* Print the character at the current index */
			i++;			  /* Move to the next character */
		}
		else
			i++; /* Skip the character by moving to the next index */
	}

	_putchar('\n'); /* Print a newline character after printing the string */
}
