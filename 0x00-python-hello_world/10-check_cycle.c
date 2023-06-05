#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if singly linked list is a cycle
 * Return: 0 if no cycle, 1 is yes
*/
int check_cycle(listint_t *list)
{
listint_t *s, *f;

if (list == NULL || list->next == NULL)
return (0);
s = list;
f = list->next;
while (f && s && f->next)
{
if (s == f)
return (1);
s = s->next;
f = f->next->next;
}
return (0);
}
