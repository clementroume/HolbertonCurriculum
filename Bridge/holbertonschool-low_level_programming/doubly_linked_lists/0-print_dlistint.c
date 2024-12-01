#include "lists.h"

/**
 * print_dlistint - Prints all the elements of a doubly linked list
 * @h: Pointer to the head of the doubly linked list
 *
 * Description:
 * This function traverses a doubly linked list starting from the head node,
 * printing each element's value on a new line. It counts and returns the
 * total number of nodes in the list.
 *
 * Return: The number of nodes in the list.
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t node_count = 0; /* Counter for the number of nodes */

	/* Traverse the list and print each node's value */
	while (h)
	{
		printf("%d\n", h->n); /* Print the value of the current node */
		h = h->next;		  /* Move to the next node */
		node_count++;		  /* Increment the node counter */
	}

	return (node_count); /* Return the total number of nodes */
}
