#include <unistd.h>
#include "main.h"

/**
 * _puts - Prints a string followed by a newline to stdout.
 * @str: Pointer to the string to be printed.
 *
 * Description:
 * This function iterates through the given string and prints each
 * character using the `_putchar` function. After printing the string,
 * it outputs a newline character (`\n`).
 */
void _puts(char *str)
{
	/* Loop through the string until the null terminator is encountered */
	while (*str)
	{
		_putchar(*str); /* Print the current character */
		str++;			/* Move to the next character */
	}
	_putchar('\n'); /* Print the newline character */
}
