#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - a function that inserts a number into a sorted
 * singly linked list
 * @head: start of the linked list
 * @number: integer to insert
 * Return: the address of the new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *curr = *head;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!(*head))
		*head = new;
	for ( ; curr->next != NULL && curr->next->n < new->n;
	     curr = curr->next)
		;
	new->next = curr->next;
	curr->next = new;
	return (new);
}
