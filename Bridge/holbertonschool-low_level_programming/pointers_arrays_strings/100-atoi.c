#include <unistd.h>

/**
 * _atoi - function that converts a string to an integer
 * @s: String to be converted to int
 *
 * Return: Converted int
 */
int _atoi(char *s)
{
	int sign = 1;		/* Initialize sign as positive */
	unsigned int n = 0; /* Initialize the result as 0 */

	/* Skip non-digit characters */
	while (*s && (*s < '0' || *s > '9'))
	{
		if (*s == '-')
			sign *= -1; /* Toggle the sign if a minus sign is found */
		s++;			/* Move to the next character */
	}

	/* Convert string of digits to an integer */
	while (*s >= '0' && *s <= '9')
	{
		n = (10 * n) + (*s - '0'); /* Build the number digit by digit */
		s++;					   /* Move to the next character */
	}

	return (sign * n); /* Return the final result with the correct sign */
}
