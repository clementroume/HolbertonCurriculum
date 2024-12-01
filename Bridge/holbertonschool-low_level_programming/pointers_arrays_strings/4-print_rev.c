#include <unistd.h>
#include "main.h"

/**
 * print_rev - Prints a string in reverse, followed by a newline.
 * @s: Pointer to the string to be reversed and printed.
 *
 * Description:
 * This function calculates the length of the string while
 * iterating through it. Then, it iterates backward through
 * the string, printing each character in reverse order.
 * Finally, it prints a newline character (`\n`).
 */
void print_rev(char *s)
{
	int len = 0;

	/* Calculate the length of the string */
	while (s[len])
		len++;

	/* Print characters in reverse order */
	while (--len >= 0)
	{
		_putchar(s[len]);
	}

	_putchar('\n'); /* Print a newline character */
}
