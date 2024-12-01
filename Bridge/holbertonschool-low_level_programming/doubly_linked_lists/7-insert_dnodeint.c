#include "lists.h"
#include <stdlib.h>

/**
 * insert_dnodeint_at_index - Inserts a new node at a given position
 * @h: Double pointer to the head of the doubly linked list
 * @idx: Index where the new node should be inserted
 * @n: Integer value for the new node
 *
 * Description:
 * This function inserts a new node at the specified index in the list.
 * If the index is beyond the current length, the function returns NULL.
 *
 * Return:
 * The address of the newly inserted node, or NULL if the insertion fails.
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *current = *h;
	dlistint_t *new_node;

	/* Handle the case where the index is 0 */
	if (idx == 0)
		return (add_dnodeint(h, n));

	/* Traverse the list to find the insertion point */
	while (current && idx > 1)
	{
		current = current->next;
		idx--;
	}

	/* If current is NULL, the index is out of range */
	if (!current)
		return (NULL);

	/* Handle the case where the new node is inserted at the end */
	if (!current->next)
		return (add_dnodeint_end(h, n));

	/* Allocate memory for the new node */
	new_node = malloc(sizeof(dlistint_t));
	if (!new_node)
		return (NULL);

	/* Initialize the new node */
	new_node->n = n;
	new_node->prev = current;
	new_node->next = current->next;

	/* Update the adjacent nodes' pointers */
	current->next->prev = new_node;
	current->next = new_node;

	return (new_node);
}
