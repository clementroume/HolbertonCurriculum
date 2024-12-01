#include "lists.h"

/**
 * dlistint_len - Counts the elements in a doubly linked list
 * @h: Pointer to the head of the doubly linked list
 *
 * Description:
 * This function traverses a doubly linked list and counts the
 * total number of nodes present in it.
 *
 * Return: The number of nodes in the list.
 */

size_t dlistint_len(const dlistint_t *h)
{
	size_t node_count = 0; /* Counter for the number of nodes */

	/* Traverse the list and count each node */
	while (h)
	{
		node_count++; /* Increment the counter */
		h = h->next;  /* Move to the next node */
	}

	return (node_count); /* Return the total number of nodes */
}
