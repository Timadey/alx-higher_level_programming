#include "lists.h"
/**
 * check_palin - check if a linked list is plaindrome
 * @h: of the link list
 * @next: next pointer to head
 * Return: pointer
 */
bool check_palin(listint_t **h, listint_t *next)
{
	listint_t *current = NULL;
	bool palin = true;

	if (next != NULL)
	{
		current = next;
		next = current->next;
		palin = check_palin(h, next);
	}
	if (current == NULL)
		return true;
	if (palin)
	{
		if ((*h)->n != current->n)
		{
			palin = false;
			return (palin);
		}
		else
		{
			*h = (*h)->next;
			palin = true;
			return (palin);
		}
	}
	else
		return (false);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *next;

	if (current == NULL)
		return (1);
	if (current->next != NULL)
		next = current->next;
	else
		return (1);
	if (check_palin(head, next))
		return (1);
	else
		return (0);
}

/**
 * transverse_listint - transverse a listint_t list
 * this function might not work, test it first
 * @head: head of the listint_t list
 * Return: the head of the transversed list
 */
listint_t *transverse_listint(listint_t **head)
{
	listint_t *h = *head;
	listint_t *prev = h;
	listint_t *current = prev->next;
	listint_t *next = current->next;

	prev->next = NULL;
	while (next != NULL)
	{
		current->next = prev;
		prev = current;
		current = next;
		next = current->next;
	}
	current->next = prev;
	h = current;
	return (h);
}
