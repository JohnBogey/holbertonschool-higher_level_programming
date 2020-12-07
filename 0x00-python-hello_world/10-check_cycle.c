#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks list for loop
 * @list:singly linked list
 * Return: 0 on no cycle 1 on cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *short_legs, *long_legs;

	if (list == NULL)
		return (0);
	if (list == list->next)
		return (1);

	short_legs = list;
	long_legs = list;

	while (long_legs->next->next != NULL)
	{
		short_legs = short_legs->next;
		long_legs = long_legs->next->next;
		if (short_legs == long_legs)
			return (1);
	}
	return (0);
}
