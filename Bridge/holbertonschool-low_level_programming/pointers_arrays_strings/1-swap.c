#include <unistd.h>

/**
 * swap_int - Swaps the values of two integers.
 * @a: Pointer to the first integer.
 * @b: Pointer to the second integer.
 *
 * Description:
 * This function swaps the values of the integers pointed to by
 * the pointers `a` and `b`. It uses a temporary variable to store
 * one of the values during the swap process.
 */
void swap_int(int *a, int *b)
{
	int temp; /* Temporary variable to hold one value during the swap */

	temp = *b; /* Store the value of `b` */
	*b = *a;   /* Assign the value of `a` to `b` */
	*a = temp; /* Assign the stored value of `b` (from `temp`) to `a` */
}
