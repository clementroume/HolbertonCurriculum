#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - Deletes the node at a specific index a list.
 * @head: Double pointer to the head of the doubly linked list
 * @index: Index of the node to be deleted (starting from 0)
 *
 * Description:
 * This function removes a node from a list at the specified index.
 * If the index is valid, it updates the adjacent nodes' pointers.
 * If the index is out of range, it returns -1.
 *
 * Return:
 * 1 if the node was successfully deleted, -1 if it failed.
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *temp = *head;

	/* Check if the list is empty or the head is NULL */
	if (!head || !*head)
		return (-1);

	/* Traverse the list to find the node at the given index */
	while (temp && index--)
		temp = temp->next;

	/* If temp is NULL, the index was out of range */
	if (!temp)
		return (-1);

	/* If the node to delete is the first node */
	if (temp->prev)
		temp->prev->next = temp->next;
	else
		*head = temp->next; /* If it's the first node, update head */

	/* If the node to delete is not the last node */
	if (temp->next)
		temp->next->prev = temp->prev;

	/* Free the memory of the node */
	free(temp);

	return (1); /* Successfully deleted the node */
}
