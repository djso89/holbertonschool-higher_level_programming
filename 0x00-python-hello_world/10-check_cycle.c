#include "lists.h"
/**
 * check_cycle - a function that checks if singly linked list
 * has a cycle in it
 * @list: list nodes
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp0, *tmp1;

	tmp0 = list;
	tmp1 = list;

	while (tmp0 && tmp1 && tmp1->next)
	{
		tmp0 = tmp0->next;
		tmp1 = tmp1->next->next;
		if (tmp0 == tmp1)
		{
			return (1);
		}
	}
	return (0);
}
