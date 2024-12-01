#include "lists.h"
#include <stdlib.h>

/**
 * add_dnodeint - Adds a new node at the beginning of a dlistint_t list
 * @head: Double pointer to the head of the doubly linked list
 * @n: Integer value to store in the new node
 *
 * Description:
 * This function creates a new node with the given value `n` and inserts it
 * at the beginning of the doubly linked list. It properly adjusts the
 * `prev` and `next` pointers of the new node and the existing head node.
 *
 * Return:
 * The address of the new element, or NULL if memory allocation fails.
 */

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new_node;

	/* Validate input */
	if (head == NULL)
		return (NULL);

	/* Allocate memory for the new node */
	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
		return (NULL);

	/* Initialize the new node */
	new_node->n = n;
	new_node->prev = NULL;
	new_node->next = *head;

	/* Update the existing head node if it exists */
	if (*head != NULL)
		(*head)->prev = new_node;

	/* Update the head to point to the new node */
	*head = new_node;

	return (new_node);
}
