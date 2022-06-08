#include "lists.h"
#include <stdlib.h>
#include <unistd.h>

/**
 * insert_node - inserts a number in an ordered linked list
 * @head: double pointer to the linked list
 * @number: number to insert in the new node
 *
 * Return: address of the new node, or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *a = NULL;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);

	a = malloc(sizeof(listint_t));
	if (!a)
		return (NULL);
	a->n = number;
	a->next = NULL;

	if (!*head || (*head)->n > number)
	{
		a->next = *head;
		return (*head = a);
	}
	else
	{
		while (current && current->n < number)
		{
			temp = current;
			current = current->next;
		}
		temp->next = a;
		a->next = current;
	}

	return (a);
}
