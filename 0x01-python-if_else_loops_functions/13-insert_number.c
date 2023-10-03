#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted linked list
 * @head: pointer to pointer of the first node in the linked list
 * @number: the number to insert into the linked list
 * Return: the address of the new node else NULL on fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = NULL, *last = NULL, *curr = NULL;

	/* if no head return NULL */
	if (!head)
		return (NULL);

	/* create node */
	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;

	/* find the node greater than node and insert node before */
	curr = *head;
	while (curr && curr->n <= node->n)
	{
		last = curr;
		curr = curr->next;
	}

	if (last)
		node->next = curr, last->next = node;
	else
		node->next = *head, *head = node;
	return (node);
}
