#include "lists.h"
#include <stdlib.h>

/**
 * add_dnodeint_end - Adds a new node at the end of a dlistint_t list
 * @head: Double pointer to the head of the doubly linked list
 * @n: Integer value to store in the new node
 *
 * Description:
 * This function creates a new node with the value `n` and appends it
 * to the end of the doubly linked list. It properly adjusts the
 * `prev` and `next` pointers of the involved nodes.
 *
 * Return:
 * The address of the new element, or NULL if memory allocation fails.
 */

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new_node, *current;

	/* Validate input */
	if (head == NULL)
		return (NULL);

	/* Allocate memory for the new node */
	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
		return (NULL);

	/* Initialize the new node */
	new_node->n = n;
	new_node->next = NULL;

	/* If the list is empty, set the new node as the head */
	if (*head == NULL)
	{
		new_node->prev = NULL;
		*head = new_node;
		return (new_node);
	}

	/* Traverse to the last node of the list */
	current = *head;
	while (current->next != NULL)
		current = current->next;

	/* Update pointers to append the new node */
	current->next = new_node;
	new_node->prev = current;

	return (new_node);
}
