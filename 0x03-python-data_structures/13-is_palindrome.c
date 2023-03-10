#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to head of list
 * Return: 1 if list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *next = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	if (fast != NULL)
		slow = slow->next;

	while (prev != NULL)
	{
		if (prev->n != slow->n)
		{
			is_palindrome = 0;
			break;
		}

		prev = prev->next;
		slow = slow->next;
	}

	/* restore the original list */
	fast = prev;
	prev = NULL;

	while (fast != NULL)
	{
		next = fast->next;
		fast->next = prev;
		prev = fast;
		fast = next;
	}

	*head = prev;

	return (is_palindrome);
}
