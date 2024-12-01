#include "lists.h"

/**
 * sum_dlistint - Calculates the sum of all the data in a doubly linked list
 * @head: Pointer to the head of the doubly linked list
 *
 * Description:
 * This function traverses a doubly linked list and calculates the sum
 * of the `n` values stored in each node. If the list is empty, it
 * returns 0.
 *
 * Return:
 * The sum of all the node values, or 0 if the list is empty.
 */
int sum_dlistint(dlistint_t *head)
{
	int sum = 0; /* Initialize sum to 0 */

	/* Traverse the list and accumulate the sum */
	while (head)
	{
		sum += head->n;	   /* Add the current node's value to sum */
		head = head->next; /* Move to the next node */
	}

	return (sum); /* Return the total sum */
}
