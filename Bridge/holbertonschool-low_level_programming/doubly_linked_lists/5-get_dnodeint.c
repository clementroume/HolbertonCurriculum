#include "lists.h"

/**
 * get_dnodeint_at_index - Retrieves the nth node of a doubly linked list
 * @head: Pointer to the head of the doubly linked list
 * @index: Index of the node to retrieve (starting at 0)
 *
 * Description:
 * This function iterates through a doubly linked list to locate the node
 * at the given index. If the index is out of range, it returns NULL.
 *
 * Return: Pointer to the node at the specified index, or NULL if not found
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int current_index = 0;

	/* Traverse the list until the desired index is reached or the list ends */
	while (head)
	{
		if (current_index == index)
			return (head); /* Return the node if the index matches */
		head = head->next;
		current_index++;
	}

	/* If the index is out of range, return NULL */
	return (NULL);
}
