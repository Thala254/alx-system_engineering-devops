#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * infinite_while - creates sleep
 *
 * Description: sleep
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - creates 5 zombie processes
 *
 * Description: make five zombies
 * Return: 0 for success
 */
int main(void)
{
	int i;
	pid_t pidme;

	i = 0;
	while (i < 5)
	{
		pidme = fork();
		if (pidme)
			printf("Zombie process created, PID: %i\n", pidme);
		else
			exit(0);
		i++;
	}
	infinite_while();
	return (0);
}
