#include "lists.h"
/**
 * pal - compares list to find matching numbers
 * @head: pointer that checks from top to bottom
 * @tail: pointer that checks from bottom to top
 * Return: Pointer to next position in list, or NULL if no match
 */

listint_t *pal(listint_t *head, listint_t *tail)
{
	if (!tail->next)
		return (head->next);
	tail = tail->next;
	if (!tail->next)
	{
		if (head->n != head->next->n)
			return (NULL);
		if (!head->next->next)
			return (head);
		return (head->next->next);
	}
	tail = pal(head->next, tail->next);
	if (!tail)
		return (NULL);
	if (tail->n == head->n)
	{
		if (!tail->next)
			return (head);
		return (tail->next);
	}
	return (NULL);
}
/**
 * is_palindrome - compares list to find matching items
 * @head: double pointer to list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (!head || !*head || !(*head)->next)
		return (1);

	if (pal(*head, *head))
		return (1);
	return (0);
}
