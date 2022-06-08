#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle and 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *lower = list;
	listint_t *higher = list;

	if (list == NULL)
		return (0);

	while (lower && higher && higher->next)
	{
		lower = lower->next;
		higher = higher->next->next;
		if (lower == higher)
			return (1);
	}

	return (0);
}
