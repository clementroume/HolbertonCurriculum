#include <unistd.h>
#include "main.h"

/**
 * rev_string - Reverses a string in place.
 * @s: Pointer to the string to be reversed.
 *
 * Description:
 * This function first calculates the length of the string while
 * iterating through it. Then, it swaps characters starting from
 * the outermost indices toward the center to reverse the string
 * in place.
 */
void rev_string(char *s)
{
	int first = 0, last = 0;
	char temp;

	/* Calculate the length of the string */
	while (s[last])
		last++;
	last--; /* Adjust for the last valid index */

	/* Swap characters from both ends toward the center */
	while (first < last)
	{
		temp = s[first];
		s[first] = s[last];
		s[last] = temp;
		first++;
		last--;
	}
}
