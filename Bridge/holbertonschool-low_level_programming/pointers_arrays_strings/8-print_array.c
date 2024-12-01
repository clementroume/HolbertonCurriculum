#include <stdio.h>
#include <unistd.h>
#include "main.h"

/**
 * print_array - function that prints n elements of an array of integers
 * @a: The array
 * @n: Length of the array
 */
void print_array(int *a, int n)
{
	int i = 0;

	/* Loop through the array and print each element */
	while (i < n)
	{
		/* Print a comma if it's not the last element */
		if (i != (n - 1))
			printf("%d, ", a[i]);
		else
			printf("%d", a[i]); /* Print the last element without a comma */
		i++;
	}
	printf("\n"); /* Print a newline after printing the array */
}
