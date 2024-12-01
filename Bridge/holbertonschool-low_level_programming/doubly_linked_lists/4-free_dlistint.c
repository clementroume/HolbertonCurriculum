#include "lists.h"
#include <stdlib.h>

/**
 * free_dlistint - Frees a doubly linked list
 * @head: Pointer to the head of the doubly linked list
 *
 * Description:
 * This function traverses a doubly linked list and frees each node.
 * It ensures that all dynamically allocated memory for the list is released.
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *current;

	/* Initialize the current pointer to the head of the list */
	current = head;

	/* Traverse the list and free each node */
	while (current)
	{
		head = current->next; /* Move to the next node */
		free(current);		  /* Free the current node */
		current = head;		  /* Update the current pointer */
	}
}
