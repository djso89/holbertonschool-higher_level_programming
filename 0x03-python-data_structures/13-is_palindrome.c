#include "lists.h"
/**
 * is_palindrome - a function that checks if a singly linked
 * list is a palindrome
 * @head: address of the starting node in linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp1 = *head;
	listint_t *tmp2 = *head;
	unsigned int i, j, len = 1;

	if (!head)
		return (0);
	if (!*head || (*head)->next == NULL)
		return (1);
	for ( ; tmp2->next; len++, tmp2 = tmp2->next)
		;
	for (i = 0; tmp1; i++)
	{
		if (tmp1 == tmp2 || tmp1->next == tmp2)
			return (1);
		tmp2 = *head;
		for (j = 0; j < (len - i) - 1; j++)
			tmp2 = tmp2->next;
		if (tmp1->n != tmp2->n)
			return (0);
		tmp1 = tmp1->next;
	}
	return (0);
}
