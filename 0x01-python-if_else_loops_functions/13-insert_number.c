#include "lists.h"
/**
 * insert_node - adds a sorted node in a linked list
 * @head: double pointer of a linked list
 * @number: Number of data of linked list
 * Return: The address of the new node or NULL if it failed
 *                     _
 *     /\             | |
 *    /  \   _ __   __| |_   _
 *   / /\ \ | '_ \ / _` | | | |
 *  / ____ \| | | | (_| | |_| |
 * / /    \ \_| | |\__, |\__, |
 * | |     \_DEC| |2020_| __/ |
 * | |     ___  _ __   __|___/_
 * | |    / _ \| '_ \ / _ \_  /
 * | |___| (_) | |_) | .__// /_
 * |______\___/| .__/ \___/___|
 *             | |
 *             |_|
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *tmp = NULL;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	tmp = *head;
	if(tmp && tmp->n < number)
	{
		while(tmp->next && tmp->next->n < number)
			tmp = tmp->next;
		new->next = tmp->next;
		tmp->next = new;
	}
	else
	{
		new->next = *head;
		*head = new;
	}
	new->n = number;
	return (new);
}
