#include <unistd.h>

/**
 * reset_to_98 - Updates the value of the integer pointed to by the input
 *               pointer to 98.
 * @n: Pointer to the integer whose value is to be updated.
 *
 * Description:
 * This function directly modifies the value stored at the memory location
 * pointed to by the `n` pointer. It is typically used to demonstrate the
 * usage of pointers in C and how to manipulate the values they point to.
 */
void reset_to_98(int *n)
{
	*n = 98; /* Dereference the pointer to update the value it points to */
}
