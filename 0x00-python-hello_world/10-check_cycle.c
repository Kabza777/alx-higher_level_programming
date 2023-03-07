#include "lists.h"

typedef struct listint_s {
	int n;
	struct listint_s *next;
} listint_t;

/**
 * check_cycle - check if a singly linked list has a cycle
 * @list: a pointer
 * Return: 0 if there is no cycle, 1 if there's a cyle
 */
int check_style(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0);

	slow = fast = list;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (-1);
	}
