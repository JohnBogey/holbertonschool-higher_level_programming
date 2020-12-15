#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if list is palindrome
 * @head: pointer to head of list
 * Return: 0 if not a palindrome 1 if a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *t_for, *t_rev;
	int length = 0, half = 0, i, j;

	t_for = *head;
	t_rev = *head;

	if (t_for->next == NULL || t_for->next->next == NULL)
		return (1);

	while (t_for != NULL)
	{
		length++;
		t_for = t_for->next;
	}
	half = length / 2;
	if (length % 2 != 0)
		half += 1;

	for (i = 0; i <= half; i++)
	{
		t_for = *head;
		for (j = 1; j < length - i; j++)
			t_for = t_for->next;
		if (t_for->n != t_rev->n)
			return (0);
		t_rev = t_rev->next;
	}
	return (1);
}
