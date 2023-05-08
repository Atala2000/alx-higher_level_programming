#include "lists.h"
/**
 * check_cycle - singly linked list is checked
 * @list: listpoint
 * Return: 0 or 1
 **/
int check_cycle(listint_t *list)
{
	listint_t *p;
	listint_t *per;

	p = list;
	per = list;
	while (list && p && p->next)
	{
		list = list->next;
		p = p->next->next;

		if (list == p)
		{
			list = per;
			per = p;
			while (1)
			{
				p = per;
				while (p->next != list && p->next != per)
				{
					p = p->next;
				}
				if (p->next == list)
					break;

				list = list->next
			}
			return (1);
		}
	}

	return (0);
}
