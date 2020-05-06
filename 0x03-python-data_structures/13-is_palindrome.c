#include "lists.h"
/**
 * reverse - a function that reverses the linked list
 * @head: address of the starting node in linked list
 * Return: new reversed linked list
 */
listint_t *reverse(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;
	return (*head);
}
/**
 * is_palindrome - a function that checks if a singly linked
 * list is a palindrome
 * @head: address of the starting node in linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *first;
	listint_t *last;

	for (first = *head, last = *head;
	     first && first->next; last = last->next)
	{
		first = first->next->next;
	}
	last = reverse(&last);
	first = *head;
	while (first && last)
	{
		if (first->n != last->n)
			return (0);
		first = first->next;
		last = last->next;
	}
	return (1);
}
